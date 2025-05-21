from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
from typing import List, Tuple

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return "MType([" + ",".join(str(x) for x in self.partype) + "]," + str(self.rettype) + ")"

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"

class StaticChecker(BaseVisitor,Utils):
    def __init__(self,ast):
        self.ast = ast
        self.struct: list[StructType] = []
        self.interface: list[InterfaceType] = []
        self.global_constant: List[Tuple[ConstDecl, bool]] = []
        self.global_variable: list[Tuple[VarDecl, bool]] = []
        self.global_envi = [
            [
                Symbol("getInt",MType([],IntType())),
                Symbol("putInt",MType([ParamDecl("i", IntType())],VoidType())),
                Symbol("putIntLn", MType([ParamDecl("i", IntType())], VoidType())),
                
                Symbol("getFloat", MType([], FloatType())),
                Symbol("putFloat", MType([ParamDecl("f", FloatType())], VoidType())),
                Symbol("putFloatLn", MType([ParamDecl("f", FloatType())], VoidType())),

                Symbol("getBool", MType([], BoolType())),
                Symbol("putBool", MType([ParamDecl("b", BoolType())], VoidType())),
                Symbol("putBoolLn", MType([ParamDecl("b", BoolType())], VoidType())),

                Symbol("getString", MType([], StringType())),
                Symbol("putString", MType([ParamDecl("s", StringType())], VoidType())),
                Symbol("putStringLn", MType([ParamDecl("s", StringType())], VoidType())),

                Symbol("putLn", MType([], VoidType()))
            ]
        ]
        self.current_function: FuncDecl = None
        self.current_struct: StructType = None
        self.current_interface: InterfaceType = None
    
    def check(self):
        return self.visit(self.ast,self.global_envi)

    

#####     PROGRAM       ######################################################################################
    def visitProgram(self, ast: Program, c):
        # Self.visit các Struct/Interface vì chúng là Global_Scope
        # Nhưng bên trong Struct/Interface có thể sử dụng constant/variable --> cũng phải lưu vào
        c = [[]] + self.global_envi        
        for i in ast.decl:
            if isinstance(i, (StructType, InterfaceType)):
                if self.lookup(i.name, c[-2] + c[-1], lambda x: x.name):
                    raise Redeclared(Type(), i.name)
                c[0] += [Symbol(i.name, None, None)]
                self.visit(i, c)
            if isinstance(i, FuncDecl):
                if self.lookup(i.name, c[-2] + c[-1], lambda x: x.name):
                    raise Redeclared(Function(), i.name)
                c[0] += [Symbol(i.name, MType(i.params, i.retType), None)]
            elif isinstance(i, ConstDecl):
                self.global_constant += [(i, True)]
            elif isinstance(i, VarDecl):
                self.global_variable += [(i, True)]

        # self.visit các Method
        list(map(lambda x: self.visit(x, c), list(filter(lambda x: isinstance(x, MethodDecl), ast.decl))))

        # cờ flag của Constant/Variable declare phải được reset lại False, khi nào self.visit thì mới bật True
        self.global_constant = list(map(lambda x: (x[0], False), self.global_constant))
        self.global_variable = list(map(lambda x: (x[0], False), self.global_variable))

        # self.visit lại từ đầu (ngoại trừ những declare không phải Struct/Interface)
        c = [[]] + c 
        remainingDecl = list(filter(lambda x: not isinstance(x, MethodDecl), ast.decl))
        for decl in remainingDecl:
            if isinstance(decl, (StructType, InterfaceType)):
                for env in c[:-2]:
                    exist = self.lookup(decl.name, env, lambda x: x.name)
                    if exist:
                        raise Redeclared(Type(), decl.name)
                c[0] += [Symbol(decl.name, None, None)]
            else:
                c = self.visit(decl, c)




#####     BLOCK      ##############################################################################################
    def visitBlock(self, ast: Block, c: List[List[Symbol]]):
        def safe_visit(x, y):
            if isinstance(y, FuncCall):
                result = self.visitFuncCall(y, x, True)
            elif isinstance(y, MethCall):
                result = self.visitMethCall(y, x, True)
            else:
                result = self.visit(y, x) 
            return result if isinstance(result, type(c)) else x 
        
        return reduce(safe_visit, ast.member, c)

        
        

