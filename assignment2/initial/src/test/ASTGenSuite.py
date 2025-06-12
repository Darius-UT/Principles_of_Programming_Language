# MSSV: 2212629
# Họ tên: Nguyễn Lê Hoàng Phúc

import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_301(self):
        input = """var x int ;"""
        expect = str(Program([VarDecl("x",IntType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,str(expect),301))
    
    def test_302(self):
        input = """func main () {return;}; var x int ;"""
        expect = Program([FuncDecl("main",[],VoidType(),Block([Return("")])),VarDecl("x",IntType(),None)])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),302))

    def test_303(self):
        input = """
            func votien() {
                return [2] ID { {1}, {"2"}, {nil}, {struc{}} };
                return "THANKS YOU, PPL1 ";
            };
    """
        expect = Program([FuncDecl("votien",[],VoidType(),Block([Return(ArrayLiteral([IntLiteral(2)],Id("ID"),[[IntLiteral(1)],[StringLiteral("\"2\"")],[NilLiteral()],[StructLiteral("struc",[])]])),Return(StringLiteral("\"THANKS YOU, PPL1 \""))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 303))

    def test_304(self):
        input = """func main() { p.foo().bar(1); };"""
        expect = Program([FuncDecl("main",[],VoidType(),Block([MethCall(MethCall(Id("p"),"foo",[]),"bar",[IntLiteral(1)])]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 304))

    def test_305(self):
        input = """
            func test() {
                if(a > b){ return 1; 
                } else { return 0; }
            }
        """
        expect = Program([FuncDecl("test",[],VoidType(),Block([If(BinaryOp(">", Id("a"),Id("b")),Block([Return(IntLiteral(1))]),Block([Return(IntLiteral(0))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 305))

    def test_306(self):
        input = """
            func (MyStruct s) doSomething() {
                s.value := s.value + 1;
            }
        """
        expect = Program([MethodDecl("MyStruct",Id("s"),FuncDecl("doSomething",[],VoidType(),Block([Assign(FieldAccess(Id("s"), "value"), BinaryOp("+", FieldAccess(Id("s"),"value"), IntLiteral(1)))])))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 306))

    def test_307(self):
        input = """
            func main() {
                return n % 2 == 0
            }
        """
        expect = Program([
            FuncDecl("main",[], VoidType(), Block([
                Return(BinaryOp("==", BinaryOp("%", Id("n"), IntLiteral(2)), IntLiteral(0)))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 307))

    def test_308(self):
        input = """
            func isEven(n int) bool {
                return n % 2 == 0
            }
        """
        expect = Program([
            FuncDecl("isEven", [ParamDecl("n", IntType())], Id("bool"), Block([
                Return(BinaryOp("==", BinaryOp("%", Id("n"), IntLiteral(2)), IntLiteral(0)))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 308))

    def test_309(self):
        input = """
            func main() integer {
                var x int = 5
                if (isEven(x)) {
                    return;
                } else {
                    return "Xin chao, ta la Tan Muc"
                }
            }
        """
        expect = Program([
            FuncDecl("main", [], Id("integer"), Block([
                VarDecl("x", IntType(), IntLiteral(5)),
                If(FuncCall("isEven", [Id("x")]), Block([Return("")]), Block([Return(StringLiteral("\"Xin chao, ta la Tan Muc\""))]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 309))

    def test_310(self):
        input = """
            func main() integer {
                var x int = 5
                if (hello.myMethod().isEven(x)) {
                    return;
                } else {
                    return "Xin chao, ta la Tan Muc"
                }
            }
        """
        expect = Program([
            FuncDecl("main", [], Id("integer"), Block([
                VarDecl("x", IntType(), IntLiteral(5)),
                If(MethCall(MethCall(Id("hello"), "myMethod", []), "isEven", [Id("x")]), Block([Return("")]), Block([Return(StringLiteral("\"Xin chao, ta la Tan Muc\""))]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 310))

    def test_311(self):
        input = """
            func isEven(n int) bool {
                return n % 2 == 0
            }
            func main() integer {
                var x int = 5
                if (isEven(x)) {
                    return "So chan";
                } else {
                    return "So le"
                }
            }
        """
        expect = Program([
            FuncDecl("isEven", [ParamDecl("n", IntType())], Id("bool"), Block([
                Return(BinaryOp("==", BinaryOp("%", Id("n"), IntLiteral(2)), IntLiteral(0)))
            ])),
            FuncDecl("main", [], Id("integer"), Block([
                VarDecl("x", IntType(), IntLiteral(5)),
                If(FuncCall("isEven", [Id("x")]), Block([Return(StringLiteral("\"So chan\""))]), Block([Return(StringLiteral("\"So le\""))]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 311))

    def test_312(self):
        input = """func main() {return;};"""
        expect = Program([FuncDecl("main",[],VoidType(),Block([Return("")]))])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),312))

    def test_313(self):
        input = """
            func main() {
                var n int = 10
                var sum int = 0
                var i int = 1
                for (i <= n) {
                    sum := sum + i
                    i := i + 1
                }
            }
        """
        expect = Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("n", IntType(), IntLiteral(10)),
                VarDecl("sum", IntType(), IntLiteral(0)),
                VarDecl("i", IntType(), IntLiteral(1)),
                ForBasic(BinaryOp("<=", Id("i"), Id("n")), Block([
                    Assign(Id("sum"), BinaryOp("+", Id("sum"), Id("i"))),
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))
                ]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),313))

    def test_314(self):
        input = """
            func main() {
                var x int = 7
                var result boolean
                if (isEven(x)) {
                    result := true
                } else {
                    result := false
                }
            }
        """
        expect = Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("x", IntType(), IntLiteral(7)),
                VarDecl("result", BoolType(), None),
                If(FuncCall("isEven", [Id("x")]), Block([Assign(Id("result"), BooleanLiteral(True))]), Block([Assign(Id("result"), BooleanLiteral(False))]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),314))

    def test_315(self):
        input = """
            func main() {
                var arr [5] int
                arr[0] := 1
                arr[1] := 2
                arr[2] := 3
                arr[3] := 4
                arr[4] := 5

                var reversed [5] int
                var i int = 4
                var j int = 0
                for var i int = 4; i < 10; i += 1 {
                    reversed[j] := arr[i]
                    i := i - 1
                    j := j + 1
                }
            }
        """
        expect = Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("arr", ArrayType([IntLiteral(5)], IntType()), None),
                Assign(ArrayCell(Id("arr"), [IntLiteral(0)]), IntLiteral(1)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(1)]), IntLiteral(2)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(2)]), IntLiteral(3)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(3)]), IntLiteral(4)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(4)]), IntLiteral(5)),

                VarDecl("reversed", ArrayType([IntLiteral(5)], IntType()), None),
                VarDecl("i", IntType(), IntLiteral(4)),
                VarDecl("j", IntType(), IntLiteral(0)),
                ForStep(VarDecl("i", IntType(), IntLiteral(4)), BinaryOp("<", Id("i"), IntLiteral(10)), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))), Block([
                    Assign(ArrayCell(Id("reversed"), [Id("j")]), ArrayCell(Id("arr"), [Id("i")])),
                    Assign(Id("i"), BinaryOp("-", Id("i"), IntLiteral(1))),
                    Assign(Id("j"), BinaryOp("+", Id("j"), IntLiteral(1)))
                ]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),315))

    def test_316(self):
        input = """
            func factorial(n int) int {
                if (n == 0) {
                    return 1
                }
                return n * factorial(n - 1)
            }
        """
        expect = Program([
            FuncDecl("factorial", [ParamDecl("n", IntType())], IntType(), Block([
                If(BinaryOp("==", Id("n"), IntLiteral(0)), Block([Return(IntLiteral(1))]), None),
                Return(BinaryOp("*", Id("n"), FuncCall("factorial", [BinaryOp("-", Id("n"), IntLiteral(1))])))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),316))

    def test_317(self):
        input = """
            func (myMethod myStructType) main() {
                for _ , value := range myArr {
                    if (arr[i] < firstMin) {
                        secondMin := firstMin
                        firstMin := arr[i]
                    } else if ((arr[i] < secondMin) && (arr[i] != firstMin)) {
                        secondMin := arr[i]
                    }
                    i := i + 1
                }
            }
        """
        expect = Program([
            MethodDecl("myMethod", Id("myStructType"), FuncDecl("main", [], VoidType(), Block([
                ForEach(Id("_"), Id("value"), Id("myArr"), Block([
                    If(BinaryOp("<", ArrayCell(Id("arr"), [Id("i")]), Id("firstMin")), 
                        Block([Assign(Id("secondMin"), Id("firstMin")), Assign(Id("firstMin"), ArrayCell(Id("arr"), [Id("i")]))]), 
                        If(BinaryOp("&&", BinaryOp("<", ArrayCell(Id("arr"), [Id("i")]), Id("secondMin")), BinaryOp("!=", ArrayCell(Id("arr"), [Id("i")]), Id("firstMin"))), 
                            Block([Assign(Id("secondMin"), ArrayCell(Id("arr"), [Id("i")]))]), 
                            None
                        )
                    ),
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))
                ]))
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),317))

    def test_318(self):
        input = """
            func (myMethod myStructType) main() {
                for _ , value := range myArr {
                    i := i + 1
                }
            }
        """
        expect = Program([
            MethodDecl("myMethod", Id("myStructType"), FuncDecl("main", [], VoidType(), Block([
                ForEach(Id("_"), Id("value"), Id("myArr"), Block([
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))
                ]))
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),318))

    def test_319(self):
        input = """
            func (myMethod myStructType) main() {
                for _ , value := range myArr {
                    i := i + 1
                }
            }
            func (myMethod myStructType) main() {
                for _ , value := range myArr {
                    if (arr[i] < firstMin) {
                        secondMin := firstMin
                        firstMin := arr[i]
                    } else if ((arr[i] < secondMin) && (arr[i] != firstMin)) {
                        secondMin := arr[i]
                    }
                    i := i + 1
                }
            }
        """
        expect = Program([
            MethodDecl("myMethod", Id("myStructType"), FuncDecl("main", [], VoidType(), Block([
                ForEach(Id("_"), Id("value"), Id("myArr"), Block([
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))
                ]))
            ]))),
            MethodDecl("myMethod", Id("myStructType"), FuncDecl("main", [], VoidType(), Block([
                ForEach(Id("_"), Id("value"), Id("myArr"), Block([
                    If(BinaryOp("<", ArrayCell(Id("arr"), [Id("i")]), Id("firstMin")), 
                        Block([Assign(Id("secondMin"), Id("firstMin")), Assign(Id("firstMin"), ArrayCell(Id("arr"), [Id("i")]))]), 
                        If(BinaryOp("&&", BinaryOp("<", ArrayCell(Id("arr"), [Id("i")]), Id("secondMin")), BinaryOp("!=", ArrayCell(Id("arr"), [Id("i")]), Id("firstMin"))), 
                            Block([Assign(Id("secondMin"), ArrayCell(Id("arr"), [Id("i")]))]), 
                            None
                        )
                    ),
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))
                ]))
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),319))

    def test_320(self):
        input = """
            func (myMethod myStructType) main() {
                for _ , value := range myArr {
                    i := i + 1
                }
            }
            func (myMethod myStructType) main() {
                for _ , value := range myArr {
                    if (arr[i] < firstMin) {
                        secondMin := firstMin
                        firstMin := arr[i]
                    } else if ((arr[i] < secondMin) && (arr[i] != firstMin)) {
                        secondMin := arr[i]
                    }
                    i := i + 1
                }
            }
            func main() {
                var arr [5] int
                arr[0] := 1
                arr[1] := 2
                arr[2] := 3
                arr[3] := 4
                arr[4] := 5

                var reversed [5] int
                var i int = 4
                var j int = 0
                for var i int = 4; i < 10; i += 1 {
                    reversed[j] := arr[i]
                    i := i - 1
                    j := j + 1
                }
            }
        """
        expect = Program([
            MethodDecl("myMethod", Id("myStructType"), FuncDecl("main", [], VoidType(), Block([
                ForEach(Id("_"), Id("value"), Id("myArr"), Block([
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))
                ]))
            ]))),
            MethodDecl("myMethod", Id("myStructType"), FuncDecl("main", [], VoidType(), Block([
                ForEach(Id("_"), Id("value"), Id("myArr"), Block([
                    If(BinaryOp("<", ArrayCell(Id("arr"), [Id("i")]), Id("firstMin")), 
                        Block([Assign(Id("secondMin"), Id("firstMin")), Assign(Id("firstMin"), ArrayCell(Id("arr"), [Id("i")]))]), 
                        If(BinaryOp("&&", BinaryOp("<", ArrayCell(Id("arr"), [Id("i")]), Id("secondMin")), BinaryOp("!=", ArrayCell(Id("arr"), [Id("i")]), Id("firstMin"))), 
                            Block([Assign(Id("secondMin"), ArrayCell(Id("arr"), [Id("i")]))]), 
                            None
                        )
                    ),
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))
                ]))
            ]))),
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("arr", ArrayType([IntLiteral(5)], IntType()), None),
                Assign(ArrayCell(Id("arr"), [IntLiteral(0)]), IntLiteral(1)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(1)]), IntLiteral(2)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(2)]), IntLiteral(3)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(3)]), IntLiteral(4)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(4)]), IntLiteral(5)),

                VarDecl("reversed", ArrayType([IntLiteral(5)], IntType()), None),
                VarDecl("i", IntType(), IntLiteral(4)),
                VarDecl("j", IntType(), IntLiteral(0)),
                ForStep(VarDecl("i", IntType(), IntLiteral(4)), BinaryOp("<", Id("i"), IntLiteral(10)), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))), Block([
                    Assign(ArrayCell(Id("reversed"), [Id("j")]), ArrayCell(Id("arr"), [Id("i")])),
                    Assign(Id("i"), BinaryOp("-", Id("i"), IntLiteral(1))),
                    Assign(Id("j"), BinaryOp("+", Id("j"), IntLiteral(1)))
                ]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),320))

    def test_321(self):
        input = """
            func main() {
                var arr [5] int
                arr[0] := 1
                arr[1] := 2
                arr[2] := 3
                arr[3] := 4
                arr[4] := 5

                var reversed [5] int
                var i int = 4
                var j int = 0
                for var i int = 4; i < 10; i += 1 {
                    reversed[j] := arr[i]
                    i := i - 1
                    j := j + 1
                }
            }
        """
        expect = Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("arr", ArrayType([IntLiteral(5)], IntType()), None),
                Assign(ArrayCell(Id("arr"), [IntLiteral(0)]), IntLiteral(1)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(1)]), IntLiteral(2)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(2)]), IntLiteral(3)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(3)]), IntLiteral(4)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(4)]), IntLiteral(5)),

                VarDecl("reversed", ArrayType([IntLiteral(5)], IntType()), None),
                VarDecl("i", IntType(), IntLiteral(4)),
                VarDecl("j", IntType(), IntLiteral(0)),
                ForStep(VarDecl("i", IntType(), IntLiteral(4)), BinaryOp("<", Id("i"), IntLiteral(10)), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))), Block([
                    Assign(ArrayCell(Id("reversed"), [Id("j")]), ArrayCell(Id("arr"), [Id("i")])),
                    Assign(Id("i"), BinaryOp("-", Id("i"), IntLiteral(1))),
                    Assign(Id("j"), BinaryOp("+", Id("j"), IntLiteral(1)))
                ]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),321))

    def test_322(self):
        input = """
            func main() {
                var arr [5] int
                arr[0] := 1
                arr[1] := 2
                arr[2] := 3
                arr[3] := 4
                arr[4] := 5

                var reversed [5] int
                var i int = 4
                var j int = 0
                for var i int = 4; i < 10; i += 1 {
                    reversed[j] := arr[i]
                    i := i - 1
                    j := j + 1
                }
            }
        """
        expect = Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("arr", ArrayType([IntLiteral(5)], IntType()), None),
                Assign(ArrayCell(Id("arr"), [IntLiteral(0)]), IntLiteral(1)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(1)]), IntLiteral(2)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(2)]), IntLiteral(3)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(3)]), IntLiteral(4)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(4)]), IntLiteral(5)),

                VarDecl("reversed", ArrayType([IntLiteral(5)], IntType()), None),
                VarDecl("i", IntType(), IntLiteral(4)),
                VarDecl("j", IntType(), IntLiteral(0)),
                ForStep(VarDecl("i", IntType(), IntLiteral(4)), BinaryOp("<", Id("i"), IntLiteral(10)), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))), Block([
                    Assign(ArrayCell(Id("reversed"), [Id("j")]), ArrayCell(Id("arr"), [Id("i")])),
                    Assign(Id("i"), BinaryOp("-", Id("i"), IntLiteral(1))),
                    Assign(Id("j"), BinaryOp("+", Id("j"), IntLiteral(1)))
                ]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),322))

    def test_323(self):
        input = """
            func foo(){
                var a [1]int = 1;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a",ArrayType([IntLiteral(1)],IntType()),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),323))

    def test_324(self):
        input = """
            func foo(){
                var a int;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a",IntType(), None)]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),324))

    def test_325(self):
        input = """
            func foo(){
                a += 1;
                a -= 1;
                a *= 1;
                a /= 1;
                a %= 1;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("-", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("*", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("/", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("%", Id("a"), IntLiteral(1)))]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),325))
        
    def test_326(self):
        input = """
            func foo(){
                a[1 + 1] := 1;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Assign(ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(1))]),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),326))
        
    def test_327(self):
        input = """
            func foo(){
                a[2].b.c[2] := 1;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Assign(ArrayCell(FieldAccess(FieldAccess(ArrayCell(Id("a"),[IntLiteral(2)]),"b"),"c"),[IntLiteral(2)]),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),327))

    def test_328(self):
        input = """func main() { p.foo().bar(1); };"""
        expect = Program([FuncDecl("main",[],VoidType(),Block([MethCall(MethCall(Id("p"),"foo",[]),"bar",[IntLiteral(1)])]))])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),328))

    def test_329(self):
        input = """
            func foo(){
                a.b := 1;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Assign(FieldAccess(Id("a"),"b"),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),329))

    def test_330(self):
        input = """
            func foo(){
                a.b[2].c := 1;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Assign(FieldAccess(ArrayCell(FieldAccess(Id("a"),"b"),[IntLiteral(2)]),"c"),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),330))

    def test_331(self):
        input = """
            func foo(){
                break;
                continue;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Break(),Continue()]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),331))

    def test_332(self):
        input = """
            func foo(){
                return;
                return foo() + 2;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Return(None),Return(BinaryOp("+", FuncCall("foo",[]), IntLiteral(2)))]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),332))

    def test_333(self):
        input = """
            func foo(){
                foo();
                foo(foo(), 2);
                a.foo();
                a[2].c.foo(foo(), 2);
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([FuncCall("foo",[]),FuncCall("foo",[FuncCall("foo",[]),IntLiteral(2)]),MethCall(Id("a"),"foo",[]),MethCall(FieldAccess(ArrayCell(Id("a"),[IntLiteral(2)]),"c"),"foo",[FuncCall("foo",[]),IntLiteral(2)])]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),333))

    def test_334(self):
        input = """
            func foo(){
                if(1) {return;}
                if(1 + 1) {
                    return 1;
                    return;
                }
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(None)]), None),
            If(BinaryOp("+", IntLiteral(1), IntLiteral(1)), Block([Return(IntLiteral(1)),Return(None)]), None)]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),334))

    def test_335(self):
        input = """
            func foo(){
                if(1) { return;
                }else if(1) {
                    return 1;
                    return ;
                } else {return;}

                if(1) {return;
                }  else {
                    return 1;
                    return ;
                }

            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(None)]), 
                If(IntLiteral(1), Block([Return(IntLiteral(1)),Return(None)]), Block([Return(None)]))),
            If(IntLiteral(1), Block([Return(None)]), Block([Return(IntLiteral(1)),Return(None)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),335))

    def test_336(self):
        input = """
            func foo(){
                if(1) {
                    return 1;
                }else if(2) {
                    return 2;
                } else if(3) {
                    return 3;
                } else if(4) {
                    return 4;
                } 

            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(IntLiteral(1))]), 
                If(IntLiteral(2), Block([Return(IntLiteral(2))]), 
                    If(IntLiteral(3), Block([Return(IntLiteral(3))]), 
                        If(IntLiteral(4), Block([Return(IntLiteral(4))]), None))))]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),336))

    def test_337(self):
        input = """
            func votien() {
                for a.i[8] {
                    return;
                    return 1;
                }
                for i := 0; i[1] < 10; i *= 2+3  {
                    return;
                    return 1;
                }
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([ForBasic(ArrayCell(FieldAccess(Id("a"),"i"),[IntLiteral(8)]),Block([Return(None),Return(IntLiteral(1))])),ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<", ArrayCell(Id("i"),[IntLiteral(1)]), IntLiteral(10)),Assign(Id("i"),BinaryOp("*", Id("i"), BinaryOp("+", IntLiteral(2), IntLiteral(3)))),Block([Return(None),Return(IntLiteral(1))]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),337))

    def test_338(self):
        input = """
            func votien() {
                for index, value := range [2]int{1,2} {
                     return;
                    return 1;
                }
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([ForEach(Id("index"),Id("value"),ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]),Block([Return(None),Return(IntLiteral(1))]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),338))

    def test_339(self):
        input = """
            func votien() {
                a.b.c[2].d()
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([MethCall(ArrayCell(FieldAccess(FieldAccess(Id("a"),"b"),"c"),[IntLiteral(2)]),"d",[])]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),339))

    def test_340(self):
        input = """func main() { p.foo().bar(1); };"""
        expect = Program([FuncDecl("main",[],VoidType(),Block([MethCall(MethCall(Id("p"),"foo",[]),"bar",[IntLiteral(1)])]))])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),340))

    def test_341(self):
        input = """func main() { p.foo().bar(1); };"""
        expect = Program([FuncDecl("main",[],VoidType(),Block([MethCall(MethCall(Id("p"),"foo",[]),"bar",[IntLiteral(1)])]))])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),341))

    def test_342(self):
        input = """
    func foo () {var a = 1;}
    func foo () int {var a = 1;}
    func foo () [2] ID {var a = 1;}
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])),
			FuncDecl("foo",[],IntType(),Block([VarDecl("a", None,IntLiteral(1))])),
			FuncDecl("foo",[],ArrayType([IntLiteral(2)],Id("ID")),Block([VarDecl("a", None,IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 342))

    def test_343(self):
        input = """
    func foo (a int) {var a = 1;}
    func foo (a int, b ID) {var a = 1;}
    func foo (a, b int) {var a = 1;}
