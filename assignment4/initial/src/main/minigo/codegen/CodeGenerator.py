'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''

""" Nguyễn Lê Hoàng Phúc - 2212629 """

from Utils import *
# from StaticCheck import *
# from StaticError import *
from Emitter import *
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce
from Visitor import *
from AST import *


class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return "MType([" + ",".join(str(x) for x in self.partype) + "]," + str(self.rettype) + ")"

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value, isStatic=True):
        #value: String
        self.isStatic = isStatic
        self.value = value

class ClassType:
    def __init__(self, name):
        #value: Id
        self.name = name

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"



class CodeGenerator(BaseVisitor,Utils):
    def __init__(self):
        self.className = "MiniGoClass"
        self.ast = None
        self.myPath = None
        self.emit = None
        self.list_body_element_in_block = []
        self.list_structType = []
        self.list_interfaceType = []
        self.list_symbol_function = [self.init]
        self.current_struct = None

    def init(self):
        buidIn_function_list = [
            Symbol("getInt", MType([], IntType()), CName("io", True)),
            Symbol("putInt", MType([IntType()], VoidType()), CName("io", True)),
            Symbol("putIntLn", MType([IntType()], VoidType()), CName("io", True)),

            Symbol("getFloat", MType([], FloatType()), CName("io", True)),
            Symbol("putFloat", MType([FloatType()], VoidType()), CName("io", True)),
            Symbol("putFloatLn", MType([FloatType()], VoidType()), CName("io", True)),

            Symbol("getBool", MType([], BoolType()), CName("io", True)),
            Symbol("putBool", MType([BoolType()], VoidType()), CName("io", True)),
            Symbol("putBoolLn", MType([BoolType()], VoidType()), CName("io", True)),

            Symbol("getString", MType([], StringType()), CName("io", True)),
            Symbol("putString", MType([StringType()], VoidType()), CName("io", True)),
            Symbol("putStringLn", MType([StringType()], VoidType()), CName("io", True)),

            Symbol("putLn", MType([], VoidType()), CName("io", True))
        ]
        return buidIn_function_list

    def gen(self, ast, inputDirectory):
        self.ast = ast
        buidIn_function = self.init()
        self.myPath = inputDirectory
        self.emit = Emitter(inputDirectory + "/" + self.className + ".j")
        self.visit(ast, buidIn_function)
       
        
    def emitObjectInit(self, structName=None, list_fields=[]):
        frame = Frame("<init>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<init>", MType([], VoidType()), False, frame))  # Bắt đầu định nghĩa phương thức <init>
        frame.enterScope(True)  
        
        idx = frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(idx, "this", ClassType(structName) if structName else ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))  # Tạo biến "this" trong phương thức <init>
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), idx, frame))  
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))  

        if structName:
            for field_name, field_type in list_fields:
                self.emit.printout(self.emit.emitREADVAR("this", ClassType(structName), idx, frame))  # aload_0
                code, _ = self.visit(self.get_default_value(field_type), self.createNewEnvironment({}, frame=frame))
                self.emit.printout(code)  # ví dụ: iconst_0
                field_type = field_type if not isinstance(field_type, Id) else self.lookup(field_type.name, self.list_structType + self.list_interfaceType, lambda x: x.name)
                self.emit.printout(self.emit.emitPUTFIELD(f"{structName}/{field_name}", field_type, frame))  # putfield PPL3/number I
                
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()  

    def emitParameterizedConstructor(self, structName, fields):
        # param_types lấy từ kiểu từng field (được xem là tham số của constructor)
        param_types = [typ if not isinstance(typ, Id) else self.lookup(typ.name, self.list_structType + self.list_interfaceType, lambda x: x.name) for _, typ in fields]
        frame = Frame("<init>", VoidType())
        
        # Bắt đầu method
        self.emit.printout(self.emit.emitMETHOD("<init>", MType(param_types, VoidType()), False, frame))
        frame.enterScope(True)

        # Đặt chỉ số cho 'this'
        idx_this = frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(idx_this, "this", ClassType(structName), frame.getStartLabel(), frame.getEndLabel(), frame))

        # Tạo biến cho từng param
        param_indices = []
        for i, (fname, ftype) in enumerate(fields):
            ftype = ftype if not isinstance(ftype, Id) else self.lookup(ftype.name, self.list_structType + self.list_interfaceType, lambda x: x.name)
            idx = frame.getNewIndex()
            param_indices.append(idx)
            self.emit.printout(self.emit.emitVAR(idx, fname, ftype, frame.getStartLabel(), frame.getEndLabel(), frame))
            
        # Label bắt đầu
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Gọi super constructor: aload_0 + invokespecial java/lang/Object/<init>()V
        self.emit.printout(self.emit.emitREADVAR("this", ClassType(structName), idx_this, frame))
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        # Gán các tham số constructor vào field
        for idx, (fname, ftype) in enumerate(fields):
            if isinstance(ftype, Id):
                ftype = self.lookup(ftype.name, self.list_structType + self.list_interfaceType, lambda x: x.name)
            # 1. Load 'this' (aload_0)
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(structName), idx_this, frame))
            # 2. Load tham số (từ chỉ số stack param bắt đầu từ 1)
            self.emit.printout(self.emit.emitREADVAR(fname, ftype, idx + 1, frame))
            # 3. putfield
            self.emit.printout(self.emit.emitPUTFIELD(structName + "/" + fname, ftype, frame))

        # return
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))

        frame.exitScope()


    def emitObjectCInit(self, ast: Program, env):
        frame = Frame("<cinit>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<clinit>", MType([], VoidType()), True, frame)) 
        frame.enterScope(True)  

        env['frame'] = frame
        self.visit(Block([decl for decl in ast.decl if (isinstance(decl, ConstDecl)) or (isinstance(decl, VarDecl) and decl.varInit)]), env)
        
        self.emit.printout(self.emit.emitRETURN(VoidType(),frame))  
        frame.exitScope()
        self.emit.printout(self.emit.emitENDMETHOD(frame))  