#####     DECLARED STATEMENT      #############################################################################
    def compareArrayType(self, x1: ArrayType, x2: ArrayType):
        """ Hàm kiểm tra xem 2 arrayType có giống nhau không """
        checkDimensionList = x1.dimens == x2.dimens
        if isinstance(x1.eleType, Id) and isinstance(x2.eleType, Id):
            checkElementType = self.compareType(x1.eleType, x2.eleType)
        else:
            checkElementType = \
                (type(x1.eleType) is type(x2.eleType)) or \
                (isinstance(x1.eleType, FloatType) and isinstance(x2.eleType, IntType))
        return checkDimensionList and checkElementType

    def compareType(self, x1, x2):
        """ Hàm kiểm tra xem 2 StructType/InterfaceType có giống nhau không """
        return x1.name == x2.name

    def struct_implement_all_prototype_of_interface (self, x1: InterfaceType, x2: StructType):
        """ Hàm kiểm tra xem StructType có triển khai toàn bộ Prototype của Interface không """
        for prototype in x1.methods:
            exist = self.lookup(prototype.name, x2.methods, lambda x: x.fun.name)
            if not exist:
                return False
            prototype_paramsType_list = list(map(lambda x: type(x), prototype.params))
            exits_paramsType_list = list(map(lambda x: type(x.parType), exist.fun.params))
            if prototype_paramsType_list != exits_paramsType_list:
                return False
            if not (type(prototype.retType) is type(exist.fun.retType)):
                return False
            if isinstance(prototype.retType, Id) and isinstance(exist.fun.retType, Id):
                return self.compareType(prototype.retType, exist.fun.retType)
        return True

    def checkAssignType (self, ast, LHSType: Type, RHSType: Type):
        """ Hàm kiểm tra kiểu giữa LHS và RHS theo quy tắc Type của AssignStatement """
        if isinstance(RHSType, NilLiteral):
            if not isinstance(LHSType, Id):
                raise TypeMismatch(ast)
            return
        
        if isinstance(LHSType, VoidType):
            raise TypeMismatch(ast)

        elif isinstance(LHSType, ArrayType) and isinstance(RHSType, ArrayType):
            if not self.compareArrayType(LHSType, RHSType):
                raise TypeMismatch(ast)
        
        elif isinstance(LHSType, Id) and isinstance(RHSType, Id):
            LHS_type = self.lookup(LHSType.name, self.struct + self.interface, lambda x: x.name)
            if not LHS_type: raise Undeclared(Type(), LHSType.name)
            RHS_type = self.lookup(RHSType.name, self.struct + self.interface, lambda x: x.name)
            if not RHS_type: raise Undeclared(Type(), RHSType.name)

            if isinstance(LHS_type, StructType) and isinstance(RHS_type, InterfaceType):
                raise TypeMismatch(ast)
            
            if (isinstance(LHS_type, StructType) and isinstance(RHS_type, StructType)) or \
                (isinstance(LHS_type, InterfaceType) and isinstance(RHS_type, InterfaceType)):
                if not self.compareType(LHS_type, RHS_type):
                    raise TypeMismatch(ast)
            
            elif isinstance(LHS_type, InterfaceType) and isinstance(RHS_type, StructType):
                if not self.struct_implement_all_prototype_of_interface(LHS_type, RHS_type):
                    raise TypeMismatch(ast)
            
        elif (not (type(LHSType) is type(RHSType))) and \
        (not (isinstance(LHSType, FloatType) and isinstance(RHSType, IntType))):
            raise TypeMismatch(ast)



# --------  Variable declare    ----------------------------------
    def visitVarDecl(self, ast: VarDecl, c):
        exist = self.lookup(ast.varName, c[0] + c[-1], lambda x: x.name)
        if exist:
            raise Redeclared(Variable(), ast.varName)
        
        if ast.varType and isinstance(ast.varType, ArrayType):
            ast.varType = self.visit(ast.varType, c)
            
        if ast.varInit:
            init_type = self.visit(ast.varInit, c)
            if not ast.varType:
                ast.varType = init_type
            else: 
                self.checkAssignType(ast, ast.varType, init_type)
            if isinstance(ast.varInit, (BinaryOp, UnaryOp)):
                ast.varInit = self.calculate_Binary_Unary_value(ast.varInit, c)
        # Đánh dấu mốc hiệu lực của Variable Declare
        self.global_variable = [gv if gv[0].varName != ast.varName else (ast, True) for gv in self.global_variable]

        c[0] += [Symbol(ast.varName, ast.varType, ast.varInit)]
        return c
        
