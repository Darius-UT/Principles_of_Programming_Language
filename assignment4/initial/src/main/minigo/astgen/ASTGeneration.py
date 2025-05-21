


from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from antlr4 import *
from AST import *


def processing_if(list_else_if_statement, else_statement: Block):
    if not list_else_if_statement:
        return else_statement
    
    head, *tail = list_else_if_statement
    exp, block = head
    
    return If(exp, block, processing_if(tail, else_statement))


class ASTGeneration(MiniGoVisitor): # type: ignore
    
#  Program definition --------------------------------------------------------------------------
    # program:  declared_statement_list EOF;
    def visitProgram(self, ctx: MiniGoParser.ProgramContext):
        return Program(self.visit(ctx.declared_statement_list()))

    # declared_statement_list: (declared_statement) (declared_statement_list) | (declared_statement);
    def visitDeclared_statement_list(self, ctx:MiniGoParser.Declared_statement_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.declared_statement())]
        else:
            return [self.visit(ctx.declared_statement())] + self.visit(ctx.declared_statement_list())




#  Literal 6.6 pdf --------------------------------------------------------------------------
    # literal:
	# literal_primitive
	# | array_lit_instance
	# | struct_lit_instance;
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visit(ctx.getChild(0))


    # literal_primitive: 
    # INTEGER_LIT
	# | FLOAT_LIT
	# | STRING_LIT
    # | TRUE
    # | FALSE
    # | NIL;
    def visitLiteral_primitive(self, ctx:MiniGoParser.Literal_primitiveContext):
        if ctx.INTEGER_LIT():
            value = int(ctx.INTEGER_LIT().getText(), 0)
            # value = ctx.INTEGER_LIT().getText()
            return IntLiteral(value)
        elif ctx.FLOAT_LIT():
            value = float(ctx.FLOAT_LIT().getText())
            # value = ctx.FLOAT_LIT().getText()
            return FloatLiteral(value)
        elif ctx.STRING_LIT():
            value = ctx.STRING_LIT().getText()
            return StringLiteral(value)
        elif ctx.TRUE() or ctx.FALSE():
            value = (ctx.getChild(0).getText() == 'true')
            return BooleanLiteral(value)
        elif ctx.NIL():
            return NilLiteral()


    # mytype: ID | primitive_type | array_type;
    def visitMytype(self, ctx:MiniGoParser.MytypeContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.getChild(0))


    # primitive_type  : INT | FLOAT | BOOLEAN | STRING;
    def visitPrimitive_type(self, ctx:MiniGoParser.Primitive_typeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        else:
            return StringType()


    # array_type      : (array_dimention) (ID | primitive_type);
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        myDimensionList = self.visit(ctx.array_dimention())
        myType = Id(ctx.ID().getText()) if ctx.ID() else self.visit(ctx.primitive_type())
        return ArrayType(myDimensionList, myType)


    # array_dimention : (array_dimention_element) (array_dimention) | array_dimention_element;
    def visitArray_dimention(self, ctx:MiniGoParser.Array_dimentionContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.array_dimention_element())]
        else:
            return [self.visit(ctx.array_dimention_element())] + self.visit(ctx.array_dimention())


    # array_dimention_element: LBRACK (INTEGER_LIT | ID) RBRACK;
    def visitArray_dimention_element(self, ctx:MiniGoParser.Array_dimention_elementContext):
        if ctx.INTEGER_LIT():
            my_decimal_int = int(ctx.INTEGER_LIT().getText(), 0)
            return IntLiteral(my_decimal_int)
        else:
            return Id(ctx.ID().getText())


    # array_lit_instance: array_type LBRACE list_array_value RBRACE; 
    def visitArray_lit_instance(self, ctx:MiniGoParser.Array_lit_instanceContext):
        myDimensionList = self.visit(ctx.array_type().array_dimention())
        if ctx.array_type().ID():
            myType = Id(ctx.array_type().ID().getText())
        else:
            myType = self.visit(ctx.array_type().primitive_type())
        myValue = self.visit(ctx.list_array_value())
        return ArrayLiteral(myDimensionList, myType, myValue)


    # list_array_value: (list_array_value_element) COMMA (list_array_value) | (list_array_value_element);
    def visitList_array_value(self, ctx:MiniGoParser.List_array_valueContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.list_array_value_element())]
        else:
            return [self.visit(ctx.list_array_value_element())] + self.visit(ctx.list_array_value())


    # list_array_value_element: ID 
    #                         | literal_primitive 
    #                         | struct_lit_instance 
    #                         | LBRACE list_array_value RBRACE;
    def visitList_array_value_element(self, ctx:MiniGoParser.List_array_value_elementContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.LBRACE():
            return self.visit(ctx.list_array_value())
        else:
            return self.visit(ctx.getChild(0))
    

    # struct_lit_instance: ID LBRACE struct_lit_instance_body RBRACE;    
    def visitStruct_lit_instance(self, ctx:MiniGoParser.Struct_lit_instanceContext):
        myName = ctx.ID().getText()
        myValue = self.visit(ctx.struct_lit_instance_body())
        return StructLiteral(myName, myValue)


    # struct_lit_instance_body        : struct_lit_instance_body_prime | ;
    def visitStruct_lit_instance_body(self, ctx:MiniGoParser.Struct_lit_instance_bodyContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return self.visit(ctx.struct_lit_instance_body_prime())


    # struct_lit_instance_body_prime  : struct_lit_instance_body_element COMMA struct_lit_instance_body_prime | struct_lit_instance_body_element;
    def visitStruct_lit_instance_body_prime(self, ctx:MiniGoParser.Struct_lit_instance_body_primeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.struct_lit_instance_body_element())]
        else:
            return [self.visit(ctx.struct_lit_instance_body_element())] + self.visit(ctx.struct_lit_instance_body_prime())


    # struct_lit_instance_body_element: ID COLON expression;
    def visitStruct_lit_instance_body_element(self, ctx:MiniGoParser.Struct_lit_instance_body_elementContext):
        return (ctx.ID().getText(), self.visit(ctx.expression()))






# 5.2 Expressions 6 pdf ---------------------------------------------------------------------
    # list_expression: list_expression_prime | ;
    def visitList_expression(self, ctx:MiniGoParser.List_expressionContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return self.visit(ctx.list_expression_prime())


    # list_expression_prime: expression COMMA list_expression_prime | expression;
    def visitList_expression_prime(self, ctx:MiniGoParser.List_expression_primeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expression())]
        else:
            return [self.visit(ctx.expression())] + self.visit(ctx.list_expression_prime())


    # expression : expression OR expression1 | expression1;
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        if ctx.OR():
            op = ctx.OR().getText()
            left = self.visit(ctx.expression())
            right = self.visit(ctx.expression1())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.expression1())


    # expression1 : expression1 AND expression2 | expression2;
    def visitExpression1(self, ctx:MiniGoParser.Expression1Context):
        if ctx.AND():
            op = ctx.AND().getText()
            left = self.visit(ctx.expression1())
            right = self.visit(ctx.expression2())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.expression2())

    # expression2 : expression2 EQUAL         expression3
    #             | expression2 NOT_EQUAL     expression3
    #             | expression2 LESS          expression3
    #             | expression2 LESS_EQUAL    expression3
    #             | expression2 GREATER       expression3
    #             | expression2 GREATER_EQUAL expression3
    #             | expression3;
    def visitExpression2(self, ctx:MiniGoParser.Expression2Context):
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.expression2())
            right = self.visit(ctx.expression3())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.expression3())


    # expression3 : expression3 ADD expression4
    #             | expression3 SUB expression4
    #             | expression4;
    def visitExpression3(self, ctx:MiniGoParser.Expression3Context):
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.expression3())
            right = self.visit(ctx.expression4())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.expression4())


    # expression4 : expression4 MUL expression5
    #             | expression4 DIV expression5
    #             | expression4 MOD expression5
    #             | expression5;
    def visitExpression4(self, ctx:MiniGoParser.Expression4Context):
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.expression4())
            right = self.visit(ctx.expression5())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.expression5())

    # expression5 : NOT expression5
    #             | SUB expression5
    #             | expression6;
    def visitExpression5(self, ctx:MiniGoParser.Expression5Context):
        if ctx.getChildCount() == 2:
            op = ctx.getChild(0).getText()
            body = self.visit(ctx.expression5())
            return UnaryOp(op, body)
        elif ctx.expression6():
            return self.visit(ctx.expression6())
        else:
            return self.visit(ctx.tmp_expression6())


    # expression6 : expression6 (LBRACK expression RBRACK)                    // 6.4 pdf --> Accessing array elements. VD:  a[2][3], b[4] ...
    #             | expression6 DOT ID                                        // 6.5 pdf --> Accessing struct fields. VD:  person.name,  person.age.b ...
    #             | expression6 DOT (function_call)                           // Method call //person.age.b.a()
    #             | function_call                                             // Function call
    #             | ID 
    #             | literal
    #             | expression7;
    def visitExpression6(self, ctx:MiniGoParser.Expression6Context):
        if ctx.LBRACK():
            myArr = self.visit(ctx.expression6())
            myIndex = [self.visit(ctx.expression())]
            if isinstance(myArr, ArrayCell):
                return ArrayCell(myArr.arr, myArr.idx + myIndex)
            else:
                return ArrayCell(myArr, myIndex)
        elif ctx.DOT() and ctx.ID():
            myObj = self.visit(ctx.expression6())
            myFieldName = ctx.ID().getText()
            return FieldAccess(myObj, myFieldName)
        elif ctx.DOT() and ctx.function_call():
            myName = self.visit(ctx.expression6())
            myReceiver = ctx.function_call().ID().getText()
            myParameter = self.visit(ctx.function_call().list_expression())
            return MethCall(myName, myReceiver, myParameter)
        elif ctx.ID() and ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.getChild(0))


    # expression7 : LPAREN expression RPAREN;
    def visitExpression7(self, ctx:MiniGoParser.Expression7Context):
        return self.visit(ctx.expression())



    # function_call: ID LPAREN list_expression RPAREN;
    def visitFunction_call(self, ctx:MiniGoParser.Function_callContext):
        myName = ctx.ID().getText()
        myPara = self.visit(ctx.list_expression())
        return FuncCall(myName, myPara)


    # method_call  : temp_expression6 DOT (function_call);      
    def visitMethod_call(self, ctx:MiniGoParser.Method_callContext):
        myName = self.visit(ctx.temp_expression6())
        myReceiver = ctx.function_call().ID().getText()
        myPara = self.visit(ctx.function_call().list_expression())
        return MethCall(myName, myReceiver, myPara)


    # temp_expression6: temp_expression6 (LBRACK expression RBRACK)                    
    #                 | temp_expression6 DOT ID                                        
    #                 | temp_expression6 DOT function_call
    #                 | function_call
    #                 | ID;
    def visitTemp_expression6(self, ctx:MiniGoParser.Temp_expression6Context):
        if ctx.LBRACK():
            myArr = self.visit(ctx.temp_expression6())
            myIndex = [self.visit(ctx.expression())]
            if isinstance(myArr, ArrayCell):
                return ArrayCell(myArr.arr, myArr.idx + myIndex)
            else:
                return ArrayCell(myArr, myIndex)
        elif ctx.DOT() and ctx.ID():
            myObj = self.visit(ctx.temp_expression6())
            myFieldName = ctx.ID().getText()
            return FieldAccess(myObj, myFieldName)
        elif ctx.DOT() and ctx.function_call():
            myName = self.visit(ctx.temp_expression6())
            myReceiver = ctx.function_call().ID().getText()
            myParameter = self.visit(ctx.function_call().list_expression())
            return MethCall(myName, myReceiver, myParameter)
        elif ctx.ID() and ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.function_call())




    