################################################################################################
#-----------     UTILITY FUNCTION      ---------------------------------------------------------
    def createNewEnvironment(self, previousO, **key_value_dict):
        returnO = previousO.copy()
        returnO.update(key_value_dict)
        return returnO

    def code_type_convert(self, lhsType: Type, rhsType: Type, frame: Frame):
        if type(lhsType) is FloatType and type(rhsType) is IntType:
            return self.emit.emitI2F(frame)
        else:
            return ""



################################################################################################
#-----------     PROGRAM DEFINITION      -------------------------------------------------------
    def visitProgram(self, ast: Program, c):
        self.ast = ast
        o = {}
        o['symbolTable'] = [c]
        self.list_structType = list(filter(lambda i: isinstance(i, StructType), ast.decl))
        self.list_interfaceType = list(filter(lambda i: isinstance(i, InterfaceType), ast.decl))
        self.list_symbol_function = \
            c + [Symbol(
                        item.name, 
                        MType(list(map(lambda x: x.parType if not isinstance(x.parType, Id) else self.lookup(x.parType.name, self.list_interfaceType + self.list_structType, lambda x: x.name), item.params)), item.retType if not isinstance(item.retType, Id) else self.lookup(item.retType.name, self.list_interfaceType + self.list_structType, lambda x: x.name)),
                        CName(self.className)) 
                 for item in ast.decl if isinstance(item, FuncDecl)]
        
        
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))

        # visit VARDECL
        for decl in ast.decl:
            if isinstance(decl, VarDecl):
                o = self.visitVarDecl_Special(decl, o)
            elif isinstance(decl, ConstDecl):
                o = self.visitVarDecl_Special(VarDecl(decl.conName, decl.conType, decl.iniExpr), o)
                
        # visit FUNCDECL
        o = reduce(lambda x, y: self.visit(y, x), list(filter(lambda i: isinstance(i, FuncDecl) and i.name != "main", ast.decl)), o)
          
        self.emitObjectInit()

        mainEmit = self.emit
        for item in self.list_structType + self.list_interfaceType:
            self.emit = Emitter(self.myPath + "/" + item.name + ".j")
            self.visit(item, {
                'symbolTable': o['symbolTable']
            })

        self.emit = mainEmit

        # visit MAIN function
        self.emitObjectCInit(ast, o)
        o = self.visit(self.lookup("main", list(filter(lambda x: isinstance(x, FuncDecl), ast.decl)), lambda x: x.name), o)

        self.emit.printout(self.emit.emitEPILOG())
        return o





################################################################################################
#-----------     BLOCK DEFINITION      ---------------------------------------------------------
    def visitBlock(self, ast: Block, o):
        self.list_body_element_in_block = ast.member
        newO = self.createNewEnvironment(o, symbolTable=[[]] + o['symbolTable']) 
        
        for stmt in ast.member:
            if isinstance(stmt, (FuncCall, MethCall)):
                newO = self.visit(stmt, self.createNewEnvironment(newO, isStmt=True))
            else:
                newO = self.visit(stmt, newO)
        return o