# --------  Constant declare    -----------------------------------
    def visitConstDecl(self, ast: ConstDecl, c):
        exist = self.lookup(ast.conName, c[0] + c[-1], lambda x: x.name)
        if exist:
            raise Redeclared(Constant(), ast.conName)
        else:
            if ast.iniExpr: 
                ast.conType = self.visit(ast.iniExpr, c)
                if isinstance(ast.iniExpr, (BinaryOp, UnaryOp)):
                    ast.iniExpr = self.calculate_Binary_Unary_value(ast.iniExpr, c)
            # Đánh dấu mốc hiệu lực của Constant Declare
            self.global_constant = [gc if gc[0].conName != ast.conName else (ast, True) for gc in self.global_constant]
            
            c[0] += [Symbol(ast.conName, ast.conType, ast.iniExpr)]
            return c


        
# --------  Parameter declare (for Function declare)   --------------
    def visitParamDecl(self, ast: ParamDecl, c):
        exist = self.lookup(ast.parName, c[0], lambda x: x.name)
        if exist: 
            raise Redeclared(Parameter(), ast.parName)
        else:
            if isinstance(ast.parType, ArrayType): # Tính toán giá trị Dimension nếu là ArrayType
                ast.parType = self.visit(ast.parType, c)
            c[0] += [Symbol(ast.parName, ast.parType, None)]
            return c
    
# --------  Function declare    ------------------------------------
    def visitFuncDecl(self, ast: FuncDecl, c):
        # Kiểm tra trong Symbol List, có tồn tại name trùng với FuncDecl hay không
        exist = self.lookup(ast.name, c[0], lambda x: x.name)
        if exist:
            raise Redeclared(Function(), ast.name)
        else:
            if isinstance(ast.retType, ArrayType): # Tính toán giá trị Dimension nếu là ArrayType
                ast.retType = self.visit(ast.retType, c)
            c[0] += [Symbol(ast.name, MType(ast.params, ast.retType), None)]
            newC = reduce(lambda x, y: self.visit(y, x), ast.params, [[]] + c)
            self.current_function = ast
            self.visit(ast.body, [[]] + newC)
            return c
        
# --------  Method declare    ---------------------------------------
    def visitMethodDecl(self, ast: MethodDecl, c):
        struct_interface = self.lookup(ast.recType.name, self.struct + self.interface, lambda x: x.name)
        if isinstance(struct_interface, StructType):
            self.current_struct = struct_interface
            exist_methodName= self.lookup(ast.fun.name, self.current_struct.methods, lambda x: x.fun.name)
            exist_fieldName = self.lookup(ast.fun.name, self.current_struct.elements, lambda x: x[0])
            if exist_methodName or exist_fieldName:
                raise Redeclared(Method(), ast.fun.name)
            else: 
                self.current_struct = StructType(self.current_struct.name, self.current_struct.elements, self.current_struct.methods + [ast])
                self.struct = [s if s.name != self.current_struct.name else self.current_struct for s in self.struct]
                newC = [[]] + c
                newC[0] += [Symbol(ast.receiver, ast.recType, None)]

                newC = reduce(lambda x, y: self.visit(y, x), ast.fun.params, [[]] + newC)
                if isinstance(ast.fun.retType, ArrayType): # Tính toán giá trị Dimension nếu là ArrayType
                    ast.fun.retType = self.visit(ast.fun.retType, newC)
                
                self.current_function = ast.fun
                self.visit(ast.fun.body, [[]] + newC)
                
                return c
        elif isinstance(struct_interface, InterfaceType):
            self.current_interface = struct_interface
            existName = self.lookup(ast.fun.name, self.current_interface.methods, lambda x: x.name)
            if existName:
                raise Redeclared(Method(), ast.fun.name)
            # else:
            #     self.current_interface = InterfaceType(self.current_interface.name, self.current_interface.methods + [ast])
            return c
        elif not struct_interface: 
            # Lỗi chưa khai báo ReceiverType không có trong mô tả nên xem như không xảy ra, không test lỗi này.
            raise Undeclared(Type(), ast.recType.name)