# Statement 5 and 4 pdf ----------------------------------------------------------------------
    # list_statement: list_statement_prime | ;
    def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return self.visit(ctx.list_statement_prime())

    # list_statement_prime: statement (list_statement_prime) | statement;
    def visitList_statement_prime(self, ctx:MiniGoParser.List_statement_primeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.statement())]
        else:
            return [self.visit(ctx.statement())] + self.visit(ctx.list_statement_prime())


    # statement   
    #     : declared_statement
    #     | assignment_statement
    #     | if_statement
    #     | for_statement
    #     | break_statement
    #     | continue_statement
    #     | call_statement
    #     | return_statement;
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visit(ctx.getChild(0))


    # declared_statement                          
    #     : variables_declared                    
    #     | constants_declared                    
    #     | function_declared
    #     | method_declared
    #     | struct_declared
    #     | interface_declared;
    def visitDeclared_statement(self, ctx:MiniGoParser.Declared_statementContext):
        return self.visit(ctx.getChild(0))

   
    # variables_declared: VAR ID ((mytype ASSIGN expression) | mytype | ASSIGN expression) SEMICOLON;
    def visitVariables_declared(self, ctx:MiniGoParser.Variables_declaredContext):
        myName = ctx.ID().getText()
        myType = self.visit(ctx.mytype()) if ctx.mytype() else None
        myInit = self.visit(ctx.expression()) if ctx.expression() else None
        return VarDecl(myName, myType, myInit)


    # variables_declared_without_semi_for_loop: VAR ID mytype? ASSIGN expression;
    def visitVariables_declared_without_semi_for_loop(self, ctx:MiniGoParser.Variables_declared_without_semi_for_loopContext):
        myName = ctx.ID().getText()
        myType = self.visit(ctx.mytype()) if ctx.mytype() else None
        myInit = self.visit(ctx.expression())
        return VarDecl(myName, myType, myInit)


    # constants_declared: CONST ID ASSIGN expression SEMICOLON;
    def visitConstants_declared(self, ctx:MiniGoParser.Constants_declaredContext):
        myConst = ctx.ID().getText()
        myReturnType = None
        myValue = self.visit(ctx.expression())
        return ConstDecl(myConst, myReturnType, myValue)


    # function_declared: FUNC ID (LPAREN list_function_parameter RPAREN) (mytype)? (function_body_container) SEMICOLON;
    def visitFunction_declared(self, ctx:MiniGoParser.Function_declaredContext):
        myName = ctx.ID().getText()
        myParam = self.visit(ctx.list_function_parameter())
        myReturnType = self.visit(ctx.mytype()) if ctx.mytype() else VoidType()
        myStatementList = Block(self.visit(ctx.function_body_container()))
        return FuncDecl(myName, myParam, myReturnType, myStatementList)


    # list_function_parameter          : list_function_parameter_prime | ;
    def visitList_function_parameter(self, ctx:MiniGoParser.List_function_parameterContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return self.visit(ctx.list_function_parameter_prime())


    # list_function_parameter_prime    : list_function_parameter_element COMMA list_function_parameter_prime | list_function_parameter_element;
    def visitList_function_parameter_prime(self, ctx:MiniGoParser.List_function_parameter_primeContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.list_function_parameter_element())
        else:
            return self.visit(ctx.list_function_parameter_element()) + self.visit(ctx.list_function_parameter_prime())



    # list_function_parameter_element  : ID (COMMA ID)* (mytype);
    def visitList_function_parameter_element(self, ctx:MiniGoParser.List_function_parameter_elementContext):
        myVarList = [ctx.ID(i).getText() for i in range(len(ctx.ID()))]
        myVarType = self.visit(ctx.mytype())
        return [ParamDecl(myVar, myVarType) for myVar in myVarList]
    

    # function_body_container: LBRACE list_statement_prime RBRACE;
    def visitFunction_body_container(self, ctx:MiniGoParser.Function_body_containerContext):
        return self.visit(ctx.list_statement_prime())


    # method_declared: FUNC (receiver_container) ID (LPAREN list_function_parameter RPAREN) (mytype)? (function_body_container) SEMICOLON;
    def visitMethod_declared(self, ctx:MiniGoParser.Method_declaredContext):
        myName = ctx.ID().getText()
        myParam = self.visit(ctx.list_function_parameter())
        myReturnType = self.visit(ctx.mytype()) if ctx.mytype() else VoidType()
        myStatementList = Block(self.visit(ctx.function_body_container()))
        
        myReceiverName = ctx.receiver_container().ID(0).getText()
        myReceiverType = Id(ctx.receiver_container().ID(1).getText())
        myFuncDecl = FuncDecl(myName, myParam, myReturnType, myStatementList)
        return MethodDecl(myReceiverName, myReceiverType, myFuncDecl)


    # receiver_container: LPAREN ID ID RPAREN;
    def visitReceiver_container(self, ctx:MiniGoParser.Receiver_containerContext):
        return Id(ctx.ID(0).getText()) + Id(ctx.ID(1).getText())


    # struct_declared: TYPE ID STRUCT (LBRACE struct_declared_body RBRACE) SEMICOLON;
    def visitStruct_declared(self, ctx:MiniGoParser.Struct_declaredContext):
        myName = ctx.ID().getText()
        myBodyList = self.visit(ctx.struct_declared_body())
        myMethodList = []
        return StructType(myName, myBodyList, myMethodList)


    # struct_declared_body        : (struct_declared_body_element) (struct_declared_body) | (struct_declared_body_element);
    def visitStruct_declared_body(self, ctx:MiniGoParser.Struct_declared_bodyContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.struct_declared_body_element())]
        else:
            return [self.visit(ctx.struct_declared_body_element())] + self.visit(ctx.struct_declared_body())


    # struct_declared_body_element: ID (mytype) SEMICOLON;
    def visitStruct_declared_body_element(self, ctx:MiniGoParser.Struct_declared_body_elementContext):
        myStr = ctx.ID().getText()
        myType = self.visit(ctx.mytype())
        return (myStr, myType)


    # interface_declared: TYPE ID INTERFACE (LBRACE interface_declared_body RBRACE) SEMICOLON;
    def visitInterface_declared(self, ctx:MiniGoParser.Interface_declaredContext):
        myName = ctx.ID().getText()
        myPrototypeList = self.visit(ctx.interface_declared_body())
        return InterfaceType(myName, myPrototypeList)


    # interface_declared_body     : (interface_declared_element) (interface_declared_body) | (interface_declared_element);
    def visitInterface_declared_body(self, ctx:MiniGoParser.Interface_declared_bodyContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.interface_declared_element())]
        else:
            return [self.visit(ctx.interface_declared_element())] + self.visit(ctx.interface_declared_body())


    # interface_declared_element  : ID (interface_parameter_container) (mytype)? SEMICOLON;
    def visitInterface_declared_element(self, ctx:MiniGoParser.Interface_declared_elementContext):
        myName = ctx.ID().getText()
        myParam = self.visit(ctx.interface_parameter_container())
        myReturnType = self.visit(ctx.mytype()) if ctx.mytype() else VoidType()
        return Prototype(myName, myParam, myReturnType)


    # interface_parameter_container     : LPAREN list_interface_parameter RPAREN;
    def visitInterface_parameter_container(self, ctx:MiniGoParser.Interface_parameter_containerContext):
        return self.visit(ctx.list_interface_parameter())


    # list_interface_parameter          : list_interface_parameter_prime | ;
    def visitList_interface_parameter(self, ctx:MiniGoParser.List_interface_parameterContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return self.visit(ctx.list_interface_parameter_prime())


    # list_interface_parameter_prime    : list_interface_parameter_element COMMA list_interface_parameter_prime | list_interface_parameter_element;
    def visitList_interface_parameter_prime(self, ctx:MiniGoParser.List_interface_parameter_primeContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.list_interface_parameter_element())
        else:
            return self.visit(ctx.list_interface_parameter_element()) + self.visit(ctx.list_interface_parameter_prime())


    # list_interface_parameter_element  : ID (COMMA ID)* (mytype);
    def visitList_interface_parameter_element(self, ctx:MiniGoParser.List_interface_parameter_elementContext):
        myVarList = [ctx.ID(i).getText() for i in range(len(ctx.ID()))]
        myVarType = self.visit(ctx.mytype())
        return [myVarType for _ in myVarList]



#  assign_statement --------------------------------------------------------------------------
    # assignment_statement: (lhs_assignment_statement) (assignment_operator) (expression) SEMICOLON;
    def visitAssignment_statement(self, ctx:MiniGoParser.Assignment_statementContext):
        myLHS = self.visit(ctx.lhs_assignment_statement())
        if (ctx.assignment_operator().ASSIGN_STATE()):
            myRHS = self.visit(ctx.expression())
        else:
            myOp = ctx.assignment_operator().getText()[:-1]
            myRHS = BinaryOp(myOp, myLHS, self.visit(ctx.expression()))
        return Assign(myLHS, myRHS)


    # assignment_operator: ASSIGN_STATE | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN;
    def visitAssignment_operator(self, ctx:MiniGoParser.Assignment_operatorContext):
        return ctx.getChild(0).getText()


    # lhs_assignment_statement: ID
    #                         | lhs_assignment_statement (LBRACK expression RBRACK)
    #                         | lhs_assignment_statement DOT ID;
    def visitLhs_assignment_statement(self, ctx:MiniGoParser.Lhs_assignment_statementContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        elif ctx.getChildCount() == 4:
            myArr = self.visit(ctx.lhs_assignment_statement())
            myIndex = [self.visit(ctx.expression())]
            if isinstance(myArr, ArrayCell):
                return ArrayCell(myArr.arr, myArr.idx + myIndex)
            else:
                return ArrayCell(myArr, myIndex)
        else:
            myObj = self.visit(ctx.lhs_assignment_statement())
            myFieldName = ctx.ID().getText()
            return FieldAccess(myObj, myFieldName)


    # assignment_statement_without_semi_for_loop: ID (assignment_operator) (expression);
    def visitAssignment_statement_without_semi_for_loop(self, ctx:MiniGoParser.Assignment_statement_without_semi_for_loopContext):
        myLHS = Id(ctx.ID().getText())
        if ctx.assignment_operator().ASSIGN_STATE():
            myRHS = self.visit(ctx.expression())
        else:
            myOp = ctx.assignment_operator().getText()[:-1]
            myRHS = BinaryOp(myOp, myLHS, self.visit(ctx.expression()))
        return Assign(myLHS, myRHS)





# if_statement: --------------------------------------------------------------------------
    # if_statement: IF (LPAREN expression RPAREN) (function_body_container) (else_if_clause)? (else_clause)? SEMICOLON;
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        condition = self.visit(ctx.expression())
        thenStatement = Block(self.visit(ctx.function_body_container()))
        elseIfStatment = self.visit(ctx.else_if_clause()) if ctx.else_if_clause() else []
        elseStatement = Block(self.visit(ctx.else_clause())) if ctx.else_clause() else None
        return If(condition, thenStatement, processing_if(elseIfStatment, elseStatement))


    # else_if_clause : (else_if_clause_content) else_if_clause | (else_if_clause_content);
    def visitElse_if_clause(self, ctx:MiniGoParser.Else_if_clauseContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.else_if_clause_content())]
        else:
            return [self.visit(ctx.else_if_clause_content())] + self.visit(ctx.else_if_clause())


    # else_if_clause_content: ELSE IF (LPAREN expression RPAREN) (function_body_container);
    def visitElse_if_clause_content(self, ctx:MiniGoParser.Else_if_clause_contentContext):
        myExpression = self.visit(ctx.expression())
        if ctx.function_body_container().getChildCount() == 0:
            myFunctionBody = None
        else:
            myFunctionBody = Block(self.visit(ctx.function_body_container()))
        return (myExpression, myFunctionBody)


    # else_clause: ELSE function_body_container;
    def visitElse_clause(self, ctx:MiniGoParser.Else_clauseContext):
        return self.visit(ctx.function_body_container())





# for_statement: --------------------------------------------------------------------------
    # for_statement: (array_for_loop | initialization_for_loop | basic_for_loop) SEMICOLON;
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        return self.visit(ctx.getChild(0))


    # basic_for_loop: FOR expression (function_body_container);
    def visitBasic_for_loop(self, ctx:MiniGoParser.Basic_for_loopContext):
        myExp = self.visit(ctx.expression())
        myStatementList = Block(self.visit(ctx.function_body_container()))
        return ForBasic(myExp, myStatementList)


    # initialization_for_loop: FOR (variables_declared_without_semi_for_loop | assignment_statement_without_semi_for_loop) 
    #                         SEMICOLON (expression) 
    #                         SEMICOLON (assignment_statement_without_semi_for_loop)
    #                         (function_body_container);
    def visitInitialization_for_loop(self, ctx:MiniGoParser.Initialization_for_loopContext):
        myInit = self.visit(ctx.getChild(1))
        myExp = self.visit(ctx.expression())
        myUpdate = self.visit(ctx.getChild(5))
        myStatementList = Block(self.visit(ctx.function_body_container()))
        return ForStep(myInit, myExp, myUpdate, myStatementList)


    # array_for_loop: FOR (ID) COMMA (ID ASSIGN_STATE RANGE expression) (function_body_container);
    def visitArray_for_loop(self, ctx:MiniGoParser.Array_for_loopContext):
        myIndex = Id(ctx.ID(0).getText())
        myValue = Id(ctx.ID(1).getText())
        myArray = self.visit(ctx.expression())
        myStatementList = Block(self.visit(ctx.function_body_container()))
        return ForEach(myIndex, myValue, myArray, myStatementList)





# break_statement: ------------------------------------------------------------------------
    # break_statement: BREAK SEMICOLON;
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return Break()




# continue_statement: ---------------------------------------------------------------------
    # continue_statement: CONTINUE SEMICOLON;
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return Continue()




# call_statement: --------------------------------------------------------------------------
    # call_statement: (function_call | method_call) SEMICOLON;
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        return self.visit(ctx.getChild(0))




# return_statement: ------------------------------------------------------------------------
    # return_statement: RETURN expression? SEMICOLON;
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        expr = self.visit(ctx.expression()) if ctx.expression() else None
        return Return(expr)
