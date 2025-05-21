# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declared_statement_list.
    def visitDeclared_statement_list(self, ctx:MiniGoParser.Declared_statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal_primitive.
    def visitLiteral_primitive(self, ctx:MiniGoParser.Literal_primitiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#mytype.
    def visitMytype(self, ctx:MiniGoParser.MytypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primitive_type.
    def visitPrimitive_type(self, ctx:MiniGoParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_type.
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_dimention.
    def visitArray_dimention(self, ctx:MiniGoParser.Array_dimentionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_dimention_element.
    def visitArray_dimention_element(self, ctx:MiniGoParser.Array_dimention_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_lit_instance.
    def visitArray_lit_instance(self, ctx:MiniGoParser.Array_lit_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_array_value.
    def visitList_array_value(self, ctx:MiniGoParser.List_array_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_array_value_element.
    def visitList_array_value_element(self, ctx:MiniGoParser.List_array_value_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_lit_instance.
    def visitStruct_lit_instance(self, ctx:MiniGoParser.Struct_lit_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_lit_instance_body.
    def visitStruct_lit_instance_body(self, ctx:MiniGoParser.Struct_lit_instance_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_lit_instance_body_prime.
    def visitStruct_lit_instance_body_prime(self, ctx:MiniGoParser.Struct_lit_instance_body_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_lit_instance_body_element.
    def visitStruct_lit_instance_body_element(self, ctx:MiniGoParser.Struct_lit_instance_body_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_expression.
    def visitList_expression(self, ctx:MiniGoParser.List_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_expression_prime.
    def visitList_expression_prime(self, ctx:MiniGoParser.List_expression_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression.
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression1.
    def visitExpression1(self, ctx:MiniGoParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression2.
    def visitExpression2(self, ctx:MiniGoParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression3.
    def visitExpression3(self, ctx:MiniGoParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression4.
    def visitExpression4(self, ctx:MiniGoParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression5.
    def visitExpression5(self, ctx:MiniGoParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression6.
    def visitExpression6(self, ctx:MiniGoParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression7.
    def visitExpression7(self, ctx:MiniGoParser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#function_call.
    def visitFunction_call(self, ctx:MiniGoParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_call.
    def visitMethod_call(self, ctx:MiniGoParser.Method_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#temp_expression6.
    def visitTemp_expression6(self, ctx:MiniGoParser.Temp_expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_statement.
    def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_statement_prime.
    def visitList_statement_prime(self, ctx:MiniGoParser.List_statement_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declared_statement.
    def visitDeclared_statement(self, ctx:MiniGoParser.Declared_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#variables_declared.
    def visitVariables_declared(self, ctx:MiniGoParser.Variables_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#variables_declared_without_semi_for_loop.
    def visitVariables_declared_without_semi_for_loop(self, ctx:MiniGoParser.Variables_declared_without_semi_for_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constants_declared.
    def visitConstants_declared(self, ctx:MiniGoParser.Constants_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#function_declared.
    def visitFunction_declared(self, ctx:MiniGoParser.Function_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_function_parameter.
    def visitList_function_parameter(self, ctx:MiniGoParser.List_function_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_function_parameter_prime.
    def visitList_function_parameter_prime(self, ctx:MiniGoParser.List_function_parameter_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_function_parameter_element.
    def visitList_function_parameter_element(self, ctx:MiniGoParser.List_function_parameter_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#function_body_container.
    def visitFunction_body_container(self, ctx:MiniGoParser.Function_body_containerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_declared.
    def visitMethod_declared(self, ctx:MiniGoParser.Method_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#receiver_container.
    def visitReceiver_container(self, ctx:MiniGoParser.Receiver_containerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_declared.
    def visitStruct_declared(self, ctx:MiniGoParser.Struct_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_declared_body.
    def visitStruct_declared_body(self, ctx:MiniGoParser.Struct_declared_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_declared_body_element.
    def visitStruct_declared_body_element(self, ctx:MiniGoParser.Struct_declared_body_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_declared.
    def visitInterface_declared(self, ctx:MiniGoParser.Interface_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_declared_body.
    def visitInterface_declared_body(self, ctx:MiniGoParser.Interface_declared_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_declared_element.
    def visitInterface_declared_element(self, ctx:MiniGoParser.Interface_declared_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_parameter_container.
    def visitInterface_parameter_container(self, ctx:MiniGoParser.Interface_parameter_containerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_interface_parameter.
    def visitList_interface_parameter(self, ctx:MiniGoParser.List_interface_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_interface_parameter_prime.
    def visitList_interface_parameter_prime(self, ctx:MiniGoParser.List_interface_parameter_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_interface_parameter_element.
    def visitList_interface_parameter_element(self, ctx:MiniGoParser.List_interface_parameter_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignment_statement.
    def visitAssignment_statement(self, ctx:MiniGoParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignment_operator.
    def visitAssignment_operator(self, ctx:MiniGoParser.Assignment_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs_assignment_statement.
    def visitLhs_assignment_statement(self, ctx:MiniGoParser.Lhs_assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignment_statement_without_semi_for_loop.
    def visitAssignment_statement_without_semi_for_loop(self, ctx:MiniGoParser.Assignment_statement_without_semi_for_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_statement.
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_if_clause.
    def visitElse_if_clause(self, ctx:MiniGoParser.Else_if_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_if_clause_content.
    def visitElse_if_clause_content(self, ctx:MiniGoParser.Else_if_clause_contentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_clause.
    def visitElse_clause(self, ctx:MiniGoParser.Else_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_statement.
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#basic_for_loop.
    def visitBasic_for_loop(self, ctx:MiniGoParser.Basic_for_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#initialization_for_loop.
    def visitInitialization_for_loop(self, ctx:MiniGoParser.Initialization_for_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_for_loop.
    def visitArray_for_loop(self, ctx:MiniGoParser.Array_for_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_statement.
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continue_statement.
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_statement.
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_statement.
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        return self.visitChildren(ctx)



del MiniGoParser