# --------  Struct type declare    --------------------------------
    def visitStructType(self, ast: StructType, c):
        # Không cần kiểm tra Redeclare, vì đã được xử lý trong Program
        # Kiểm tra từng phần tử trong Struct, xem đã khai báo chưa --> Redeclared Field
        self.current_struct = self.lookup(ast.name, self.struct, lambda x: x.name)

        elementStruct = []
        for field_name, field_type in ast.elements:
            exist =  self.lookup(field_name, elementStruct, lambda x: x.name)
                # self.lookup(field_name, self.current_struct.methods, lambda x: x.fun.name)
            if exist: 
                raise Redeclared(Field(), field_name)
            if isinstance(field_type, ArrayType):
                field_type = self.visit(field_type, c)
            elementStruct += [Symbol(field_name, field_type, None)]
        self.struct += [ast]
            
# --------  Prototype declare (for Interface type declare)   -------
    def visitPrototype(self, ast: Prototype, c):
        exist = self.lookup(ast.name, c, lambda x: x.name)
        if exist: 
            raise Redeclared(Prototype(), ast.name)
        else:
            # Tính toán giá trị Dimension nếu là ArrayType
            ast.params = [self.visit(e, c) if isinstance(e, ArrayType) else e for e in ast.params]
            if isinstance(ast.retType, ArrayType):
                ast.retType = self.visit(ast.retType, c)
            c += [Symbol(ast.name, MType(ast.params, ast.retType), None)]
            return c
    
# --------  Interface type declare    --------------------------------
    def visitInterfaceType(self, ast: InterfaceType, c):
        # Không cần kiểm tra Redeclare, vì đã được xử lý trong Program
        reduce(lambda x, y: self.visit(y, x), ast.methods, [])
        self.interface += [ast]



#####     FOR STATEMENT      ######################################################################################
# --------  For basic    --------------------------------
    def visitForBasic(self, ast: ForBasic, c : List[List[Symbol]]): 
        if not (isinstance(self.visit(ast.cond, c), BoolType)):
            raise TypeMismatch(ast)
        self.visit(ast.loop, [[]] + c)
        return c

# --------  For step   ----------------------------------
    def visitForStep(self, ast: ForStep, c: List[List[Symbol]]): 
        newC = self.visit(Block([ast.init]), [[]] + c)
        
        if not isinstance(self.visit(ast.cond, newC), BoolType):
            raise TypeMismatch(ast)
        
        self.visit(Block([ast.upda] + ast.loop.member), newC)
        return c

# --------  For each   ----------------------------------
    def visitForEach(self, ast: ForEach, c: List[List[Symbol]]):
        # Kiểm tra lỗi chưa khai báo index, value
        for env in c[:-2]:
            existIndexName = self.lookup(ast.idx.name, env, lambda x: x.name)
            if existIndexName: break
        else: raise Undeclared(Identifier(), ast.idx.name)
        
        for env in c[:-2]:
            existValueName = self.lookup(ast.value.name, env, lambda x: x.name)
            if existValueName: break
        else: raise Undeclared(Identifier(), ast.value.name)

        # Lỗi arrayType của arr
        arrType = self.visit(ast.arr, c)
        if not isinstance(arrType, ArrayType):
            raise TypeMismatch(ast)
        if len(arrType.dimens) > 1:
            valueType = ArrayType(arrType.dimens[1:], arrType.eleType)
        else: 
            valueType = arrType.eleType

        # Kiểm tra lỗi typeMismatch của index (có phải IntType không), value (có trùng khớp với khai báo không)
        if not isinstance(existIndexName.mtype, IntType):
            raise TypeMismatch(ast)
        self.checkAssignType_callStatement(ast, existValueName.mtype, valueType)

        newC = [[]] + c
        newC[0] += [Symbol(ast.idx.name, IntType(), None), Symbol(ast.value.name, valueType, None)]
        self.visit(ast.loop, [[]] + newC)
        return c





#####     EXPRESSION       ######################################################################################
# --------  Identifier   ----------------------------------
    def visitId(self, ast: Id, c: List[List[Symbol]]):
        for env in c:
            exist = self.lookup(ast.name, env, lambda x: x.name)
            if (exist) and (exist.mtype) and (not isinstance(exist.mtype, MType)): # Không return nếu là Id là function/struct/interface
                return exist.mtype 
        # Không tìm thấy Id.name trong c  -> Tìm trong global
        for gc, flag in self.global_constant:
            if (gc.conName == ast.name):
                return self.visit(gc.iniExpr, c)
        for gv, flag in self.global_variable:
            if (flag) and (gv.varName == ast.name):
                if not gv.varInit:
                    return gv.varType
                elif gv.varInit and isinstance(gv.varInit, Id):
                    break
                else:
                    return self.visit(gv.varInit, c)  
        raise Undeclared(Identifier(), ast.name)