"""
        expect = Program([FuncDecl("foo",[ParamDecl("a",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])),
			FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",Id("ID"))],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])),
			FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 343))

    def test_344(self):
        input = """
    func (ID ID) foo (a int) {var a = 1;}
    func (ID ID) foo (a int, b ID) {var a = 1;}
    func (ID ID) foo (a, b int) {var a = 1;}
"""
        expect = Program([MethodDecl("ID",Id("ID"),FuncDecl("foo",[ParamDecl("a",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))),
			MethodDecl("ID",Id("ID"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",Id("ID"))],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))),
			MethodDecl("ID",Id("ID"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 344))

    def test_345(self):
        input = """
        type INTERFACE interface {
            foo();
            foo() int;
            foo() [2]ID;
            foo(a int);
            foo(a int, b int);
            foo(a, b int);
        }
"""
        expect = Program([InterfaceType("INTERFACE",[
            Prototype("foo",[],VoidType()),Prototype("foo",[],IntType()),
            Prototype("foo",[],ArrayType([IntLiteral(2)],Id("ID"))),
            Prototype("foo",[IntType()],VoidType()),
            Prototype("foo",[IntType(),IntType()],VoidType()),
            Prototype("foo",[IntType(),IntType()],VoidType())])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 345))

    def test_346(self):
        input = """
    func foo () {
        continue;
        break;
        return;
        return 1;
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Continue(),Break(),Return(None),Return(IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 346))

    def test_347(self):
        input = """
    func foo () {
        var a int = 1;
        var a float = 1;
        var a boolean;
        var a string = 1;
        var a = 1;
        var a ID = 1;
        var a [ID][1] int = 1;
        const a = 1;
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            VarDecl("a",IntType(),IntLiteral(1)),
            VarDecl("a",FloatType(),IntLiteral(1)),
            VarDecl("a",BoolType(), None),
            VarDecl("a",StringType(),IntLiteral(1)),
            VarDecl("a", None,IntLiteral(1)),
            VarDecl("a",Id("ID"),IntLiteral(1)),
            VarDecl("a",ArrayType([Id("ID"),IntLiteral(1)],IntType()),IntLiteral(1)),
            ConstDecl("a",None,IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 347))

    def test_348(self):
        input = """
    func foo () {
        var a int = 1;
        var a float = 1;
        var a boolean;
        var a string = 1;
        var a = 1;
        var a ID = 1;
        var a [ID][1] int = 1;
        const a = 1;
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            VarDecl("a",IntType(),IntLiteral(1)),
            VarDecl("a",FloatType(),IntLiteral(1)),
            VarDecl("a",BoolType(), None),
            VarDecl("a",StringType(),IntLiteral(1)),
            VarDecl("a", None,IntLiteral(1)),
            VarDecl("a",Id("ID"),IntLiteral(1)),
            VarDecl("a",ArrayType([Id("ID"),IntLiteral(1)],IntType()),IntLiteral(1)),
            ConstDecl("a",None,IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 348))

    def test_349(self):
        input = """
    func foo () {
        a := 1;
        a += 1;
        a -= 1;
        a *= 1;
        a /= 1;
        a %= 1;
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(Id("a"),IntLiteral(1)),
            Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),
            Assign(Id("a"),BinaryOp("-", Id("a"), IntLiteral(1))),
            Assign(Id("a"),BinaryOp("*", Id("a"), IntLiteral(1))),
            Assign(Id("a"),BinaryOp("/", Id("a"), IntLiteral(1))),
            Assign(Id("a"),BinaryOp("%", Id("a"), IntLiteral(1)))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 349))

    def test_350(self):
        input = """
    func foo () {
        a[1] := 2;
        a[2][1+1] += 3;
        a.b -= 5;
        b.b[a + b].b.c[2] := 4;
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(ArrayCell(Id("a"),[IntLiteral(1)]),IntLiteral(2)),
            Assign(ArrayCell(Id("a"),[IntLiteral(2),BinaryOp("+", IntLiteral(1), IntLiteral(1))]),BinaryOp("+", ArrayCell(Id("a"),[IntLiteral(2),BinaryOp("+", IntLiteral(1), IntLiteral(1))]), IntLiteral(3))),
            Assign(FieldAccess(Id("a"),"b"),BinaryOp("-", FieldAccess(Id("a"),"b"), IntLiteral(5))),
            Assign(ArrayCell(FieldAccess(FieldAccess(ArrayCell(FieldAccess(Id("b"),"b"),[BinaryOp("+", Id("a"), Id("b"))]),"b"),"c"),[IntLiteral(2)]),IntLiteral(4))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 350))

    def test_351(self):
        input = """
    func foo () {
        a();
        a(1, 2);
        a(1);
        b.a.a();
        b.a.a(1, 2);
        b.a.a(1);
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            FuncCall("a",[]),
            FuncCall("a",[IntLiteral(1),IntLiteral(2)]),
            FuncCall("a",[IntLiteral(1)]),
            MethCall(FieldAccess(Id("b"),"a"),"a",[]),
            MethCall(FieldAccess(Id("b"),"a"),"a",[IntLiteral(1),IntLiteral(2)]),
            MethCall(FieldAccess(Id("b"),"a"),"a",[IntLiteral(1)])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 351))
    
    def test_352(self):
        input = """
        func foo () {
            if (a) {return;}
            if (b) {return;} else {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            If(Id("a"),Block([Return(None)]), None),
            If(Id("b"),Block([Return(None)]),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 352))

    def test_353(self):
        input = """
        func foo () {
            for(1) {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([ForBasic(IntLiteral(1),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 353))

    def test_354(self):
        input = """
        func foo () {
            for a, b := range 2 {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([ForEach(Id("a"),Id("b"),IntLiteral(2),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 354))

    def test_355(self):
        input = """
        func foo () {
            for a, b := range 2 {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([ForEach(Id("a"),Id("b"),IntLiteral(2),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 355))

    def test_356(self):
        input = """
        func foo () {
            for var a = 1; a < 10; a := 1 {return;}
            for a += 1; a < 10; a -= 1 {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(10)),Assign(Id("a"),IntLiteral(1)),Block([Return(None)])),ForStep(Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),BinaryOp("<", Id("a"), IntLiteral(10)),Assign(Id("a"),BinaryOp("-", Id("a"), IntLiteral(1))),Block([Return(None)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 356))

    def test_357(self):
        input = """
        func foo () {
            if (1){return;} else if (2){return;} else if (3){return;} else {return;}
            if (1){return;} else if (2){return;} else if (3){return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(None)]), 
               If(IntLiteral(2), Block([Return(None)]), 
                  If(IntLiteral(3), Block([Return(None)]), Block([Return(None)])))),
            If(IntLiteral(1), Block([Return(None)]), 
               If(IntLiteral(2), Block([Return(None)]), 
                  If(IntLiteral(3), Block([Return(None)]), None)))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 357))

    def test_358(self):
        input = """
        func foo () {
            return a[2][3][4];
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Return(ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3),IntLiteral(4)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 358))

    def test_359(self):
        input = """
        func foo () {
            a.b[2][3][4] := 1;
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(ArrayCell(FieldAccess(Id("a"),"b"),[IntLiteral(2),IntLiteral(3),IntLiteral(4)]),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 359))

    def test_360(self):
        input = """
        func foo () {
            a[1*2][1+2] := a[1*2][1+2];
            a[1+2] := a[1+2];
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(ArrayCell(Id("a"),[BinaryOp("*", IntLiteral(1), IntLiteral(2)),BinaryOp("+", IntLiteral(1), IntLiteral(2))]),ArrayCell(Id("a"),[BinaryOp("*", IntLiteral(1), IntLiteral(2)),BinaryOp("+", IntLiteral(1), IntLiteral(2))])),
            Assign(ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(2))]),ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(2))]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 360))

    def test_361(self):
        input = """const VoTien = foo( a[0b1][3] ); """
        expect = Program([ConstDecl("VoTien",None,FuncCall("foo",[ArrayCell(Id("a"),[IntLiteral("0b1"),IntLiteral(3)])]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 361))

    def test_362(self):
        input = """func main() { p.foo().bar(1); };"""
        expect = Program([FuncDecl("main",[],VoidType(),Block([MethCall(MethCall(Id("p"),"foo",[]),"bar",[IntLiteral(1)])]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 362))

    def test_363(self):
        input = """var x int ;"""
        expect = str(Program([VarDecl("x",IntType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,str(expect),363))
    
    def test_364(self):
        input = """func main () {return;}; var x int ;"""
        expect = Program([FuncDecl("main",[],VoidType(),Block([Return("")])),VarDecl("x",IntType(),None)])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),364))

    def test_365(self):
        input = """
            func votien() {
                return [2] ID { {1}, {"2"}, {nil}, {struc{}} };
                return "THANKS YOU, PPL1 ";
            };
    """
        expect = Program([FuncDecl("votien",[],VoidType(),Block([Return(ArrayLiteral([IntLiteral(2)],Id("ID"),[[IntLiteral(1)],[StringLiteral("\"2\"")],[NilLiteral()],[StructLiteral("struc",[])]])),Return(StringLiteral("\"THANKS YOU, PPL1 \""))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 365))

    def test_366(self):
        input = """func main() { p.foo().bar(1); };"""
        expect = Program([FuncDecl("main",[],VoidType(),Block([MethCall(MethCall(Id("p"),"foo",[]),"bar",[IntLiteral(1)])]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 366))

    def test_367(self):
        input = """
            func test() {
                if(a > b){ return 1; 
                } else { return 0; }
            }
        """
        expect = Program([FuncDecl("test",[],VoidType(),Block([If(BinaryOp(">", Id("a"),Id("b")),Block([Return(IntLiteral(1))]),Block([Return(IntLiteral(0))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 367))

    def test_368(self):
        input = """
            func (MyStruct s) doSomething() {
                s.value := s.value + 1;
            }
        """
        expect = Program([MethodDecl("MyStruct",Id("s"),FuncDecl("doSomething",[],VoidType(),Block([Assign(FieldAccess(Id("s"), "value"), BinaryOp("+", FieldAccess(Id("s"),"value"), IntLiteral(1)))])))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 368))

    def test_369(self):
        input = """
            func main() {
                return n % 2 == 0
            }
        """
        expect = Program([
            FuncDecl("main",[], VoidType(), Block([
                Return(BinaryOp("==", BinaryOp("%", Id("n"), IntLiteral(2)), IntLiteral(0)))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 369))

    def test_370(self):
        input = """
            func isEven(n int) bool {
                return n % 2 == 0
            }
        """
        expect = Program([
            FuncDecl("isEven", [ParamDecl("n", IntType())], Id("bool"), Block([
                Return(BinaryOp("==", BinaryOp("%", Id("n"), IntLiteral(2)), IntLiteral(0)))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 370))

    def test_371(self):
        input = """
            func main() integer {
                var x int = 5
                if (isEven(x)) {
                    return;
                } else {
                    return "Xin chao, ta la Tan Muc"
                }
            }
        """
        expect = Program([
            FuncDecl("main", [], Id("integer"), Block([
                VarDecl("x", IntType(), IntLiteral(5)),
                If(FuncCall("isEven", [Id("x")]), Block([Return("")]), Block([Return(StringLiteral("\"Xin chao, ta la Tan Muc\""))]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 371))

    def test_372(self):
        input = """
            func main() integer {
                var x int = 5
                if (hello.myMethod().isEven(x)) {
                    return;
                } else {
                    return "Xin chao, ta la Tan Muc"
                }
            }
        """
        expect = Program([
            FuncDecl("main", [], Id("integer"), Block([
                VarDecl("x", IntType(), IntLiteral(5)),
                If(MethCall(MethCall(Id("hello"), "myMethod", []), "isEven", [Id("x")]), Block([Return("")]), Block([Return(StringLiteral("\"Xin chao, ta la Tan Muc\""))]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 372))

    def test_373(self):
        input = """
            func isEven(n int) bool {
                return n % 2 == 0
            }
            func main() integer {
                var x int = 5
                if (isEven(x)) {
                    return "So chan";
                } else {
                    return "So le"
                }
            }
        """
        expect = Program([
            FuncDecl("isEven", [ParamDecl("n", IntType())], Id("bool"), Block([
                Return(BinaryOp("==", BinaryOp("%", Id("n"), IntLiteral(2)), IntLiteral(0)))
            ])),
            FuncDecl("main", [], Id("integer"), Block([
                VarDecl("x", IntType(), IntLiteral(5)),
                If(FuncCall("isEven", [Id("x")]), Block([Return(StringLiteral("\"So chan\""))]), Block([Return(StringLiteral("\"So le\""))]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 373))

    def test_374(self):
        input = """func main() {return;};"""
        expect = Program([FuncDecl("main",[],VoidType(),Block([Return("")]))])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),374))

    def test_375(self):
        input = """
            func main() {
                var n int = 10
                var sum int = 0
                var i int = 1
                for (i <= n) {
                    sum := sum + i
                    i := i + 1
                }
            }
        """
        expect = Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("n", IntType(), IntLiteral(10)),
                VarDecl("sum", IntType(), IntLiteral(0)),
                VarDecl("i", IntType(), IntLiteral(1)),
                ForBasic(BinaryOp("<=", Id("i"), Id("n")), Block([
                    Assign(Id("sum"), BinaryOp("+", Id("sum"), Id("i"))),
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))
                ]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),375))

    def test_376(self):
        input = """
            func main() {
                var x int = 7
                var result boolean
                if (isEven(x)) {
                    result := true
                } else {
                    result := false
                }
            }
        """
        expect = Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("x", IntType(), IntLiteral(7)),
                VarDecl("result", BoolType(), None),
                If(FuncCall("isEven", [Id("x")]), Block([Assign(Id("result"), BooleanLiteral(True))]), Block([Assign(Id("result"), BooleanLiteral(False))]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),376))

    def test_377(self):
        input = """
            func main() {
                var arr [5] int
                arr[0] := 1
                arr[1] := 2
                arr[2] := 3
                arr[3] := 4
                arr[4] := 5

                var reversed [5] int
                var i int = 4
                var j int = 0
                for var i int = 4; i < 10; i += 1 {
                    reversed[j] := arr[i]
                    i := i - 1
                    j := j + 1
                }
            }
        """
        expect = Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("arr", ArrayType([IntLiteral(5)], IntType()), None),
                Assign(ArrayCell(Id("arr"), [IntLiteral(0)]), IntLiteral(1)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(1)]), IntLiteral(2)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(2)]), IntLiteral(3)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(3)]), IntLiteral(4)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(4)]), IntLiteral(5)),

                VarDecl("reversed", ArrayType([IntLiteral(5)], IntType()), None),
                VarDecl("i", IntType(), IntLiteral(4)),
                VarDecl("j", IntType(), IntLiteral(0)),
                ForStep(VarDecl("i", IntType(), IntLiteral(4)), BinaryOp("<", Id("i"), IntLiteral(10)), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))), Block([
                    Assign(ArrayCell(Id("reversed"), [Id("j")]), ArrayCell(Id("arr"), [Id("i")])),
                    Assign(Id("i"), BinaryOp("-", Id("i"), IntLiteral(1))),
                    Assign(Id("j"), BinaryOp("+", Id("j"), IntLiteral(1)))
                ]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),377))

    def test_378(self):
        input = """
            func factorial(n int) int {
                if (n == 0) {
                    return 1
                }
                return n * factorial(n - 1)
            }
        """
        expect = Program([
            FuncDecl("factorial", [ParamDecl("n", IntType())], IntType(), Block([
                If(BinaryOp("==", Id("n"), IntLiteral(0)), Block([Return(IntLiteral(1))]), None),
                Return(BinaryOp("*", Id("n"), FuncCall("factorial", [BinaryOp("-", Id("n"), IntLiteral(1))])))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),378))

    def test_379(self):
        input = """
            func (myMethod myStructType) main() {
                for _ , value := range myArr {
                    if (arr[i] < firstMin) {
                        secondMin := firstMin
                        firstMin := arr[i]
                    } else if ((arr[i] < secondMin) && (arr[i] != firstMin)) {
                        secondMin := arr[i]
                    }
                    i := i + 1
                }
            }
        """
        expect = Program([
            MethodDecl("myMethod", Id("myStructType"), FuncDecl("main", [], VoidType(), Block([
                ForEach(Id("_"), Id("value"), Id("myArr"), Block([
                    If(BinaryOp("<", ArrayCell(Id("arr"), [Id("i")]), Id("firstMin")), 
                        Block([Assign(Id("secondMin"), Id("firstMin")), Assign(Id("firstMin"), ArrayCell(Id("arr"), [Id("i")]))]), 
                        If(BinaryOp("&&", BinaryOp("<", ArrayCell(Id("arr"), [Id("i")]), Id("secondMin")), BinaryOp("!=", ArrayCell(Id("arr"), [Id("i")]), Id("firstMin"))), 
                            Block([Assign(Id("secondMin"), ArrayCell(Id("arr"), [Id("i")]))]), 
                            None
                        )
                    ),
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))
                ]))
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),379))

    def test_380(self):
        input = """
            func (myMethod myStructType) main() {
                for _ , value := range myArr {
                    i := i + 1
                }
            }
        """
        expect = Program([
            MethodDecl("myMethod", Id("myStructType"), FuncDecl("main", [], VoidType(), Block([
                ForEach(Id("_"), Id("value"), Id("myArr"), Block([
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))
                ]))
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),380))

    def test_381(self):
        input = """
            func (myMethod myStructType) main() {
                for _ , value := range myArr {
                    i := i + 1
                }
            }
            func (myMethod myStructType) main() {
                for _ , value := range myArr {
                    if (arr[i] < firstMin) {
                        secondMin := firstMin
                        firstMin := arr[i]
                    } else if ((arr[i] < secondMin) && (arr[i] != firstMin)) {
                        secondMin := arr[i]
                    }
                    i := i + 1
                }
            }
        """
        expect = Program([
            MethodDecl("myMethod", Id("myStructType"), FuncDecl("main", [], VoidType(), Block([
                ForEach(Id("_"), Id("value"), Id("myArr"), Block([
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))
                ]))
            ]))),
            MethodDecl("myMethod", Id("myStructType"), FuncDecl("main", [], VoidType(), Block([
                ForEach(Id("_"), Id("value"), Id("myArr"), Block([
                    If(BinaryOp("<", ArrayCell(Id("arr"), [Id("i")]), Id("firstMin")), 
                        Block([Assign(Id("secondMin"), Id("firstMin")), Assign(Id("firstMin"), ArrayCell(Id("arr"), [Id("i")]))]), 
                        If(BinaryOp("&&", BinaryOp("<", ArrayCell(Id("arr"), [Id("i")]), Id("secondMin")), BinaryOp("!=", ArrayCell(Id("arr"), [Id("i")]), Id("firstMin"))), 
                            Block([Assign(Id("secondMin"), ArrayCell(Id("arr"), [Id("i")]))]), 
                            None
                        )
                    ),
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))
                ]))
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),381))

    def test_382(self):
        input = """
            func (myMethod myStructType) main() {
                for _ , value := range myArr {
                    i := i + 1
                }
            }
            func (myMethod myStructType) main() {
                for _ , value := range myArr {
                    if (arr[i] < firstMin) {
                        secondMin := firstMin
                        firstMin := arr[i]
                    } else if ((arr[i] < secondMin) && (arr[i] != firstMin)) {
                        secondMin := arr[i]
                    }
                    i := i + 1
                }
            }
            func main() {
                var arr [5] int
                arr[0] := 1
                arr[1] := 2
                arr[2] := 3
                arr[3] := 4
                arr[4] := 5

                var reversed [5] int
                var i int = 4
                var j int = 0
                for var i int = 4; i < 10; i += 1 {
                    reversed[j] := arr[i]
                    i := i - 1
                    j := j + 1
                }
            }
        """
        expect = Program([
            MethodDecl("myMethod", Id("myStructType"), FuncDecl("main", [], VoidType(), Block([
                ForEach(Id("_"), Id("value"), Id("myArr"), Block([
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))
                ]))
            ]))),
            MethodDecl("myMethod", Id("myStructType"), FuncDecl("main", [], VoidType(), Block([
                ForEach(Id("_"), Id("value"), Id("myArr"), Block([
                    If(BinaryOp("<", ArrayCell(Id("arr"), [Id("i")]), Id("firstMin")), 
                        Block([Assign(Id("secondMin"), Id("firstMin")), Assign(Id("firstMin"), ArrayCell(Id("arr"), [Id("i")]))]), 
                        If(BinaryOp("&&", BinaryOp("<", ArrayCell(Id("arr"), [Id("i")]), Id("secondMin")), BinaryOp("!=", ArrayCell(Id("arr"), [Id("i")]), Id("firstMin"))), 
                            Block([Assign(Id("secondMin"), ArrayCell(Id("arr"), [Id("i")]))]), 
                            None
                        )
                    ),
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))
                ]))
            ]))),
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("arr", ArrayType([IntLiteral(5)], IntType()), None),
                Assign(ArrayCell(Id("arr"), [IntLiteral(0)]), IntLiteral(1)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(1)]), IntLiteral(2)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(2)]), IntLiteral(3)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(3)]), IntLiteral(4)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(4)]), IntLiteral(5)),

                VarDecl("reversed", ArrayType([IntLiteral(5)], IntType()), None),
                VarDecl("i", IntType(), IntLiteral(4)),
                VarDecl("j", IntType(), IntLiteral(0)),
                ForStep(VarDecl("i", IntType(), IntLiteral(4)), BinaryOp("<", Id("i"), IntLiteral(10)), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))), Block([
                    Assign(ArrayCell(Id("reversed"), [Id("j")]), ArrayCell(Id("arr"), [Id("i")])),
                    Assign(Id("i"), BinaryOp("-", Id("i"), IntLiteral(1))),
                    Assign(Id("j"), BinaryOp("+", Id("j"), IntLiteral(1)))
                ]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),382))

    def test_383(self):
        input = """
            func main() {
                var arr [5] int
                arr[0] := 1
                arr[1] := 2
                arr[2] := 3
                arr[3] := 4
                arr[4] := 5

                var reversed [5] int
                var i int = 4
                var j int = 0
                for var i int = 4; i < 10; i += 1 {
                    reversed[j] := arr[i]
                    i := i - 1
                    j := j + 1
                }
            }
        """
        expect = Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("arr", ArrayType([IntLiteral(5)], IntType()), None),
                Assign(ArrayCell(Id("arr"), [IntLiteral(0)]), IntLiteral(1)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(1)]), IntLiteral(2)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(2)]), IntLiteral(3)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(3)]), IntLiteral(4)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(4)]), IntLiteral(5)),

                VarDecl("reversed", ArrayType([IntLiteral(5)], IntType()), None),
                VarDecl("i", IntType(), IntLiteral(4)),
                VarDecl("j", IntType(), IntLiteral(0)),
                ForStep(VarDecl("i", IntType(), IntLiteral(4)), BinaryOp("<", Id("i"), IntLiteral(10)), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))), Block([
                    Assign(ArrayCell(Id("reversed"), [Id("j")]), ArrayCell(Id("arr"), [Id("i")])),
                    Assign(Id("i"), BinaryOp("-", Id("i"), IntLiteral(1))),
                    Assign(Id("j"), BinaryOp("+", Id("j"), IntLiteral(1)))
                ]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),383))

    def test_384(self):
        input = """
            func main() {
                var arr [5] int
                arr[0] := 1
                arr[1] := 2
                arr[2] := 3
                arr[3] := 4
                arr[4] := 5

                var reversed [5] int
                var i int = 4
                var j int = 0
                for var i int = 4; i < 10; i += 1 {
                    reversed[j] := arr[i]
                    i := i - 1
                    j := j + 1
                }
            }
        """
        expect = Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("arr", ArrayType([IntLiteral(5)], IntType()), None),
                Assign(ArrayCell(Id("arr"), [IntLiteral(0)]), IntLiteral(1)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(1)]), IntLiteral(2)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(2)]), IntLiteral(3)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(3)]), IntLiteral(4)),
                Assign(ArrayCell(Id("arr"), [IntLiteral(4)]), IntLiteral(5)),

                VarDecl("reversed", ArrayType([IntLiteral(5)], IntType()), None),
                VarDecl("i", IntType(), IntLiteral(4)),
                VarDecl("j", IntType(), IntLiteral(0)),
                ForStep(VarDecl("i", IntType(), IntLiteral(4)), BinaryOp("<", Id("i"), IntLiteral(10)), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))), Block([
                    Assign(ArrayCell(Id("reversed"), [Id("j")]), ArrayCell(Id("arr"), [Id("i")])),
                    Assign(Id("i"), BinaryOp("-", Id("i"), IntLiteral(1))),
                    Assign(Id("j"), BinaryOp("+", Id("j"), IntLiteral(1)))
                ]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),384))

    def test_385(self):
        input = """
            func foo(){
                var a [1]int = 1;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a",ArrayType([IntLiteral(1)],IntType()),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),385))

    def test_386(self):
        input = """
            func foo(){
                var a int;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a",IntType(), None)]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),386))

    def test_387(self):
        input = """
            func foo(){
                a += 1;
                a -= 1;
                a *= 1;
                a /= 1;
                a %= 1;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("-", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("*", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("/", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("%", Id("a"), IntLiteral(1)))]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),387))
        
    def test_388(self):
        input = """
            func foo(){
                a[1 + 1] := 1;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Assign(ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(1))]),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),388))
        
    def test_389(self):
        input = """
            func foo(){
                a[2].b.c[2] := 1;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Assign(ArrayCell(FieldAccess(FieldAccess(ArrayCell(Id("a"),[IntLiteral(2)]),"b"),"c"),[IntLiteral(2)]),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),389))

    def test_390(self):
        input = """func main() { p.foo().bar(1); };"""
        expect = Program([FuncDecl("main",[],VoidType(),Block([MethCall(MethCall(Id("p"),"foo",[]),"bar",[IntLiteral(1)])]))])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),390))

    def test_391(self):
        input = """
            func foo(){
                a.b := 1;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Assign(FieldAccess(Id("a"),"b"),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),391))

    def test_392(self):
        input = """
            func foo(){
                a.b[2].c := 1;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Assign(FieldAccess(ArrayCell(FieldAccess(Id("a"),"b"),[IntLiteral(2)]),"c"),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),392))

    def test_393(self):
        input = """
            func foo(){
                break;
                continue;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Break(),Continue()]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),393))

    def test_394(self):
        input = """
            func foo(){
                return;
                return foo() + 2;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Return(None),Return(BinaryOp("+", FuncCall("foo",[]), IntLiteral(2)))]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),394))

    def test_395(self):
        input = """
            func foo(){
                foo();
                foo(foo(), 2);
                a.foo();
                a[2].c.foo(foo(), 2);
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([FuncCall("foo",[]),FuncCall("foo",[FuncCall("foo",[]),IntLiteral(2)]),MethCall(Id("a"),"foo",[]),MethCall(FieldAccess(ArrayCell(Id("a"),[IntLiteral(2)]),"c"),"foo",[FuncCall("foo",[]),IntLiteral(2)])]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),395))

    def test_396(self):
        input = """
            func foo(){
                if(1) {return;}
                if(1 + 1) {
                    return 1;
                    return;
                }
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(None)]), None),
            If(BinaryOp("+", IntLiteral(1), IntLiteral(1)), Block([Return(IntLiteral(1)),Return(None)]), None)]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),396))

    def test_397(self):
        input = """
            func foo(){
                if(1) { return;
                }else if(1) {
                    return 1;
                    return ;
                } else {return;}

                if(1) {return;
                }  else {
                    return 1;
                    return ;
                }

            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(None)]), 
                If(IntLiteral(1), Block([Return(IntLiteral(1)),Return(None)]), Block([Return(None)]))),
            If(IntLiteral(1), Block([Return(None)]), Block([Return(IntLiteral(1)),Return(None)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),397))

    def test_398(self):
        input = """
            func foo(){
                if(1) {
                    return 1;
                }else if(2) {
                    return 2;
                } else if(3) {
                    return 3;
                } else if(4) {
                    return 4;
                } 

            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(IntLiteral(1))]), 
                If(IntLiteral(2), Block([Return(IntLiteral(2))]), 
                    If(IntLiteral(3), Block([Return(IntLiteral(3))]), 
                        If(IntLiteral(4), Block([Return(IntLiteral(4))]), None))))]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),398))

    def test_399(self):
        input = """
            func votien() {
                for a.i[8] {
                    return;
                    return 1;
                }
                for i := 0; i[1] < 10; i *= 2+3  {
                    return;
                    return 1;
                }
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([ForBasic(ArrayCell(FieldAccess(Id("a"),"i"),[IntLiteral(8)]),Block([Return(None),Return(IntLiteral(1))])),ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<", ArrayCell(Id("i"),[IntLiteral(1)]), IntLiteral(10)),Assign(Id("i"),BinaryOp("*", Id("i"), BinaryOp("+", IntLiteral(2), IntLiteral(3)))),Block([Return(None),Return(IntLiteral(1))]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),399))

    def test_400(self):
        input = """
            func votien() {
                for index, value := range [2]int{1,2} {
                     return;
                    return 1;
                }
            }
"""
        expect = Program([FuncDecl("votien",[],VoidType(),Block([ForEach(Id("index"),Id("value"),ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]),Block([Return(None),Return(IntLiteral(1))]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),400))