################################################################################################
#-----------     EXPRESSION DEFINITION      ----------------------------------------------------
    # Literal ------------------------
    def visitId(self, ast: Id, o):
        """ Ghi giá trị """
        def process_when_var_isLeft():
            code = self.code_type_convert(id_symbol.mtype, o.get('rhsType'), frame)
            if isinstance(id_symbol.value, CName):
                code += self.emit.emitPUTSTATIC(f"{id_symbol.value.value}/{id_symbol.name}", id_symbol.mtype, frame)
            else:
                code += self.emit.emitWRITEVAR(id_symbol.name, id_symbol.mtype, id_symbol.value.value, frame)
            return code

        """ Đọc giá trị """
        def process_when_var_isRight():
            if isinstance(id_symbol.value, CName):
                code = self.emit.emitGETSTATIC(f"{id_symbol.value.value}/{id_symbol.name}", id_symbol.mtype, frame)
            else:
                code = self.emit.emitREADVAR(id_symbol.name, id_symbol.mtype, id_symbol.value.value, frame)
            return code
        
        """'"""""""""""""""""""""""""""""""""
        frame = o['frame']
        id_symbol = self.lookup(ast.name, [sym for env in o['symbolTable'] for sym in env], lambda x: x.name)
        
        # Nếu id_symbol không tìm thấy (trả về None) 
        if not id_symbol:
            # Không tìm thấy Id + Id được truy cập từ FieldAcess => Đây là biến THIS trong METHOD
            if o.get('fieldAccessFlag', False):
                code = self.emit.emitREADVAR("this", ClassType(self.current_struct.name), 0, frame)
                return code, ClassType(self.current_struct.name)
            # Không tìm thấy Id + Id được truy cập từ những Expr khác --> Đây chính là vế trái của Assign (cần tự khai báo biến b)
            else:
                idx = frame.getNewIndex()
                self.emit.printout(self.emit.emitVAR(idx, ast.name, o['rhsType'], frame.getStartLabel(), frame.getEndLabel(), frame))
                id_symbol = Symbol(ast.name, o['rhsType'], Index(idx))
                o['symbolTable'][0] += [id_symbol]

        if isinstance(id_symbol.mtype, Id):
            id_symbol.mtype = self.lookup(id_symbol.mtype.name, self.list_structType + self.list_interfaceType, lambda x: x.name)
            
        if (o['isLeft']): # Write
            code = process_when_var_isLeft()
        else:
            code = process_when_var_isRight()
        return code, id_symbol.mtype
  
    def visitIntLiteral(self, ast: IntLiteral, o):
        code = self.emit.emitPUSHICONST(ast.value, o['frame'])
        return code, IntType()
    
    def visitFloatLiteral(self, ast: FloatLiteral, o):
        code = self.emit.emitPUSHFCONST(ast.value, o['frame'])
        return code, FloatType()
    
    def visitBooleanLiteral(self, ast: BooleanLiteral, o):
        code = self.emit.emitPUSHCONST(str(ast.value), BoolType(), o['frame'])
        return code, BoolType()
    
    def visitStringLiteral(self, ast: StringLiteral, o):
        code = self.emit.emitPUSHCONST(ast.value, StringType(), o['frame'])
        return code, StringType()

    def visitArrayLiteral(self, ast: ArrayLiteral, o):
        frame = o['frame']
        code = ""

        # Mảng 1 chiều
        if len(ast.dimens) == 1:
            # 1. Đẩy lên Stack -> Số chiều
            exprCode, _ = self.visit(ast.dimens[0], o)
            code += exprCode
            # 2. Tạo array mới với lệnh newarray (có số chiều đã khai báo)
            if isinstance(ast.eleType, (StringType, Id)):
                code += self.emit.emitANEWARRAY(ast.eleType, frame)
            else:
                code += self.emit.emitNEWARRAY(ast.eleType, frame)
            # 3. Thêm vào các giá trị
            for i in range(len(ast.value)):
                # arrayRef
                code += self.emit.emitDUP(frame)
                # index
                code += self.emit.emitPUSHICONST(i, frame)
                # value
                valueCode, valueType = self.visit(ast.value[i], o)
                code += valueCode + self.code_type_convert(ast.eleType, valueType, frame)
                # iastore
                code += self.emit.emitASTORE(ast.eleType, frame)
        # Mảng n chiều
        else:
            # 1. Đẩy lên Stack -> Số chiều n1
            exprCode, _ = self.visit(ast.dimens[0], o)
            code += exprCode
            # 2. Tạo array n1 chiều với lệnh anewarray
            code += self.emit.emitANEWARRAY(ArrayType(ast.dimens[1:], ast.eleType if not isinstance(ast.eleType, Id) else self.lookup(ast.eleType.name, self.list_structType + self.list_interfaceType, lambda x: x.name)), frame)
            # 3. Thêm nội dung của các chiều vào array (thêm các mảng khác vào array)
            for i in range(len(ast.value)):
                # arrayRef
                code += self.emit.emitDUP(frame)
                # index
                code += self.emit.emitPUSHICONST(i, frame)
                # value --> đệ quy cho các cấp mảng con
                tmpCode, _ = self.visit(ArrayLiteral(ast.dimens[1:], ast.eleType, ast.value[i]), o)
                code += tmpCode
                # aastore
                code += self.emit.emitASTORE(ArrayType(ast.dimens[1:], ast.eleType), frame)

        return code, ArrayType(ast.dimens, ast.eleType)

    def visitStructLiteral(self, ast: StructLiteral, o):
        frame = o['frame']
        code = ""

        # new StructType
        code += self.emit.emitNEW(ast.name, frame)
        code += self.emit.emitDUP(frame)

        # Đánh giá tất cả các biểu thức
        arg_types = []
        for field_name, expr in ast.elements:
            ecode, etype = self.visit(expr, o)
            code += ecode
            arg_types.append(etype)

        # Gọi constructor có tham số
        code += self.emit.emitINVOKESPECIAL_CONSTRUCTOR(ast.name, arg_types, frame)

        return code, ClassType(ast.name)

    def visitNilLiteral(self, ast: NilLiteral, o):
        code = self.emit.emitPUSHCONST("null", NilLiteral(), o['frame'])
        return code, NilLiteral()
    
    # Arraycell Access ----------------------
    def process_arrayCell(self, ast: ArrayCell, o, arrCode, arrType):
        def baseCase_when_isLeft():
            rhsCode, rhsType = self.visit(o.get('rhsAST'), self.createNewEnvironment(o, isLeft=False))
            code = rhsCode + self.code_type_convert(retType, rhsType, frame)
            code += self.emit.emitASTORE(retType, frame)
            return code

        def baseCase_when_isRight():
            return self.emit.emitALOAD(retType, frame)

        def recursive(myIndexList):
            code = ""
            if len(myIndexList) == 1:
                if o.get('isLeft'):
                    code += baseCase_when_isLeft()
                else:
                    code += baseCase_when_isRight()
            else:
                code += self.emit.emitALOAD(ArrayType(None, None), frame)  # tải mảng cấp dưới
                tmpCode, _ = self.visit(myIndexList[1], o)
                code += tmpCode
                code += recursive(myIndexList[1:])
            return code

        frame = o['frame']

        if len(ast.idx) < len(arrType.dimens):
            retType = ArrayType(arrType.dimens[len(ast.idx):], arrType.eleType)
        else:
            retType = arrType.eleType

        # Bắt đầu từ phần arrCode đã xử lý
        tmpCode, _ = self.visit(ast.idx[0], self.createNewEnvironment(o, isLeft=False))
        code = arrCode + tmpCode
        code += recursive(ast.idx)
        return code, retType
    
    def visitArrayCell(self, ast: ArrayCell, o):
        arrCode, arrType = self.visit(ast.arr, self.createNewEnvironment(o, isLeft=False))  # code + loại mảng
        return self.process_arrayCell(ast, o, arrCode, arrType)

    # Field Access ------------------------
    def visitFieldAccess(self, ast: FieldAccess, o):
        def find_fieldType(structType):
            # Tìm AST của Struct có tên là structType.name
            structAST = self.lookup(structType.name, self.list_structType, lambda x: x.name)
            # Tìm trong AST => fieldType
            for fieldName, fieldType in structAST.elements:
                if fieldName == ast.field:
                    return fieldType

        code = ""
        frame = o['frame']
        # objectRef
        objCode, objType = self.visit(ast.receiver, self.createNewEnvironment(o, fieldAccessFlag=True, isLeft=False))
        code += objCode
        # type
        fieldType = find_fieldType(objType)
        fieldType = fieldType if not isinstance(fieldType, Id) else self.lookup(fieldType.name, self.list_structType + self.list_interfaceType, lambda x: x.name)

        if o.get('isLeft', False):
            # Nếu là vế trái của phép gán
            tmpCode, _ = self.visit(o.get('rhsAST'), self.createNewEnvironment(o, isLeft=False))
            code += tmpCode
            code += self.code_type_convert(fieldType, o.get('rhsType'), frame)
            
            code += self.emit.emitPUTFIELD(f"{objType.name}/{ast.field}", fieldType, frame)
        else:
            # Nếu là vế phải của phép gán
            code += self.emit.emitGETFIELD(f"{objType.name}/{ast.field}", fieldType, frame)
        return code, fieldType
        
                


    # Binary-Unary Expression ------------------------
    def visitBinaryOp(self, ast: BinaryOp, o):
        frame = o['frame']

        leftCode, leftType = self.visit(ast.left, o)
        rightCode, rightType = self.visit(ast.right, o)
        operandsType = leftType

        if type(leftType) is type(rightType):
            if isinstance(ast.left, IntType) and ast.op == "/":
                leftCode += self.emit.emitI2F(frame)
                rightCode += self.emit.emitI2F(frame)
                operandsType = FloatType()
        else:
            if isinstance(leftType, IntType) and isinstance(rightType, FloatType):
                leftCode += self.emit.emitI2F(frame)
                operandsType = FloatType()
            elif isinstance(leftType, FloatType) and isinstance(rightType, IntType):
                rightCode +=  self.emit.emitI2F(frame)
                operandsType = FloatType()

        if isinstance(operandsType, (IntType, FloatType, BoolType)):
            if ast.op in ["+", "-"]:
                opCode = self.emit.emitADDOP(ast.op, operandsType, frame)
                retType = operandsType
       
            elif ast.op in ["*", "/"]:
                opCode = self.emit.emitMULOP(ast.op, operandsType, frame)
                retType = operandsType
                
            elif ast.op in ["%"]:
                opCode = self.emit.emitMOD(frame)
                retType = operandsType
                
            elif ast.op in ["==", "!=", "<", ">", "<=", ">="]:
                opCode = self.emit.emitREOP(ast.op, operandsType, frame)
                retType = BoolType()
                
            elif ast.op in ["&&"]:
                opCode = self.emit.emitANDOP(frame)
                retType = BoolType()
                
            elif ast.op in ["||"]:
                opCode = self.emit.emitOROP(frame)
                retType = BoolType()
   
        elif isinstance(operandsType, StringType):
            # Hàm được xử lý đặc biệt, nếu không chuẩn sẽ dẫn đến Stack size is too large
            if ast.op in ["+"]:
                entireCode = self.emit.emitSTRINGCONCATINATION(frame, leftCode, rightCode)
                retType = StringType()
                return entireCode, retType
                
            elif ast.op in ["==", "!=", "<", ">", "<=", ">="]:
                opCode = self.emit.emitSTRINGCOMPARATION(ast.op, frame)
                retType = BoolType()

        code = leftCode + rightCode + opCode
        return code, retType
              
    def visitUnaryOp(self, ast: UnaryOp, o):
        frame = o['frame']
        expCode, expType = self.visit(ast.body, o)
        
        if ast.op == "-":
            opCode = self.emit.emitNEGOP(expType, frame)
        elif ast.op == "!":
            opCode = self.emit.emitNOT(expType, frame)
        
        return expCode + opCode, expType

  

    # Call Expression
    def visitMethCall(self, ast: MethCall, o):
        frame = o['frame']
        code = ""

        # 1. Tạo mã cho receiver
        recv_code, recv_type = self.visit(ast.receiver, self.createNewEnvironment(o, isLeft=False))
        code += recv_code

        # 2. Resolve kiểu thực sự (nếu chỉ là Id)
        recv_type = self.lookup(recv_type.name, self.list_structType + self.list_interfaceType, lambda x: x.name)   

        # 3. Kiểm tra statement hay expression
        is_stmt = o.pop("isStmt", False)

        # 4. Đánh giá các đối số
        arg_codes = []
        arg_types = []
        for arg in ast.args:
            acode, atype = self.visit(arg, o)
            arg_codes.append(acode)
            arg_types.append(atype)
            code += acode

        return_type = None

        # 5. Gọi phương thức trên StructType
        if isinstance(recv_type, StructType):
            method = next((m for m in self.find_methods_of_struct(recv_type.name) 
                        if m.fun.name == ast.metName), False)

            param_types = [p.parType for p in method.fun.params]
            mtype = MType(param_types, method.fun.retType if not isinstance(method.fun.retType, Id) else self.lookup(method.fun.retType.name, self.list_structType + self.list_interfaceType, lambda x: x.name))
            return_type = method.fun.retType
            code += self.emit.emitINVOKEVIRTUAL(f"{recv_type.name}/{ast.metName}", mtype, frame)

        # 6. Gọi phương thức trên InterfaceType
        elif isinstance(recv_type, InterfaceType):
            method = next((m for m in recv_type.methods if m.name == ast.metName), False)
            param_types = method.params
            mtype = MType(param_types, method.retType)
            return_type = method.retType
            code += self.emit.emitINVOKEINTERFACE(f"{recv_type.name}/{ast.metName}", mtype, frame)

        # 7. Nếu là statement
        if is_stmt:
            self.emit.printout(code)
            return o

        # 8. Nếu là expression
        return code, return_type