# --------  Integer literal   ----------------------------------
    def visitIntLiteral(self, ast: IntLiteral, c): 
        return IntType()

# --------  Float literal   ----------------------------------
    def visitFloatLiteral(self, ast: FloatLiteral, c): 
        return FloatType()

# --------  Boolean literal   ----------------------------------
    def visitBooleanLiteral(self, ast: BooleanLiteral, c): 
        return BoolType()

# --------  String literal   ----------------------------------
    def visitStringLiteral(self, ast: StringLiteral, c): 
        return StringType()

# --------  Array literal   ----------------------------------
    def check_array_elements (self, ast: ArrayLiteral, listDimensionLength: list, listData: list):
        """ 
        Hàm kiểm tra:
        1. Số lượng phần tử có trùng với Dimension đã khai báo không
        2. Type của mỗi phần tử có trùng với Type đã khai báo không
        """
        if not listDimensionLength:
            return True
        # if listDimensionLength[0] != len(listData):
        #     return False

        def checkType(expected_type, actual_type):
            """Hàm phụ: Kiểm tra kiểu dữ liệu có khớp với khai báo không"""
            return (type(expected_type) is type(actual_type)) or \
                (isinstance(expected_type, FloatType) and isinstance(actual_type, IntType))

        for element in listData:
            if isinstance(element, list):  # Nếu phần tử là list => Đệ quy kiểm tra tiếp
                if not self.check_array_elements(ast, listDimensionLength[1:], element):
                    return False
            else:  # Nếu phần tử không phải list => Kiểm tra kiểu của nó
                element_type = self.visit(element, [])
                if not checkType(ast.eleType, element_type):
                    raise TypeMismatch(ast)
    
        return True

    def visitArrayLiteral(self, ast: ArrayLiteral, c): 
        # Kiểm tra xem ArrayType có hợp lệ không
        arrayType = self.visit(ArrayType(ast.dimens, ast.eleType), c)     
        # Kiểm tra Dimension và Type của Literal có hợp lệ chưa    
        isValid_dimension_type = self.check_array_elements(ast, [i.value for i in arrayType.dimens], ast.value)
        if not isValid_dimension_type:
            raise TypeMismatch(ast)
        return ArrayType(arrayType.dimens, arrayType.eleType)


# --------  Struct literal   ----------------------------------
    def visitStructLiteral(self, ast: StructLiteral, c):  
        exist = self.lookup(ast.name, self.struct, lambda x: x.name)
        if not exist:
            raise Undeclared(Type(), ast.name)
        for eleName, eleType in ast.elements:
            existField = self.lookup(eleName, exist.elements, lambda x: x[0])
            if not existField:
                raise Undeclared(Field(), eleName)
            self.visit(eleType, c)
        return Id(ast.name)

# --------  Nil literal   ----------------------------------
    def visitNilLiteral(self, ast: NilLiteral, c): 
        return NilLiteral()



