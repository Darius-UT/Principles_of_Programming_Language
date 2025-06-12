import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_201(self):
        self.assertTrue(TestParser.checkParser("abc","Error on line 1 col 1: abc", 201))

    def test_202(self):
        self.assertTrue(TestParser.checkParser("if","Error on line 1 col 1: if", 202))

    def test_203(self):
        self.assertTrue(TestParser.checkParser("+","Error on line 1 col 1: +", 203))

    def test_204(self):
        self.assertTrue(TestParser.checkParser("[]","Error on line 1 col 1: [", 204))

    def test_205(self):
        self.assertTrue(TestParser.checkParser("_myVar","Error on line 1 col 1: _myVar", 205))

    def test_206(self):
        self.assertTrue(TestParser.checkParser("12","Error on line 1 col 1: 12", 206))

    def test_207(self):
        self.assertTrue(TestParser.checkParser("0x1A","Error on line 1 col 1: 0x1A", 207))

    def test_208(self):
        self.assertTrue(TestParser.checkParser("3.14","Error on line 1 col 1: 3.14", 208))

    def test_209(self):
        self.assertTrue(TestParser.checkParser("\"hello\"","Error on line 1 col 1: \"hello\"", 209))

    def test_210(self):
        self.assertTrue(TestParser.checkParser("// comment","Error on line 1 col 11: <EOF>", 210))

    def test_211(self):
        self.assertTrue(TestParser.checkParser("/* block comment */","Error on line 1 col 20: <EOF>", 211))

    def test_212(self):
        self.assertTrue(TestParser.checkParser("^","^", 212))

    def test_213(self):
        self.assertTrue(TestParser.checkParser("\"unterminated","\"unterminated", 213))

    def test_214(self):
        self.assertTrue(TestParser.checkParser("\"illegal\\g\"","\"illegal\g", 214))

    def test_215(self):
        self.assertTrue(TestParser.checkParser("var","Error on line 1 col 4: <EOF>", 215))

    def test_216(self):
        self.assertTrue(TestParser.checkParser("type","Error on line 1 col 5: <EOF>", 216))

    def test_217(self):
        self.assertTrue(TestParser.checkParser("func","Error on line 1 col 5: <EOF>", 217))

    def test_218(self):
        self.assertTrue(TestParser.checkParser("return","Error on line 1 col 1: return", 218))

    def test_219(self):
        self.assertTrue(TestParser.checkParser("break","Error on line 1 col 1: break", 219))

    def test_220(self):
        self.assertTrue(TestParser.checkParser("continue","Error on line 1 col 1: continue", 220))

    def test_221(self):
        self.assertTrue(TestParser.checkParser("nil","Error on line 1 col 1: nil", 221))

    def test_222(self):
        self.assertTrue(TestParser.checkParser("true","Error on line 1 col 1: true",222))

    def test_223(self):
        self.assertTrue(TestParser.checkParser("false","Error on line 1 col 1: false",223))

    def test_224(self):
        self.assertTrue(TestParser.checkParser("( )","Error on line 1 col 1: (",224))

    def test_225(self):
        self.assertTrue(TestParser.checkParser("{ }","Error on line 1 col 1: {",225))

    def test_226(self):
        self.assertTrue(TestParser.checkParser(":=","Error on line 1 col 1: :=",226))

    def test_227(self):
        self.assertTrue(TestParser.checkParser("==","Error on line 1 col 1: ==",227))

    def test_228(self):
        self.assertTrue(TestParser.checkParser("!=","Error on line 1 col 1: !=",228))

    def test_229(self):
        self.assertTrue(TestParser.checkParser("<=","Error on line 1 col 1: <=",229))

    def test_230(self):
        self.assertTrue(TestParser.checkParser(">=","Error on line 1 col 1: >=",230))

    def test_231(self):
        self.assertTrue(TestParser.checkParser("5+3","Error on line 1 col 1: 5",231))

    def test_232(self):
        self.assertTrue(TestParser.checkParser("x = 10","Error on line 1 col 1: x",232))

    def test_233(self):
        self.assertTrue(TestParser.checkParser("for i := 0; i < 10; i++","Error on line 1 col 1: for",233))

    def test_234(self):
        self.assertTrue(TestParser.checkParser("foo.bar","Error on line 1 col 1: foo",234))

    def test_235(self):
        self.assertTrue(TestParser.checkParser("arr[0]","Error on line 1 col 1: arr",235))

    def test_236(self):
        self.assertTrue(TestParser.checkParser("12.e-5","Error on line 1 col 1: 12.e-5",236))

    def test_237(self):
        self.assertTrue(TestParser.checkParser("'c'","'",237))

    def test_238(self):
        self.assertTrue(TestParser.checkParser("void","Error on line 1 col 1: void",238))

    def test_239(self):
        self.assertTrue(TestParser.checkParser("package main","Error on line 1 col 1: package",239))

    def test_240(self):
        self.assertTrue(TestParser.checkParser("switch","Error on line 1 col 1: switch",240))

    def test_241(self):
        self.assertTrue(TestParser.checkParser("case","Error on line 1 col 1: case",241))

    def test_242(self):
        self.assertTrue(TestParser.checkParser("default","Error on line 1 col 1: default",242))

    def test_243(self):
        self.assertTrue(TestParser.checkParser("map[string]int","Error on line 1 col 1: map",243))

    def test_244(self):
        self.assertTrue(TestParser.checkParser("defer","Error on line 1 col 1: defer",244))

    def test_245(self):
        self.assertTrue(TestParser.checkParser("go","Error on line 1 col 1: go",245))

    def test_246(self):
        self.assertTrue(TestParser.checkParser("interface","Error on line 1 col 1: interface",246))

    def test_247(self):
        self.assertTrue(TestParser.checkParser("struct","Error on line 1 col 1: struct",247))

    def test_248(self):
        self.assertTrue(TestParser.checkParser("chan","Error on line 1 col 1: chan",248))

    def test_249(self):
        self.assertTrue(TestParser.checkParser("range","Error on line 1 col 1: range",249))

    def test_250(self):
        self.assertTrue(TestParser.checkParser("select","Error on line 1 col 1: select",250))

    def test_251(self):
        self.assertTrue(TestParser.checkParser("""
        func main() {
            var a int = 5
            var b float = 3.14
            if (a > b) {
                return "Greater"
            } else {
                return "Smaller"
            };
        }
    """, "successful", 251))

    def test_252(self):
        self.assertTrue(TestParser.checkParser("""
            var x int = 10;
            const PI float = 3.1415;
            var name string = "John Doe";
            var isActive bool = true;
    """, "Error on line 3 col 22: float", 252))

    def test_253(self):
        self.assertTrue(TestParser.checkParser("""
            if (x > 5) {
                y = x * 2;
            } else if (x == 5) {
                y = x + 10;
            } else {
                y = 0;
            }
    """, "Error on line 2 col 13: if", 253))

    def test_254(self):
        self.assertTrue(TestParser.checkParser("""
        for (i = 0; i < 10; i = i + 1) {
            print(i);
        }
    """, "Error on line 2 col 9: for", 254))

    def test_255(self):
        self.assertTrue(TestParser.checkParser("""
        func factorial(n int) int {
            if (n == 0) {
                return 1;
            }
            return n * factorial(n - 1);
        }
    """, "successful", 255))

    def test_256(self):
        self.assertTrue(TestParser.checkParser("""
        type Person struct {
            name string;
            age int;
            func (p Person) GetAge() int {
                return p.age;
            }
        }
        """, "Error on line 5 col 13: func", 256))

    def test_257(self):
        self.assertTrue(TestParser.checkParser("""
        var arr [5]int = [2][3]int{{1, 2, 3}, {4, 5, 6}};
        """, "successful", 257))

    def test_258(self):
        self.assertTrue(TestParser.checkParser("""

        func myFunc(a, b int, c string) int {
            var arr [5]int = [2][3]int{{1, 2, 3}, {4, 5, 6}}
        }
        
        """, "successful", 258))

    def test_259(self):
        self.assertTrue(TestParser.checkParser("""

        func myFunc(a, b int, c string) int{
            var arr = [2][3]int{{1, 2, 3}, {4, 5, 6}}
        };
        
        """, "successful", 259))

    def test_260(self):
        self.assertTrue(TestParser.checkParser("""

        func myFunc(a, b int, c string) string {
            var arr [5]int 
            return
        }
        
        """, "successful", 260))

    def test_261(self):
        self.assertTrue(TestParser.checkParser("""
        
        func myFunc(a, b int, c string) [2]int {
            var arr
        }
        
        """, "Error on line 4 col 20: ;", 261))

    def test_262(self):
        self.assertTrue(TestParser.checkParser("""
        continue;
        """, "Error on line 2 col 9: continue", 262))

    def test_263(self):
        self.assertTrue(TestParser.checkParser("""
        x == 10;
        """, "Error on line 2 col 9: x", 263))

    def test_264(self):
        self.assertTrue(TestParser.checkParser("""
        var name string "Hello";
        """, "Error on line 2 col 25: \"Hello\"", 264))

    def test_265(self):
        self.assertTrue(TestParser.checkParser("""
        var str = "This is an unclosed string
        """, "\"This is an unclosed string", 265))

    def test_266(self):
        self.assertTrue(TestParser.checkParser("""
        var str = "Hello\qWorld";
        """, "\"Hello\q", 266))

    def test_267(self):
        self.assertTrue(TestParser.checkParser("""
        /* This is an unclosed comment
        """, "Error on line 2 col 9: /", 267))

    def test_268(self):
        self.assertTrue(TestParser.checkParser("""

        type Outer struct {
            type Inner struct {
                value int;
                func (i Inner) GetValue() int {
                    return i.value;
                }
            }
            /**/
            inner Inner;
            func (o Outer) GetInnerValue() int {
                return o.inner.GetValue();
            }
            // hello
        }

        """, "Error on line 4 col 13: type", 268))

    def test_269(self):
        self.assertTrue(TestParser.checkParser("""
        func ComplexFunction(a int, b float, c string, d [5]int, e [4]float) [3][23]int {
            var result int;
            return result
        };
        """, "successful", 269))

    def test_270(self):
        self.assertTrue(TestParser.checkParser("""
        type ErrorStruct struct {
            name string
            age int;
            func (e ErrorStruct) GetName() string 
                return e.name;
            };
        }
        """, "Error on line 5 col 13: func", 270))

    def test_271(self):
        self.assertTrue(TestParser.checkParser("""
        type ErrorStruct struct {
            name string
            age int;
            func (e ErrorStruct) GetName() string 
                return e.name;
            };
        }""", "Error on line 5 col 13: func", 271))

    def test_272(self):
        self.assertTrue(TestParser.checkParser("""
        type ErrorStruct struct {
            name string
            age int;
            /*func (e ErrorStruct) GetName() string 
                return e.name;
            };
            */
        }
        """, "successful", 272))

    def test_273(self):
        self.assertTrue(TestParser.checkParser("""
        func Fibonacci(n int) int {
            if (n <= 1) {
                return n;
            }
            var a int = Fibonacci(n - 1) + Fibonacci(n - 2);
            return a;
        }
        """, "successful", 273))

    def test_274(self):
        self.assertTrue(TestParser.checkParser("""
        for (i = 0; i < 100; i = i + 1) {
            if (i % 2 == 0) {
                continue;
            } else if (i == 55) {
                break;
            }
            print(i);
        }
        """, "Error on line 2 col 9: for", 274))

    def test_275(self):
        self.assertTrue(TestParser.checkParser("""
        var unknownType myCustomType = 10;
        """, "successful", 275))

    def test_276(self):
        self.assertTrue(TestParser.checkParser("""
        var _variable$Name123 string = "Hello, World!";
        """, "$", 276))

    def test_277(self):
        self.assertTrue(TestParser.checkParser("""
        var result float = 10 / 0;
        """, "successful", 277))

    def test_278(self):
        self.assertTrue(TestParser.checkParser("""
        var a int = "string_value";
        """, "successful", 278))

    def test_279(self):
        self.assertTrue(TestParser.checkParser("""
        func NoReturn() int {
            return;
        }
        """, "successful", 279))

    def test_280(self):
        self.assertTrue(TestParser.checkParser("""
        func NoReturn() int {
            
        }
        """, "Error on line 4 col 9: }", 280))

    def test_281(self):
        self.assertTrue(TestParser.checkParser("""
        func NoReturn(a, b, c, d, e int, asd float, trh6h string) int {return;}
        """, "successful", 281))

    def test_282(self):
        self.assertTrue(TestParser.checkParser("""
        func NestedIf(x int) string {
            if (x > 0) {
                if (x > 10) {
                    return "Greater than 10"
                } else {
                    if (x == 5) {
                        return "Equal to 5"
                    } else {
                        return "Between 1 and 10"
                    }
                }
            } else {
                return "Negative"
            }
        }
        """, "successful", 282))

    def test_283(self):
        self.assertTrue(TestParser.checkParser("""
        func MissingBrace() int 
            return 10;
        """, "Error on line 2 col 33: ;", 283))

    def test_284(self):
        self.assertTrue(TestParser.checkParser("""
        func NoReturnValue() string {
        }
        """, "Error on line 3 col 9: }", 284))

    def test_285(self):
        self.assertTrue(TestParser.checkParser("""
        func UndefinedVariable() {
            x = 10;
        }
        """, "Error on line 3 col 15: =", 285))

    def test_286(self):
        self.assertTrue(TestParser.checkParser("""
        type InvalidStruct struct {
            name string;
            age unknownType;
        }
        """, "successful", 286))

    def test_287(self):
        self.assertTrue(TestParser.checkParser("""
        var str string = "Hello \q World!";
        """, "\"Hello \q", 287))

    def test_288(self):
        self.assertTrue(TestParser.checkParser("""
        /* This is an unclosed comment
        var x int = 10;
        """, "Error on line 2 col 9: /", 288))

    def test_289(self):
        self.assertTrue(TestParser.checkParser("""
        func InvalidParams(x int, y string z float) {
            return;
        }
        """, "Error on line 2 col 44: z", 289))

    def test_290(self):
        self.assertTrue(TestParser.checkParser("""
        type DuplicateField struct {
            name string;
            name int;
        }
        """, "successful", 290))

    def test_291(self):
        self.assertTrue(TestParser.checkParser("""
        var result = 10 === 10;
        """, "Error on line 2 col 27: =", 291))

    def test_292(self):
        self.assertTrue(TestParser.checkParser("""
        var specialVar = @#$%^&*();
        """, "@", 292))

    def test_293(self):
        self.assertTrue(TestParser.checkParser("""
        func Outer() {
            func Inner() {
                print("Inner function");
            }
            Inner();
        }
        """, "successful", 293))

    def test_294(self):
        self.assertTrue(TestParser.checkParser("""
        var arr [5]int = [1, 2, 3, 4, 5];
        """, "Error on line 2 col 28: ,", 294))

    def test_295(self):
        self.assertTrue(TestParser.checkParser("""
        
        """, "Error on line 3 col 9: <EOF>", 295))

    def test_296(self):
        self.assertTrue(TestParser.checkParser("""
        nil
        """, "Error on line 2 col 9: nil", 296))

    def test_297(self):
        self.assertTrue(TestParser.checkParser("""
        /* test
    */ a /* */
        """, "Error on line 3 col 8: a", 297))

    def test_298(self):
        self.assertTrue(TestParser.checkParser("""
        type Person struct {
            func (p Person) Greet() string {
                return "Hello, " + p.name
            }; c c;
            func (p Person) Greet() string {
                return "Hello, " + p.name
            } c c;                                                    
        }   
        """, "Error on line 3 col 13: func", 298))

    def test_299(self):
        self.assertTrue(TestParser.checkParser("""
        func (p Person) Greet() string {
            if (1) {return;}
            else if (1)
            {}
        };
        """, "Error on line 4 col 13: else", 299))

    def test_300(self):
        self.assertTrue(TestParser.checkParser("""
        type Person struct {
            /* func (p Person) Greet() string {
                return "Hello, " + p.name
            }
            */
            c c
            func (c c) Add(x, y int, b float) {return ;}  
            value int;                            
        }
        """, "Error on line 8 col 13: func", 300))