################################################################################################
#-----------     STATEMENT DEFINITION      -----------------------------------------------------
    # Function Call ------------------------
    def visitFuncCall(self, ast: FuncCall, o):
        frame = o['frame']
        
        symbol = self.lookup(ast.funName, self.list_symbol_function, lambda x: x.name)

        for arg in ast.args:
            # Nếu FunCall là Stmt thì cần truyền newO (do visit expr) - ngược lại chỉ cần tryền o
            if o.get('isStmt', False):
                newO = self.createNewEnvironment(o, isLeft=False)
                newO.pop('isStmt')
            else:
                newO = self.createNewEnvironment(o)
            code, _ = self.visit(arg, newO)
            self.emit.printout(code)

        code = self.emit.emitINVOKESTATIC(f"{symbol.value.value}/{symbol.name}", symbol.mtype, frame)
        if o.get('isStmt', False):
            self.emit.printout(code)
            return o
        else:
            return code, symbol.mtype.rettype



    # Variable declare ------------------------
    """ Chuyển đổi Dimension về dạng chuẩn (phần tử nguyên tử chỉ bao gồm Interal) """
    def calculate_dimension_element(self, dimen):
        if isinstance(dimen, IntLiteral):
            return dimen
        elif isinstance(dimen, ArrayLiteral):
            return dimen
        elif isinstance(dimen, Id):
            constDecl_AST = self.lookup(dimen.name, list(filter(lambda x: isinstance(x, ConstDecl), self.ast.decl + self.list_body_element_in_block)), lambda x: x.conName)
            return self.calculate_dimension_element(constDecl_AST.iniExpr)
        elif isinstance(dimen, ArrayCell):
            # Lấy mảng gốc
            array = self.calculate_dimension_element(dimen.arr)
            # Lặp qua từng chiều chỉ số
            current = array
            for idx_expr in dimen.idx:
                idx_val_expr = self.calculate_dimension_element(idx_expr)
                idx_val = idx_val_expr.value
                if isinstance(current, ArrayLiteral):
                    current = current.value
                current = current[idx_val]
            # Kết quả cuối cùng
            return current
        elif isinstance(dimen, BinaryOp):
            leftExpr = self.calculate_dimension_element(dimen.left)
            rightExpr = self.calculate_dimension_element(dimen.right)
            if dimen.op == "+":
                return IntLiteral(int(leftExpr.value + rightExpr.value))
            elif dimen.op == "-":
                return IntLiteral(int(leftExpr.value - rightExpr.value))
            elif dimen.op == "*":
                return IntLiteral(int(leftExpr.value * rightExpr.value))

    """ Tạo nestedList trong ArrayLiteral (Mặc định chỉ có IntLiteral, không còn Id...) """
    def create_nested_list(self, varType: ArrayType, recursiveArray):
        if len(recursiveArray) == 1:
            default_value = self.get_default_value(varType.eleType)
            return [default_value for _ in range(recursiveArray[0].value)]
        else:
            return [self.create_nested_list(varType, recursiveArray[1:]) for i in range(recursiveArray[0].value)]

    """ Khởi tạo giá trị mặc định """
    def get_default_value(self, varType: Type):
        if isinstance(varType, IntType):
            return IntLiteral(0)
        elif isinstance(varType, FloatType):
            return FloatLiteral(0.0)
        elif isinstance(varType, BoolType):
            return BooleanLiteral('false')
        elif isinstance(varType, StringType):
            # return NilLiteral()
            return StringLiteral('""')
        elif isinstance(varType, ArrayType):
            nestedList = self.create_nested_list(varType, reduce(lambda x, y: x + [self.calculate_dimension_element(y)], varType.dimens, []))
            return ArrayLiteral(varType.dimens, varType.eleType, nestedList)
        elif isinstance(varType, Id):
            # Nếu là StructType
            if self.lookup(varType.name, self.list_structType, lambda x: x.name):
                return StructLiteral(varType.name, [])
            # Nếu là InterfaceType
            elif self.lookup(varType.name, self.list_interfaceType, lambda x: x.name):
                return NilLiteral()
        
    def visitVarDecl(self, ast: VarDecl, o): 
        """ Xử lý Type của Init trước khi visit """
        def process_type_varInit():
            if isinstance(ast.varType, ArrayType) and isinstance(ast.varInit, ArrayLiteral) and isinstance(ast.varType.eleType, FloatType) and isinstance(ast.varInit.eleType, IntType):
                ast.varInit.eleType = FloatType()
            elif isinstance(ast.varInit, FuncCall):
                newO['isStmt'] = False
            elif isinstance(ast.varType, FloatType) and isinstance(ast.varInit, IntLiteral):
                ast.varInit = FloatLiteral(float(ast.varInit.value))
                
        """ Xử lý khai báo biến TOÀN CỤC """
        def process_global_varDecl():
            var_symbol = self.lookup(ast.varName, [sym for env in o["symbolTable"] for sym in env], lambda x: x.name)
            self.emit.printout(self.emit.emitPUTSTATIC(f"{var_symbol.value.value}/{var_symbol.name}", var_symbol.mtype, frame))

        """ Xử lý khai báo biến CỤC BỘ """
        def process_local_varDecl():
            idx = frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx, ast.varName, ast.varType, frame.getStartLabel(), frame.getEndLabel(), frame))
            self.emit.printout(self.emit.emitWRITEVAR(ast.varName, ast.varType, idx, frame))
            o['symbolTable'][0] += [Symbol(ast.varName, ast.varType, Index(idx))]   

        """'"""""""""""""""""""""""""""""""""
        # Tiền khai báo
        is_global_variable_declare = o.get("frame", False).name == "<cinit>"
        newO = self.createNewEnvironment(o, isLeft=False)
        frame = newO['frame']

        # 1. Xử lý giá trị trước khi đẩy lên Stack
        if not ast.varInit:
            # Nếu chưa có Init --> tự khai báo giá trị mặc định
            ast.varInit = self.get_default_value(ast.varType)
        else:
            # Đã có Init --> Xử lý Type của varInit trước khi visit
            process_type_varInit()
            
        # 2. Visit varInit => Đẩy giá trị lên Stack
        initCode, initType = self.visit(ast.varInit, newO)
        self.emit.printout(initCode)

        # Nếu chưa khai báo Type => khai báo Type theo Type của varInit
        if not ast.varType:
            ast.varType = initType
            
        if isinstance(ast.varType, (Id, ClassType)):
            ast.varType = self.lookup(ast.varType.name, self.list_structType + self.list_interfaceType, lambda x: x.name)
        elif isinstance(ast.varType, ArrayType) and isinstance(ast.varType.eleType, Id):
                ast.varType.eleType = self.lookup(ast.varType.eleType.name, self.list_structType + self.list_interfaceType, lambda x: x.name)
        
        # 3. Logic chính xử lý LƯU GIÁ TRỊ trên stack vào biến
        if is_global_variable_declare:
            process_global_varDecl()
        else:
            process_local_varDecl() 
        return o

    def visitVarDecl_Special(self, ast: VarDecl, o):
        # Nếu chưa có Init --> tự khai báo giá trị mặc định
        if not ast.varInit:
            ast.varInit = self.get_default_value(ast.varType)
        if not ast.varType:
            newO = self.createNewEnvironment(o, frame=Frame("tmpFrame", VoidType()), isLeft=False)
            newO["frame"].enterScope(False)
            _, typ = self.visit(ast.varInit, newO)
            newO["frame"].exitScope()
            ast.varType = typ
        self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, ast.varType, True, False, None))
        o["symbolTable"][-1] += [Symbol(ast.varName, ast.varType, CName(self.className, True))]
        return o

    # Constant Declare ------------------------
    def visitConstDecl(self, ast: ConstDecl, o):
        return self.visit(VarDecl(ast.conName, ast.conType, ast.iniExpr), o)


    # Parameter declare ------------------------
    def visitParamDecl(self, ast: ParamDecl, o):
        frame = o['frame']
        idx = frame.getNewIndex()
        ast.parType = ast.parType if not isinstance(ast.parType, Id) else self.lookup(ast.parType.name, self.list_structType + self.list_interfaceType, lambda x: x.name)
        self.emit.printout(self.emit.emitVAR(idx, ast.parName, ast.parType, frame.getStartLabel(), frame.getEndLabel(), frame))

        o['symbolTable'][0] += [Symbol(ast.parName, ast.parType, Index(idx))]
        return o


    # Function declare ------------------------
    def visitFuncDecl(self, ast: FuncDecl, o):
        frame = Frame(ast.name, ast.retType)

        isMain = ast.name == "main" and len(ast.params) == 0 and isinstance(ast.retType, VoidType)
        if isMain:
            function_type = MType([ArrayType([], StringType())], VoidType())
        else:
            function_type = MType(list(map(lambda x: x.parType if not isinstance(x.parType, Id) else self.lookup(x.parType.name, self.list_structType + self.list_interfaceType, lambda y: y.name), ast.params)), ast.retType if not isinstance(ast.retType, Id) else self.lookup(ast.retType.name, self.list_structType + self.list_interfaceType, lambda y: y.name))
        self.emit.printout(self.emit.emitMETHOD(ast.name, function_type, True, frame))

        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        
        newO = self.createNewEnvironment(o, symbolTable=[[]] + o['symbolTable'], frame=frame)

        if isMain:
            idx = frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx, "args", ArrayType([], StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            newO = reduce(lambda x, y: self.visit(y, x), ast.params, newO)

        # Thân hàm
        newO = self.visit(ast.body, newO)
        
        # Return hàm
        if isinstance(ast.retType, VoidType):
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        return o

    def visitFuncDecl_instanceMethod(self, ast: FuncDecl, o):
        frame = o['frame']
        # Param
        newO = self.createNewEnvironment(o, symbolTable=[[]] + o['symbolTable'], frame=frame)
        newO = reduce(lambda x, y: self.visit(y, x), ast.params, newO)
        # Thân hàm
        newO = self.visit(ast.body, newO)
        # Return hàm
        if isinstance(ast.retType, VoidType):
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        return o


    # Method declare ------------------------
    def visitMethodDecl(self, ast: MethodDecl, o):
        self.current_struct = self.lookup(ast.recType.name, self.list_structType, lambda x: x.name)
        
        newO = self.createNewEnvironment(o, frame=Frame("tmpFrame", VoidType()))
        frame = newO['frame']

        function_type = MType(list(map(lambda x: x.parType if not isinstance(x.parType, Id) else self.lookup(x.parType.name, self.list_structType + self.list_interfaceType, lambda y: y.name), ast.fun.params)), ast.fun.retType if not isinstance(ast.fun.retType, Id) else self.lookup(ast.fun.retType.name, self.list_structType + self.list_interfaceType, lambda y: y.name))
        self.emit.printout(self.emit.emitMETHOD(ast.fun.name, function_type, False, frame))
        frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        
        # Khởi tạo biến this (cho METHOD)=> getIndex đầu tiên nên sẽ có idx = 0 (sau này muốn READVAR thì không cần tìm mà load thẳng idx = 0)
        idx = frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(idx, "this", ClassType(ast.recType.name), frame.getStartLabel(), frame.getEndLabel(), frame))

        # Visit FUNCTION
        newO = self.visitFuncDecl_instanceMethod(ast.fun, newO)

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        
        return o
    


    # Assignment Statement ------------------------
    def visitAssign(self, ast: Assign, o):
        newO = self.createNewEnvironment(o, isLeft=False)
       
        # visitRHS
        if isinstance(ast.lhs, (ArrayCell, FieldAccess)):
            newO['rhsAST'] = ast.rhs
        else:
            if isinstance(ast.rhs, FuncCall):
                newO['isStmt'] = False
            rhsCode, rhsType = self.visit(ast.rhs, newO)
            newO['rhsType'] = rhsType
            
        # visitLHS
        newO['isLeft'] = True
        lhsCode, _ = self.visit(ast.lhs, newO)

        self.emit.printout(("" if isinstance(ast.lhs, (ArrayCell, FieldAccess)) else rhsCode) + lhsCode)
        return o



    # If Statement declare --------------------
    def visitIf(self, ast: If, o):  
        newO = self.createNewEnvironment(o, symbolTable=[[]] + o['symbolTable'])
        frame = newO['frame']
        fLabel = frame.getNewLabel()

        # expr
        code, _ = self.visit(ast.expr, self.createNewEnvironment(newO, isLeft=False))
        self.emit.printout(code)
        # Nhảy tới fLabel nếu đỉnh Stack False
        self.emit.printout(self.emit.emitIFFALSE(fLabel, frame))
        # thenStmt
        self.visit(ast.thenStmt, newO)
    
        if not ast.elseStmt:
            # Đặt fLabel tại đây
            self.emit.printout(self.emit.emitLABEL(fLabel, frame))
        else:
            tLabel = frame.getNewLabel()
            # Nhảy tới tLabel trong mọi trường hợp
            self.emit.printout(self.emit.emitGOTO(tLabel, frame))
            # Đặt fLabel tại đây
            self.emit.printout(self.emit.emitLABEL(fLabel, frame))
            # elseStmt
            self.visit(ast.elseStmt, newO)
            # Đặt tLabel tại đây
            self.emit.printout(self.emit.emitLABEL(tLabel, frame))
        return o


    # For-Basic -------------------------------
    def visitForBasic(self, ast: ForBasic, o):
        newO = self.createNewEnvironment(o, symbolTable=[[]] + o['symbolTable'])
        frame = newO['frame']
        frame.enterLoop()
        
        continueLabel = frame.getContinueLabel()
        breakLabel = frame.getBreakLabel()

        # Đặt continueLabel tại đây
        self.emit.printout(self.emit.emitLABEL(continueLabel, frame))
        # cond
        code, _ = self.visit(ast.cond, self.createNewEnvironment(newO, isLeft=False))
        self.emit.printout(code)
        # Nhảy đến breakLabel nếu đỉnh Stack là False
        self.emit.printout(self.emit.emitIFFALSE(breakLabel, frame))
        # Block
        self.visit(ast.loop, newO)
        # Nhảy đến continueLabel trong mọi trường hợp
        self.emit.printout(self.emit.emitGOTO(continueLabel, frame))
        # Đặt breakLabel tại đây
        self.emit.printout(self.emit.emitLABEL(breakLabel, frame))
        
        frame.exitLoop()
        return o

    # For-Step-----------------------------------
    def visitForStep(self, ast: ForStep, o):
        newO = self.createNewEnvironment(o, symbolTable=[[]] + o['symbolTable'])
        frame = newO['frame']
        frame.enterLoop()

        breakLabel = frame.getBreakLabel()
        continueLabel = frame.getContinueLabel()
        conditionLabel = frame.getNewLabel()

        # Init (Dạng 1 AssignStatement hoặc VarDeclaration with init)
        newO = self.visit(ast.init, newO)
        # Đặt conditionLabel tại đây
        self.emit.printout(self.emit.emitLABEL(conditionLabel, frame))
        # Cond
        code, _ = self.visit(ast.cond, self.createNewEnvironment(newO, isLeft=False))
        self.emit.printout(code)
        # Nhảy đến breakLabel nếu đỉnh Stack là False
        self.emit.printout(self.emit.emitIFFALSE(breakLabel, frame))
        # Loop
        newO = self.visit(ast.loop, newO)
        # Đặt continueLabel tại đây
        self.emit.printout(self.emit.emitLABEL(continueLabel, frame))
        # Upda
        newO = self.visit(ast.upda, newO)
        # Nhảy đến conditionLabel trong mọi trường hợp
        self.emit.printout(self.emit.emitGOTO(conditionLabel, frame))
        # Đặt breakLabel tại đây
        self.emit.printout(self.emit.emitLABEL(breakLabel, frame))
        
        frame.exitLoop()
        return o

    # For-Each ----------------------------------
    def visitForEach(self, ast, o):
        # thẩy bỏ qua (đặt thầy thầy có nói)
        return o


        
    # Return Statement ------------------------
    def visitReturn(self, ast: Return, o):
        frame = o['frame']
        if ast.expr:
            newO = self.createNewEnvironment(o, isLeft=False)
            code, typ = self.visit(ast.expr, newO)
            self.emit.printout(code)
            self.emit.printout(self.emit.emitRETURN(typ, frame))
        else:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        return o

    # Continue -----------------------------------
    def visitContinue(self, ast, o):  
        self.emit.printout(self.emit.emitGOTO(o['frame'].getContinueLabel(), o['frame']))
        return o

    # Break --------------------------------------
    def visitBreak(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o['frame'].getBreakLabel(), o['frame']))
        return o