# --------  Function call   ----------------------------------
    def compareArrayType_callStatement(self, x1: ArrayType, x2: ArrayType):
        """ 
            Hàm kiểm tra xem 2 arrayType có giống nhau không theo quy tắc của Return Statement
            Lưu ý: Không có trường hợp đặc biệt giữa Int và Float
        """
        checkDimensionList = x1.dimens == x2.dimens
        if isinstance(x1.eleType, Id) and isinstance(x2.eleType, Id):
            if x1.eleType.name != x2.eleType.name:
                return False
        checkElementType = (type(x1.eleType) is type(x2.eleType))
        return checkDimensionList and checkElementType
    
    def checkAssignType_callStatement (self, ast, expectedType: Type, actualType: Type):
        """ Hàm kiểm tra kiểu giữa expectedType và actualType theo quy tắc Type của Call_Statement """
        if isinstance(actualType, NilLiteral):
            if not isinstance(expectedType, Id):
                raise TypeMismatch(ast)
            return
        
        if not (type(expectedType) is type(actualType)):
            raise TypeMismatch(ast)
        
        if isinstance(expectedType, ArrayType):
            if not self.compareArrayType_callStatement(expectedType, actualType):
                raise TypeMismatch(ast)
        
        elif isinstance(expectedType, Id):
            expected_type = self.lookup(expectedType.name, self.struct + self.interface, lambda x: x.name)
            if not expected_type: raise Undeclared(Type(), expectedType.name)
            actual_type = self.lookup(actualType.name, self.struct + self.interface, lambda x: x.name)
            if not actual_type: raise Undeclared(Type(), actualType.name)

            if (isinstance(expected_type, StructType) and isinstance(actual_type, StructType)) or \
                (isinstance(expected_type, InterfaceType) and isinstance(actual_type, InterfaceType)):
                if not self.compareType(expectedType, actual_type):
                    raise TypeMismatch(ast)
            elif not (type(expected_type) is type(actual_type)):
                raise TypeMismatch(ast)

    def check_return_type_callStatement(self, ast, return_type, stmtType):
        """ Kiểm tra kiểu trả về của hàm/method dựa trên ngữ cảnh (Statement hoặc Expression) """
        if \
        (not stmtType and isinstance(return_type, VoidType)) or \
        (stmtType and not isinstance(return_type, VoidType)):
            raise TypeMismatch(ast)

    def check_parameters_callStatement(self, ast, c, expected_params, given_args):
        """ Kiểm tra số lượng và kiểu tham số của function/method """
        if len(expected_params) != len(given_args):
            raise TypeMismatch(ast)
        
        for i in range(len(given_args)):
            expected_type = expected_params[i].parType if hasattr(expected_params[i], 'parType') else expected_params[i]
            actual_type = self.visit(given_args[i], c)
            self.checkAssignType_callStatement(ast, expected_type, actual_type)


    def visitFuncCall(self, ast: FuncCall, c, stmtType = False):
        # Test_115 -> khi FunCall gọi function có tên trùng với các var khác, thì function sẽ bị che mất --> Không tìm thấy function đó trong scope này nữa
        for env in c[:-2]:
            existOverrideName = self.lookup(ast.funName, env, lambda x: x.name)
            if existOverrideName and not isinstance(existOverrideName.mtype, MType):
                raise Undeclared(Function(), ast.funName)
        
        functionType = self.lookup(ast.funName, c[-2] + c[-1], lambda x: x.name) # Vì 2 list cuối cùng mới chứa các Symbol function (thông thường + buid-in)
        if not functionType:
            raise Undeclared(Function(), ast.funName)
        # Kiểm tra kiểu trả về
        self.check_return_type_callStatement(ast, functionType.mtype.rettype, stmtType)
        # Kiểm tra tham số
        self.check_parameters_callStatement(ast, c, functionType.mtype.partype, ast.args)
            
        return functionType.mtype.rettype
        
    
# --------  Method call   ----------------------------------
    def visitMethCall(self, ast: MethCall, c, stmtType = False):
        myReceiver_type = self.visit(ast.receiver, c)
        if not isinstance(myReceiver_type, Id):
            raise TypeMismatch(ast)

        def lookup_method(name, container,  key_func):
            """ Hàm tìm method trong struct hoặc interface """
            entity = self.lookup(myReceiver_type.name, container, lambda x: x.name)
            return self.lookup(name, entity.methods, key_func) if entity else None

        # Kiểm tra struct trước, nếu không có thì kiểm tra interface
        method = \
            lookup_method(ast.metName, self.struct, lambda x: x.fun.name) or \
            lookup_method(ast.metName, self.interface, lambda x: x.name)
        if not method:
            raise Undeclared(Method(), ast.metName)
        
        return_type = method.fun.retType if hasattr(method, "fun") else method.retType
        params = method.fun.params if hasattr(method, "fun") else method.params
        # Kiểm tra kiểu trả về
        self.check_return_type_callStatement(ast, return_type, stmtType)
        # Kiểm tra tham số
        self.check_parameters_callStatement(ast, c, params, ast.args)
        return return_type

 
# --------  Array access   ----------------------------------
    def visitArrayCell(self, ast: ArrayCell, c): 
        arrayType = self.visit(ast.arr, c) # Vì sẽ visitABC nên nếu có lỗi sẽ raise ngay lập tức, còn không chắc chắn sẽ trả về Type của Array
        indexTypeError = next(filter(lambda x: not isinstance(self.visit(x, c), IntType), ast.idx), False)
        if indexTypeError:
            raise TypeMismatch(ast)
        if len(ast.idx) < len(arrayType.dimens):
            return ArrayType(arrayType.dimens[len(ast.idx):], arrayType.eleType)
        else:
            return arrayType.eleType

