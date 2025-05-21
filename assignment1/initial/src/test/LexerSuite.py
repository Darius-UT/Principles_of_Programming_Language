import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
        
    def test_101(self):
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))

    def test_102(self):
        self.assertTrue(TestLexer.checkLexeme("if","if,<EOF>",102))

    def test_103(self):
        self.assertTrue(TestLexer.checkLexeme("+","+,<EOF>",103))

    def test_104(self):
        self.assertTrue(TestLexer.checkLexeme("[]","[,],<EOF>",104))

    def test_105(self):
        self.assertTrue(TestLexer.checkLexeme("_myVar","_myVar,<EOF>",105))

    def test_106(self):
        self.assertTrue(TestLexer.checkLexeme("12","12,<EOF>",106))

    def test_107(self):
        self.assertTrue(TestLexer.checkLexeme("0x1A","0x1A,<EOF>",107))

    def test_108(self):
        self.assertTrue(TestLexer.checkLexeme("3.14","3.14,<EOF>",108))

    def test_109(self):
        self.assertTrue(TestLexer.checkLexeme("\"hello\"","\"hello\",<EOF>",109))

    def test_110(self):
        self.assertTrue(TestLexer.checkLexeme("// comment","<EOF>",110))

    def test_111(self):
        self.assertTrue(TestLexer.checkLexeme("/* block comment */","<EOF>",111))

    def test_112(self):
        self.assertTrue(TestLexer.checkLexeme("^","ErrorToken ^",112))

    def test_113(self):
        self.assertTrue(TestLexer.checkLexeme("\"unterminated","Unclosed string: \"unterminated",113))

    def test_114(self):
        self.assertTrue(TestLexer.checkLexeme("\"illegal\\g\"","Illegal escape in string: \"illegal\\g",114))

    def test_115(self):
        self.assertTrue(TestLexer.checkLexeme("var","var,<EOF>",115))

    def test_116(self):
        self.assertTrue(TestLexer.checkLexeme("type","type,<EOF>",116))

    def test_117(self):
        self.assertTrue(TestLexer.checkLexeme("func","func,<EOF>",117))

    def test_118(self):
        self.assertTrue(TestLexer.checkLexeme("return","return,<EOF>",118))

    def test_119(self):
        self.assertTrue(TestLexer.checkLexeme("break","break,<EOF>",119))

    def test_120(self):
        self.assertTrue(TestLexer.checkLexeme("continue","continue,<EOF>",120))

    def test_121(self):
        self.assertTrue(TestLexer.checkLexeme("nil","nil,<EOF>",121))

    def test_122(self):
        self.assertTrue(TestLexer.checkLexeme("true","true,<EOF>",122))

    def test_123(self):
        self.assertTrue(TestLexer.checkLexeme("false","false,<EOF>",123))

    def test_124(self):
        self.assertTrue(TestLexer.checkLexeme("( )","(,),<EOF>",124))

    def test_125(self):
        self.assertTrue(TestLexer.checkLexeme("{ }","{,},<EOF>",125))

    def test_126(self):
        self.assertTrue(TestLexer.checkLexeme(":=",":=,<EOF>",126))

    def test_127(self):
        self.assertTrue(TestLexer.checkLexeme("==","==,<EOF>",127))

    def test_128(self):
        self.assertTrue(TestLexer.checkLexeme("!=","!=,<EOF>",128))

    def test_129(self):
        self.assertTrue(TestLexer.checkLexeme("<=","<=,<EOF>",129))

    def test_130(self):
        self.assertTrue(TestLexer.checkLexeme(">=",">=,<EOF>",130))

    def test_131(self):
        self.assertTrue(TestLexer.checkLexeme("5+3","5,+,3,<EOF>",131))

    def test_132(self):
        self.assertTrue(TestLexer.checkLexeme("x = 10","x,=,10,<EOF>",132))

    def test_133(self):
        self.assertTrue(TestLexer.checkLexeme("for i := 0; i < 10; i++","for,i,:=,0,;,i,<,10,;,i,+,+,<EOF>",133))

    def test_134(self):
        self.assertTrue(TestLexer.checkLexeme("foo.bar","foo,.,bar,<EOF>",134))

    def test_135(self):
        self.assertTrue(TestLexer.checkLexeme("arr[0]","arr,[,0,],<EOF>",135))

    def test_136(self):
        self.assertTrue(TestLexer.checkLexeme("12.e-5","12.e-5,<EOF>",136))

    def test_137(self):
        self.assertTrue(TestLexer.checkLexeme("'c'","ErrorToken '",137))

    def test_138(self):
        self.assertTrue(TestLexer.checkLexeme("void","void,<EOF>",138))

    def test_139(self):
        self.assertTrue(TestLexer.checkLexeme("package main","package,main,<EOF>",139))

    def test_140(self):
        self.assertTrue(TestLexer.checkLexeme("switch","switch,<EOF>",140))

    def test_141(self):
        self.assertTrue(TestLexer.checkLexeme("case","case,<EOF>",141))

    def test_142(self):
        self.assertTrue(TestLexer.checkLexeme("default","default,<EOF>",142))

    def test_143(self):
        self.assertTrue(TestLexer.checkLexeme("map[string]int","map,[,string,],int,<EOF>",143))

    def test_144(self):
        self.assertTrue(TestLexer.checkLexeme("defer","defer,<EOF>",144))

    def test_145(self):
        self.assertTrue(TestLexer.checkLexeme("go","go,<EOF>",145))

    def test_146(self):
        self.assertTrue(TestLexer.checkLexeme("interface","interface,<EOF>",146))

    def test_147(self):
        self.assertTrue(TestLexer.checkLexeme("struct","struct,<EOF>",147))

    def test_148(self):
        self.assertTrue(TestLexer.checkLexeme("chan","chan,<EOF>",148))

    def test_149(self):
        self.assertTrue(TestLexer.checkLexeme("range","range,<EOF>",149))

    def test_150(self):
        self.assertTrue(TestLexer.checkLexeme("select","select,<EOF>",150))

    def test_151(self):
        self.assertTrue(TestLexer.checkLexeme("""
        func main() {
            var a int = 5
            var b float = 3.14
            if (a > b) {
                return "Greater"
            } else {
                return "Smaller"
            };
        }
        """, "func,main,(,),{,var,a,int,=,5,;,var,b,float,=,3.14,;,if,(,a,>,b,),{,return,\"Greater\",;,},else,{,return,\"Smaller\",;,},;,},;,<EOF>", 151))

    def test_152(self):
        self.assertTrue(TestLexer.checkLexeme("""
            var x int = 10;
            const PI float = 3.1415;
            var name string = "John Doe";
            var isActive bool = true;
        """, "var,x,int,=,10,;,const,PI,float,=,3.1415,;,var,name,string,=,\"John Doe\",;,var,isActive,bool,=,true,;,<EOF>", 152))

    def test_153(self):
        self.assertTrue(TestLexer.checkLexeme("""
            if (x > 5) {
                y = x * 2;
            } else if (x == 5) {
                y = x + 10;
            } else {
                y = 0;
            }
        """, "if,(,x,>,5,),{,y,=,x,*,2,;,},else,if,(,x,==,5,),{,y,=,x,+,10,;,},else,{,y,=,0,;,},;,<EOF>", 153))

    def test_154(self):
        self.assertTrue(TestLexer.checkLexeme("""
        for (i = 0; i < 10; i = i + 1) {
            print(i);
        }
        """, "for,(,i,=,0,;,i,<,10,;,i,=,i,+,1,),{,print,(,i,),;,},;,<EOF>", 154))

    def test_155(self):
        self.assertTrue(TestLexer.checkLexeme("""
        func factorial(n int) int {
            if (n == 0) {
                return 1;
            }
            return n * factorial(n - 1);
        }
        """, "func,factorial,(,n,int,),int,{,if,(,n,==,0,),{,return,1,;,},;,return,n,*,factorial,(,n,-,1,),;,},;,<EOF>", 155))

    def test_156(self):
        self.assertTrue(TestLexer.checkLexeme("""
        type Person struct {
            name string;
            age int;
            func (p Person) GetAge() int {
                return p.age;
            }
        }
        """, "type,Person,struct,{,name,string,;,age,int,;,func,(,p,Person,),GetAge,(,),int,{,return,p,.,age,;,},;,},;,<EOF>", 156))

    def test_157(self):
        self.assertTrue(TestLexer.checkLexeme("""
        var arr [5]int = [1, 2, 3, 4, 5];
        """, "var,arr,[,5,],int,=,[,1,,,2,,,3,,,4,,,5,],;,<EOF>", 157))

    def test_158(self):
        self.assertTrue(TestLexer.checkLexeme("""
        var arr = [1, 2, 3, 4, 5];
        """, "var,arr,=,[,1,,,2,,,3,,,4,,,5,],;,<EOF>", 158))

    def test_159(self):
        self.assertTrue(TestLexer.checkLexeme("""
        var arr [5]int;
        """, "var,arr,[,5,],int,;,<EOF>", 159))

    def test_160(self):
        self.assertTrue(TestLexer.checkLexeme("""
        var arr;
        """, "var,arr,;,<EOF>", 160))

    def test_161(self):
        self.assertTrue(TestLexer.checkLexeme("""
        break;
        """, "break,;,<EOF>", 161))

    def test_162(self):
        self.assertTrue(TestLexer.checkLexeme("""
        continue;
        """, "continue,;,<EOF>", 162))

    def test_163(self):
        self.assertTrue(TestLexer.checkLexeme("""
        x == 10;
        """, "x,==,10,;,<EOF>", 163))

    def test_164(self):
        self.assertTrue(TestLexer.checkLexeme("""
        var name string "Hello";
        """, "var,name,string,\"Hello\",;,<EOF>", 164))

    def test_165(self):
        self.assertTrue(TestLexer.checkLexeme("""
        var str = "This is an unclosed string
        """, "var,str,=,Unclosed string: \"This is an unclosed string", 165))

    def test_166(self):
        self.assertTrue(TestLexer.checkLexeme("""
        var str = "Hello\qWorld";
        """, "var,str,=,Illegal escape in string: \"Hello\q", 166))

    def test_167(self):
        self.assertTrue(TestLexer.checkLexeme("""
        /* This is an unclosed comment
        """, "/,*,This,is,an,unclosed,comment,;,<EOF>", 167))

    def test_168(self):
        self.assertTrue(TestLexer.checkLexeme("""

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

        """, "type,Outer,struct,{,type,Inner,struct,{,value,int,;,func,(,i,Inner,),GetValue,(,),int,{,return,i,.,value,;,},;,},;,inner,Inner,;,func,(,o,Outer,),GetInnerValue,(,),int,{,return,o,.,inner,.,GetValue,(,),;,},;,},;,<EOF>", 168))

    def test_169(self):
        self.assertTrue(TestLexer.checkLexeme("""
        func ComplexFunction(a int, b float, c string, d [5]int, e [4]float) [3][23]int {
            var result int;
            return result
        };
        """, "func,ComplexFunction,(,a,int,,,b,float,,,c,string,,,d,[,5,],int,,,e,[,4,],float,),[,3,],[,23,],int,{,var,result,int,;,return,result,;,},;,<EOF>", 169))

    def test_170(self):
        self.assertTrue(TestLexer.checkLexeme("""
        type ErrorStruct struct {
            name string
            age int;
            func (e ErrorStruct) GetName() string 
                return e.name;
            };
        }
        """, "type,ErrorStruct,struct,{,name,string,;,age,int,;,func,(,e,ErrorStruct,),GetName,(,),string,;,return,e,.,name,;,},;,},;,<EOF>", 170))

    def test_171(self):
        self.assertTrue(TestLexer.checkLexeme("""
        type ErrorStruct struct {
            name string
            age int;
            func (e ErrorStruct) GetName() string 
                return e.name;
            };
        }""", "type,ErrorStruct,struct,{,name,string,;,age,int,;,func,(,e,ErrorStruct,),GetName,(,),string,;,return,e,.,name,;,},;,},<EOF>", 171))

    def test_172(self):
        self.assertTrue(TestLexer.checkLexeme("""
        type ErrorStruct struct {
            name string
            age int;
            /*func (e ErrorStruct) GetName() string 
                return e.name;
            };
            */
        }
        """, "type,ErrorStruct,struct,{,name,string,;,age,int,;,},;,<EOF>", 172))

    def test_173(self):
        self.assertTrue(TestLexer.checkLexeme("""
        func Fibonacci(n int) int {
            if (n <= 1) {
                return n;
            }
            var a int = Fibonacci(n - 1) + Fibonacci(n - 2);
            return a;
        }
        """, "func,Fibonacci,(,n,int,),int,{,if,(,n,<=,1,),{,return,n,;,},;,var,a,int,=,Fibonacci,(,n,-,1,),+,Fibonacci,(,n,-,2,),;,return,a,;,},;,<EOF>", 173))

    def test_174(self):
        self.assertTrue(TestLexer.checkLexeme("""
        for (i = 0; i < 100; i = i + 1) {
            if (i % 2 == 0) {
                continue;
            } else if (i == 55) {
                break;
            }
            print(i);
        }
        """, "for,(,i,=,0,;,i,<,100,;,i,=,i,+,1,),{,if,(,i,%,2,==,0,),{,continue,;,},else,if,(,i,==,55,),{,break,;,},;,print,(,i,),;,},;,<EOF>", 174))

    def test_175(self):
        self.assertTrue(TestLexer.checkLexeme("""
        var unknownType myCustomType = 10;
        """, "var,unknownType,myCustomType,=,10,;,<EOF>", 175))

    def test_176(self):
        self.assertTrue(TestLexer.checkLexeme("""
        var _variable$Name123 string = "Hello, World!";
        """, "var,_variable,ErrorToken $", 176))

    def test_177(self):
        self.assertTrue(TestLexer.checkLexeme("""
        var result float = 10 / 0;
        """, "var,result,float,=,10,/,0,;,<EOF>", 177))

    def test_178(self):
        self.assertTrue(TestLexer.checkLexeme("""
        var a int = "string_value";
        """, "var,a,int,=,\"string_value\",;,<EOF>", 178))

    def test_179(self):
        self.assertTrue(TestLexer.checkLexeme("""
        func NoReturn() int {
            return;
        }
        """, "func,NoReturn,(,),int,{,return,;,},;,<EOF>", 179))

    def test_180(self):
        self.assertTrue(TestLexer.checkLexeme("""
        func NoReturn() int {
            
        }
        """, "func,NoReturn,(,),int,{,},;,<EOF>", 180))

    def test_181(self):
        self.assertTrue(TestLexer.checkLexeme("""
        func NoReturn(a, b, c, d, e int, asd float, trh6h string) int {return;}
        """, "func,NoReturn,(,a,,,b,,,c,,,d,,,e,int,,,asd,float,,,trh6h,string,),int,{,return,;,},;,<EOF>", 181))

    def test_182(self):
        self.assertTrue(TestLexer.checkLexeme("""
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
        """, "func,NestedIf,(,x,int,),string,{,if,(,x,>,0,),{,if,(,x,>,10,),{,return,\"Greater than 10\",;,},else,{,if,(,x,==,5,),{,return,\"Equal to 5\",;,},else,{,return,\"Between 1 and 10\",;,},;,},;,},else,{,return,\"Negative\",;,},;,},;,<EOF>", 182))

    def test_183(self):
        self.assertTrue(TestLexer.checkLexeme("""
        func MissingBrace() int 
            return 10;
        """, "func,MissingBrace,(,),int,;,return,10,;,<EOF>", 183))

    def test_184(self):
        self.assertTrue(TestLexer.checkLexeme("""
        func NoReturnValue() string {
        }
        """, "func,NoReturnValue,(,),string,{,},;,<EOF>", 184))

    def test_185(self):
        self.assertTrue(TestLexer.checkLexeme("""
        func UndefinedVariable() {
            x = 10;
        }
        """, "func,UndefinedVariable,(,),{,x,=,10,;,},;,<EOF>", 185))

    def test_186(self):
        self.assertTrue(TestLexer.checkLexeme("""
        type InvalidStruct struct {
            name string;
            age unknownType;
        }
        """, "type,InvalidStruct,struct,{,name,string,;,age,unknownType,;,},;,<EOF>", 186))

    def test_187(self):
        self.assertTrue(TestLexer.checkLexeme("""
        var str string = "Hello \q World!";
        """, "var,str,string,=,Illegal escape in string: \"Hello \q", 187))

    def test_188(self):
        self.assertTrue(TestLexer.checkLexeme("""
        /* This is an unclosed comment
        var x int = 10;
        """, "/,*,This,is,an,unclosed,comment,;,var,x,int,=,10,;,<EOF>", 188))

    def test_189(self):
        self.assertTrue(TestLexer.checkLexeme("""
        func InvalidParams(x int, y string z float) {
            return;
        }
        """, "func,InvalidParams,(,x,int,,,y,string,z,float,),{,return,;,},;,<EOF>", 189))

    def test_190(self):
        self.assertTrue(TestLexer.checkLexeme("""
        type DuplicateField struct {
            name string;
            name int;
        }
        """, "type,DuplicateField,struct,{,name,string,;,name,int,;,},;,<EOF>", 190))

    def test_191(self):
        self.assertTrue(TestLexer.checkLexeme("""
        var result = 10 === 10;
        """, "var,result,=,10,==,=,10,;,<EOF>", 191))

    def test_192(self):
        self.assertTrue(TestLexer.checkLexeme("""
        var specialVar = @#$%^&*();
        """, "var,specialVar,=,ErrorToken @", 192))

    def test_193(self):
        self.assertTrue(TestLexer.checkLexeme("""
        func Outer() {
            func Inner() {
                print("Inner function");
            }
            Inner();
        }
        """, "func,Outer,(,),{,func,Inner,(,),{,print,(,\"Inner function\",),;,},;,Inner,(,),;,},;,<EOF>", 193))

    def test_194(self):
        self.assertTrue(TestLexer.checkLexeme("""
        var arr [5]int = [1, 2, 3, 4, 5];
        """, "var,arr,[,5,],int,=,[,1,,,2,,,3,,,4,,,5,],;,<EOF>", 194))

    def test_195(self):
        self.assertTrue(TestLexer.checkLexeme("""
        `
        """, "ErrorToken `", 195))

    def test_196(self):
        self.assertTrue(TestLexer.checkLexeme("""
        nil
        """, "nil,;,<EOF>", 196))

    def test_197(self):
        self.assertTrue(TestLexer.checkLexeme("""
        /* test
    */ a /* */
        """, "a,;,<EOF>", 197))

    def test_198(self):
        self.assertTrue(TestLexer.checkLexeme("""
        type Person struct {
            func (p Person) Greet() string {
                return "Hello, " + p.name
            }; c c;
            func (p Person) Greet() string {
                return "Hello, " + p.name
            } c c;                                                    
        }   
        """, "type,Person,struct,{,func,(,p,Person,),Greet,(,),string,{,return,\"Hello, \",+,p,.,name,;,},;,c,c,;,func,(,p,Person,),Greet,(,),string,{,return,\"Hello, \",+,p,.,name,;,},c,c,;,},;,<EOF>", 198))

    def test_199(self):
        self.assertTrue(TestLexer.checkLexeme("""
        func (p Person) Greet() string {
            if (1) {return;}
            else if (1)
            {}
        };
        """, "func,(,p,Person,),Greet,(,),string,{,if,(,1,),{,return,;,},;,else,if,(,1,),;,{,},;,},;,<EOF>", 199))

    def test_200(self):
        self.assertTrue(TestLexer.checkLexeme("""
        type Person struct {
            /* func (p Person) Greet() string {
                return "Hello, " + p.name
            }
            */
            c c
            func (c c) Add(x, y int, b float) {return ;}  
            value int;                            
        }
        """, "type,Person,struct,{,c,c,;,func,(,c,c,),Add,(,x,,,y,int,,,b,float,),{,return,;,},;,value,int,;,},;,<EOF>", 200))