################################################################################################
#-----------     STATEMENT DEFINITION      -----------------------------------------------------
    # Struct Type  ------------------------
    """ Hàm tìm Tên của Interface có prototype tên funcName """
    def find_interface_name (self, funcName):
        for interfaceAST in self.list_interfaceType:
            exist = self.lookup(funcName, interfaceAST.methods, lambda x: x.name)
            if exist:
                return interfaceAST.name
        return None

    """ Hàm tìm danh sách tất cả Methods của 1 Struct """
    def find_methods_of_struct(self, structName):
        return list(filter(lambda x: isinstance(x, MethodDecl) and x.recType.name == structName, self.ast.decl))
    
    def visitStructType(self, ast: StructType, o):
        self.emit.printout(self.emit.emitPROLOG(ast.name, "java/lang/Object"))
        newO = self.createNewEnvironment(o)

        # Tiền xử lý -> printout tất cả các dòng implements (KHÔNG TRÙNG LẶP)
        listMethods = self.find_methods_of_struct(ast.name)
        interfaces = set()

        for methodAST in listMethods:
            interfaceName = self.find_interface_name(methodAST.fun.name)
            if interfaceName:
                interfaces.add(interfaceName)

        for interface in interfaces:
            self.emit.printout(self.emit.emitIMPLEMENTS(interface))

        # 1. Xử lý các Fields
        for field_name, field_type in ast.elements:
            field_type = field_type if not isinstance(field_type, Id) else self.lookup(field_type.name, self.list_structType + self.list_interfaceType, lambda x: x.name)
            self.emit.printout(self.emit.emitATTRIBUTE(f"public {field_name}", field_type, False, False, None))

        # Hàm khởi tạo KHÔNG THAM SỐ cho class => Khởi tạo this + khởi tạo giá trị mặc định cho fields
        self.emitObjectInit(ast.name, ast.elements)

        # Hàm khởi tạo CÓ THAM SỐ
        self.emitParameterizedConstructor(ast.name, ast.elements)
        
        # 2. Xử lý các Methods
        for method in ast.methods + listMethods:
            newO = self.visit(method, newO)

        self.emit.printout(self.emit.emitEPILOG())
        return o

    # Prototype  ------------------------
    def visitPrototype(self, ast: Prototype, o):
        self.emit.printout(self.emit.emitMETHOD(ast.name, MType(ast.params, ast.retType), False, o['frame'], True))
        self.emit.printout(self.emit.emitENDMETHOD(o['frame'], True))
        return o

    # Interface Type  ------------------------
    def visitInterfaceType(self, ast: InterfaceType, o):
        self.emit.printout(self.emit.emitPROLOG_INTERFACE(ast.name, ""))
        frame = Frame(f"{ast.name}Interface", VoidType())  
        frame.enterScope(True)  

        self.visit(Block(list(map(lambda x: x, ast.methods))), self.createNewEnvironment(o, frame=frame))

        frame.exitScope()
        self.emit.printout(self.emit.emitEPILOG())
        return o