# --------   Field access   ----------------------------------
    def visitFieldAccess(self, ast: FieldAccess, c: List[List[Symbol]]):
        myReceiver_type = self.visit(ast.receiver, c)
        if not myReceiver_type:
            raise Undeclared(Variable(), ast.receiver)
        if not isinstance(myReceiver_type, Id):
            raise TypeMismatch(ast)
        else:
            self.current_struct = self.lookup(myReceiver_type.name, self.struct, lambda x: x.name)
            if not self.current_struct:
                raise TypeMismatch(ast)
            else:
                for myName, myType in self.current_struct.elements:
                    if ast.field == myName:
                        return myType
                raise Undeclared(Field(), ast.field)



#####     TYPE      ##############################################################################################
    def visitIf(self, ast: If, c): 
        if not isinstance(self.visit(ast.expr, c), BoolType):
            raise TypeMismatch(ast)
        self.visit(ast.thenStmt, c) if isinstance(ast.thenStmt, If) else self.visit(ast.thenStmt, [[]] + c)
        if ast.elseStmt:
            self.visit(ast.elseStmt, [[]] + c)
        return c
    
    def visitIntType(self, ast: IntType, c):
        return ast

    def visitFloatType(self, ast: FloatType, c): 
        return ast

    def visitBoolType(self, ast: BoolType, c): 
        return ast

    def visitStringType(self, ast: StringType, c): 
        return ast

    def visitVoidType(self, ast: VoidType, c):
        return ast

    # Ví dụ: [3][4] float
    def visitArrayType(self, ast: ArrayType, c): 
        typeError = next(filter(lambda x: not isinstance(self.visit(x, c), (IntType, Id)), ast.dimens), False)
        if typeError:
            raise TypeMismatch(ast)
        # Tính toán dimension_value
        ast.dimens = [self.calculate_Binary_Unary_value(d, c) for d in ast.dimens]
        
        if isinstance(ast.eleType, Id): # Kiểm tra Undeclared Type của elementType
            entity = self.lookup(ast.eleType.name, self.struct + self.interface, lambda x: x.name)
            if not entity:
                raise Undeclared(Type(), ast.eleType.name)
            if isinstance(entity, StructType):
                self.current_struct = entity
            else:
                self.current_interface = entity
        return ast



    def visitAssign(self, ast: Assign, c): 
        if isinstance(ast.lhs, Id):
            for env in c[:-2]:
                exist = self.lookup(ast.lhs.name, env, lambda x: x.name)
                if exist and not isinstance(exist.mtype, MType): # Testcase 118
                    self.checkAssignType(ast, self.visit(ast.lhs, c), self.visit(ast.rhs, c))
                    return c
            else: # Không tồn tại Id_LHS -> Tự động khai báo biến mới
                if isinstance(ast.rhs, (BinaryOp, UnaryOp)):
                    ast.rhs = self.calculate_Binary_Unary_value(ast.rhs, c)
                c[0] += [Symbol(ast.lhs.name, self.visit(ast.rhs, c), ast.rhs)]
        else:
            self.checkAssignType(ast, self.visit(ast.lhs, c), self.visit(ast.rhs, c))
        return c
            
    def visitContinue(self, ast: Continue, c): 
        return c
    
    def visitBreak(self, ast: Break, c): 
        return c

    def visitReturn(self, ast: Return, c): 
        if ast.expr:
            exprType = self.visit(ast.expr, c)
            self.checkAssignType_callStatement(ast, self.current_function.retType, exprType)
        else:
            if not isinstance(self.current_function.retType, VoidType):
                raise TypeMismatch(ast)
        return c

                


    def calculate_Binary_Unary_value (self, ast: Expr, c):
        if isinstance(ast, (IntLiteral, FloatLiteral, BooleanLiteral, StringLiteral)):
            return ast
        elif isinstance(ast, Id):
            # Kiểm tra trong c xem đã có khai báo Constant chưa?
            for env in c[:-2]:
                constantSymbol = self.lookup(ast.name, env, lambda x: x.name)
                if constantSymbol:
                    return self.calculate_Binary_Unary_value(constantSymbol.value, c)
            else: # Duyệt hết c vẫn không tìm thấy, tức là chưa khai báo. Nhưng vẫn còn global_constant
                for i in range(len(self.global_constant)):
                    if self.global_constant[i][0].conName == ast.name:
                        return self.calculate_Binary_Unary_value(self.global_constant[i][0].iniExpr, c)
            # Đã duyệt tất cả những vị trí có thể có, nếu vẫn không thấy ==> raise Undeclared
            raise Undeclared(Identifier(), ast.name)
            
        elif isinstance(ast, BinaryOp):
            left_value = (self.calculate_Binary_Unary_value(ast.left, c)).value
            right_value = (self.calculate_Binary_Unary_value(ast.right, c)).value

            left_type = self.visit(ast.left, c)
            right_type = self.visit(ast.right, c)

            def is_int_or_float(t: Type): 
                return isinstance(t, (IntType, FloatType))

            if ast.op == "+":
                if isinstance(left_type, StringType) and isinstance(right_type, StringType):
                    return StringLiteral(str(left_value + right_value))
                elif is_int_or_float(left_type) and is_int_or_float(right_type):
                    return FloatLiteral(float(left_value + right_value)) if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntLiteral(int(left_value + right_value))

            elif ast.op in ["-", "*", "/"]:
                if is_int_or_float(left_type) and is_int_or_float(right_type):
                    return FloatLiteral(float(eval(str(left_value) + ast.op + str(right_value)))) if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntLiteral(int(eval(str(left_value) + ast.op + str(right_value))))

            elif ast.op == "%":
                if isinstance(left_type, IntType) and isinstance(right_type, IntType):
                    return IntLiteral(int(left_value % right_value))

            elif ast.op in ["==", "!=", "<", ">", "<=", ">="]:
                if isinstance(left_type, (IntType, FloatType, StringType)) and \
                isinstance(right_type, (IntType, FloatType, StringType)) and \
                type(left_type) is type(right_type):
                    return BooleanLiteral(bool(eval(str(left_value) + ast.op + str(right_value))))

            elif ast.op in ["&&", "||"]:
                if isinstance(left_type, BoolType) and isinstance(right_type, BoolType):
                    return BooleanLiteral(bool(left_value and right_value)) if ast.op == "&&" else BooleanLiteral(bool(left_value or right_value))
                
        elif isinstance(ast, UnaryOp):
            expr_value = (self.calculate_Binary_Unary_value(ast.body, c)).value
            expr_type = self.visit(ast.body, c)
            
            if ast.op == "-":
                if isinstance(expr_type, IntType):
                    return IntLiteral(int(-expr_value))
                elif isinstance(expr_type, FloatType):
                    return FloatLiteral(float(-expr_value))
            elif ast.op == "!":
                if isinstance(expr_type, BoolType):
                    return BooleanLiteral(bool(not expr_value))

    def visitBinaryOp(self, ast: BinaryOp, c):
        left_type = self.visit(ast.left, c)
        right_type = self.visit(ast.right, c)

        def is_int_or_float(t: Type): 
            return isinstance(t, (IntType, FloatType))

        if ast.op == "+":
            if isinstance(left_type, StringType) and isinstance(right_type, StringType):
                return StringType()
            elif is_int_or_float(left_type) and is_int_or_float(right_type):
                return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()

        elif ast.op in ["-", "*", "/"]:
            if is_int_or_float(left_type) and is_int_or_float(right_type):
                return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()

        elif ast.op == "%":
            if isinstance(left_type, IntType) and isinstance(right_type, IntType):
                return IntType()

        elif ast.op in ["==", "!=", "<", ">", "<=", ">="]:
            if isinstance(left_type, (IntType, FloatType, StringType)) and \
            isinstance(right_type, (IntType, FloatType, StringType)) and \
            type(left_type) is type(right_type):
                return BoolType()

        elif ast.op in ["&&", "||"]:
            if isinstance(left_type, BoolType) and isinstance(right_type, BoolType):
                return BoolType()
            
        raise TypeMismatch(ast)

    def visitUnaryOp(self, ast: UnaryOp, c):
        exp_type = self.visit(ast.body, c)

        if ast.op == "-":
            if isinstance(exp_type, IntType):
                return IntType()
            elif isinstance(exp_type, FloatType):
                return FloatType()
        elif ast.op == "!":
            if isinstance(exp_type, BoolType):
                return BoolType()

        raise TypeMismatch(ast)
