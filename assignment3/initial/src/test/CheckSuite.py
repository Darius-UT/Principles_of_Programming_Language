import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_001(self):
        input = """
var HoangPhuc = 1;
var HoangPhuc = 2;
        """
        expect = "Redeclared Variable: HoangPhuc\n"
        self.assertTrue(TestChecker.test(input, expect, 1))

    def test_002(self):
        input = """
var HoangPhuc = 1;
const HoangPhuc = 2;
        """
        expect = "Redeclared Constant: HoangPhuc\n"
        self.assertTrue(TestChecker.test(input, expect, 2))

    def test_003(self):
        input = """
const HoangPhuc = 1;
var HoangPhuc = 2;
        """
        expect = "Redeclared Variable: HoangPhuc\n"
        self.assertTrue(TestChecker.test(input, expect, 3))

    def test_004(self):
        input = """
const HoangPhuc = 1;
func HoangPhuc () {return;}
        """
        expect = "Redeclared Function: HoangPhuc\n"
        self.assertTrue(TestChecker.test(input, expect, 4))

    def test_005(self):
        input = """
func HoangPhuc () {return;}
var HoangPhuc = 1;
        """
        expect = "Redeclared Variable: HoangPhuc\n"
        self.assertTrue(TestChecker.test(input, expect, 5))

    def test_006(self):
        input = """
var getInt = 1;
        """
        expect = "Redeclared Variable: getInt\n"
        self.assertTrue(TestChecker.test(input, expect, 6))

    def test_007(self):
        input = """
type  HoangPhuc struct {
    HoangPhuc int;
}
type TIEN struct {
    HoangPhuc string;
    TIEN int;
    TIEN float;
}
        """
        expect = "Redeclared Field: TIEN\n"
        self.assertTrue(TestChecker.test(input, expect, 7))

    def test_008(self):
        input = """
func (v TIEN) putIntLn () {return;}
func (v TIEN) getInt () {return;}
func (v TIEN) getInt () {return;}
type TIEN struct {
    HoangPhuc int;
}
        """
        expect = "Redeclared Method: getInt\n"
        self.assertTrue(TestChecker.test(input, expect, 8))

    def test_009(self):
        input = """
type HoangPhuc interface {
    HoangPhuc ();
    HoangPhuc (a int);
}
        """
        expect = "Redeclared Prototype: HoangPhuc\n"
        self.assertTrue(TestChecker.test(input, expect, 9))

    def test_010(self):
        input = """
func HoangPhuc (a, a int) {return;}
        """
        expect = "Redeclared Parameter: a\n"
        self.assertTrue(TestChecker.test(input, expect, 10))

    def test_011(self):
        input = """
func HoangPhuc (b int) {
    var b = 1;
    var a = 1;
    const a = 1;
}
        """
        expect = "Redeclared Constant: a\n"
        self.assertTrue(TestChecker.test(input, expect, 11))

    def test_012(self):
        input = """
func HoangPhuc (b int) {
    for var a = 1; a < 1; a += 1 {
        const a = 2;
    }
}
        """
        expect = "Redeclared Constant: a\n"
        self.assertTrue(TestChecker.test(input, expect, 12))

    def test_013(self):
        input = """
var a = 1;
var b = a;
var c = d;
        """
        expect = "Undeclared Identifier: d\n"
        self.assertTrue(TestChecker.test(input, expect, 13))

    def test_014(self):
        input = """
func HoangPhuc () int {return 1;}

func foo () {
    var b = HoangPhuc();
    foo_hoangphuc();
    return;
}
        """
        expect = "Undeclared Function: foo_hoangphuc\n"
        self.assertTrue(TestChecker.test(input, expect, 14))

    def test_015(self):
        input = """
type TIEN struct {
    HoangPhuc int;
}

func (v TIEN) getInt () {
    const c = v.HoangPhuc;
    var d = v.tien;
}
        """
        expect = "Undeclared Field: tien\n"
        self.assertTrue(TestChecker.test(input, expect, 15))

    def test_016(self):
        input = """
type TIEN struct {
    HoangPhuc int;
}

func (v TIEN) getInt () {
    v.getInt ();
    v.putInt ();
}
        """
        expect = "Undeclared Method: putInt\n"
        self.assertTrue(TestChecker.test(input, expect, 16))

    def test_017(self):
        input = """
type TIEN struct {HoangPhuc int;}
type TIEN struct {v int;}
        """
        expect = "Redeclared Type: TIEN\n"
        self.assertTrue(TestChecker.test(input, expect, 17))

    def test_018(self):
        input = """
type TIEN interface {foo();}
type TIEN interface {foo();}
        """
        expect = "Redeclared Type: TIEN\n"
        self.assertTrue(TestChecker.test(input, expect, 18))

    def test_019(self):
        input = """
type TIEN struct {a int;}
type VO struct {a int;}
type TIEN interface {foo();}
        """
        expect = "Redeclared Type: TIEN\n"
        self.assertTrue(TestChecker.test(input, expect, 19))

    def test_020(self):
        input = """
func putInt() {return;}
        """
        expect = "Redeclared Function: putInt\n"
        self.assertTrue(TestChecker.test(input, expect, 20))

    def test_021(self):
        input = """
    type PHUC struct {HoangPhuc int;}
    func (v PHUC) foo (v int) {return;}
    func foo () {return;}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 21))

    def test_022(self):
        input = """
    func (v PHUC) foo (a, b int) {
        var a = 1;
    }

    type PHUC struct {
        HoangPhuc int;
    }

    type Hoang struct {
        HoangPhuc int;
    }

    func (v Hoang) foo (a, b int) {
        var a = 1;
    }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 22))

    def test_023(self):
        input = """
    func foo () {
        const a = 1;
        for a, b := range [3]int {1, 2, 3} {
            var d = 1;
        }
    }
        """
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input, expect, 23))

    def test_024(self):
        input = """
    var a = foo();
    func foo () int {
        var a =  koo();
        var c = getInt();
        putInt(c);
        putIntLn(c);
        return 1;
    }
    var d = foo();
    func koo () int {
        var a =  foo ();
        return 1;
    }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 24))

    def test_025(self):
        input = """
    var a = d;
    func foo () {
        const b = 1;
        for a, c := range [3]int{1, 2, 3} {
            var d = c;
        }
        var d = a;
        var a = 1;
    }
    var d = a;
        """
        expect = "Undeclared Identifier: d\n"
        self.assertTrue(TestChecker.test(input, expect, 25))

    def test_026(self):
        input = """
    var v PHUC;
    const b = v.b;        
    type PHUC struct {
        a int;
        b int;
        c int;
    }
    const a = v.a;
    const e = v.e;
        """
        expect = "Undeclared Field: e\n"
        self.assertTrue(TestChecker.test(input, expect, 26))

    def test_027(self):
        input = """
    var v PHUC;

    func foo ()  {
        var x = v;
        const a = x.a;
        const e = x.e;
    }
        
    type PHUC struct {
        a int;
        b int;
        c int;
    }
        """
        expect = "Undeclared Field: e\n"
        self.assertTrue(TestChecker.test(input, expect, 27))

    def test_028(self):
        input = """
    var v PHUC;        
    type PHUC struct {
        a int;
        s Hoang
    }
    type Hoang struct {
        d float
        e float
    }
    const my = v.s.d
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 28))

    def test_029(self):
        input = """
    var a = foo();
    func foo () int {
        var a =  koo();
        var c = getInt();
        putInt(c);
        putIntLn(c);
        return 1;
    }
    var d = foo();
    func koo () int {
        var a =  foo ();
        return 1;
    }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 29))

    def test_030(self):
        input = """
    const a = 2;
    func foo () {
        const a = 1;
        for var a = 1; a < 1; b += 2 {
            const b = 1;
        }
    }
        """
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input, expect, 30))

    def test_031(self):
        input = """
    func (v PHUC) foo (a, b int) {
        const v = 1;
        const a = 1;
    }

    type PHUC struct {
        HoangPhuc int;
    }

    func (v Hoang) foo () {
        const a = 1;
    }

    type Hoang struct {
        HoangPhuc int;
    }

    func (v Hoang) foo (a, b int) {
        const a = 1;
    }
    """
        expect = "Redeclared Method: foo\n"
        self.assertTrue(TestChecker.test(input, expect, 31))

    def test_032(self):
        input = """
    const a = 2;
    func foo () {
        const a = 1;
        for a < 1 {
            const a = 1;
            for a < 1 {
                const a = 1;
                const b = 1;
            }
            const b = 1;
            var a = 1;
        }
    }
    """
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input, expect, 32))

    def test_033(self):
        input = """
    var v PHUC;
    const b = v.foo();        
    type PHUC struct {
        a int;
    } 
    func (v PHUC) foo() int {return 1;}
    func (v PHUC) koo() int {return 1;}
    const c = v.koo();  
    const d = v.zoo();
    """
        expect = "Undeclared Method: zoo\n"
        self.assertTrue(TestChecker.test(input, expect, 33))

    def test_034(self):
        input = """
    var v PHUC;      
    type PHUC struct {
        a int;
    } 
    type Hoang interface {
        foo() int;
    }

    func (v PHUC) foo() int {return 1;}
    func (b PHUC) koo() {b.koo();}
    func foo() {
        var x Hoang;  
        const b = x.foo(); 
        x.koo(); 
    }
    """
        expect = "Undeclared Method: koo\n"
        self.assertTrue(TestChecker.test(input, expect, 34))

    def test_035(self):
        input = """
    const a = 2;
    func foo () {
        const a = 1;
        for a < 1 {
            const a = 1;
            for a < 1 {
                const a = 1;
                const b = 1;
            }
            const b = 1;
            var a = 1;
        }
    }
    """
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input, expect, 35))

    def test_036(self):
        input = """
        type Phuc interface {foo();}
        type Phuc interface {foo();}
        """
        expect = "Redeclared Type: Phuc\n"
        self.assertTrue(TestChecker.test(input, expect, 36))

    def test_037(self):
        input = """
        func foo(){
            var v int;
            const x = v;
            var k float = x;
            var y boolean = x;
        }
        """
        expect = "Type Mismatch: VarDecl(y,BoolType,Id(x))\n"
        self.assertTrue(TestChecker.test(input, expect, 37))

    def test_038(self):
        input = """
        type Phuc struct {
            v int;
        }
        var v Phuc;
        func foo() {
            for 1 {
                var a int = 1.2;
            }
        }
        """
        expect = "Type Mismatch: For(IntLiteral(1),Block([VarDecl(a,IntType,FloatLiteral(1.2))]))\n"
        self.assertTrue(TestChecker.test(input, expect, 38))

    def test_039(self):
        input = """
        var a [2][3] int;
        var b = a[1];
        var c [2] int = b;
        var d [1] string = b;
        """
        expect = "Type Mismatch: VarDecl(c,ArrayType(IntType,[IntLiteral(2)]),Id(b))\n"
        self.assertTrue(TestChecker.test(input, expect, 39))

    def test_040(self):
        input = """
        var a int = 1 % 2;
        var b int = 1 % 2.0;
        """
        expect = "Type Mismatch: BinaryOp(IntLiteral(1),%,FloatLiteral(2.0))\n"
        self.assertTrue(TestChecker.test(input, expect, 40))

    def test_041(self):
        input = """
        func foo() int {return 1;}
        func HoangPhuc() int {
            return HoangPhuc();
            foo();
        }
        """
        expect = "Type Mismatch: FuncCall(foo,[])\n"
        self.assertTrue(TestChecker.test(input, expect, 41))

    def test_042(self):
        input = """
        var v int = 1.2;
        """
        expect = "Type Mismatch: VarDecl(v,IntType,FloatLiteral(1.2))\n"
        self.assertTrue(TestChecker.test(input, expect, 42))

    def test_043(self):
        input = """
        type S1 struct {HoangPhuc int;}
        type S2 struct {HoangPhuc int;}

        var v S1;
        const x = v;
        var z S1 = x;
        var k S2 = x;
        """
        expect = "Type Mismatch: VarDecl(k,Id(S2),Id(x))\n"
        self.assertTrue(TestChecker.test(input, expect, 43))

    def test_044(self):
        input = """
        type S1 struct {HoangPhuc1 int;}
        type S2 struct {HoangPhuc int;}
        type I1 interface {HoangPhuc();}
        type I2 interface {HoangPhuc();}

        func (s S1) HoangPhuc() {return;}

        var a S1;
        var b S2;
        var c I1 = a;
        var d I2 = b;
        """
        expect = "Type Mismatch: VarDecl(d,Id(I2),Id(b))\n"
        self.assertTrue(TestChecker.test(input, expect, 44))

    def test_045(self):
        input = """
        type I1 interface {HoangPhuc();}
        type I2 interface {HoangPhuc();}

        var v I1;
        const x = v;
        var z I1 = x;
        var k I2 = x;
        """
        expect = "Type Mismatch: VarDecl(k,Id(I2),Id(x))\n"
        self.assertTrue(TestChecker.test(input, expect, 45))

    def test_046(self):
        input = """
        type I1 interface {HoangPhuc();}
        type I2 interface {HoangPhuc();}

        var v I1;
        const x = v;
        var z I1 = x;
        var k I2 = x;
        """
        expect = "Type Mismatch: VarDecl(k,Id(I2),Id(x))\n"
        self.assertTrue(TestChecker.test(input, expect, 46))

    def test_047(self):
        input = """
        type S1 struct {HoangPhuc1 int;}
        type S2 struct {HoangPhuc int;}
        type I1 interface {HoangPhuc() S1;}
        type I2 interface {HoangPhuc() S2;}

        func (s S1) HoangPhuc() S1 {return s;}

        var a S1;
        var c I1 = a;
        var d I2 = a;
        """
        expect = "Type Mismatch: VarDecl(d,Id(I2),Id(a))\n"
        self.assertTrue(TestChecker.test(input, expect, 47))

    def test_048(self):
        input = """
        type Phuc interface {foo();}
        type Phuc interface {foo();}
        """
        expect = "Redeclared Type: Phuc\n"
        self.assertTrue(TestChecker.test(input, expect, 48))

    def test_049(self):
        input = """
        func foo(){
            var v int;
            const x = v;
            var k float = x;
            var y boolean = x;
        }
        """
        expect = "Type Mismatch: VarDecl(y,BoolType,Id(x))\n"
        self.assertTrue(TestChecker.test(input, expect, 49))

    def test_050(self):
        input = """
        type Phuc struct {
            v int;
        }
        var v Phuc;
        func foo() {
            for 1 {
                var a int = 1.2;
            }
        }
        """
        expect = "Type Mismatch: For(IntLiteral(1),Block([VarDecl(a,IntType,FloatLiteral(1.2))]))\n"
        self.assertTrue(TestChecker.test(input, expect, 50))

    def test_051(self):
        input = """
        var a [2][3] int;
        var b = a[1];
        var c [2] int = b;
        var d [1] string = b;
        """
        expect = "Type Mismatch: VarDecl(c,ArrayType(IntType,[IntLiteral(2)]),Id(b))\n"
        self.assertTrue(TestChecker.test(input, expect, 51))

    def test_052(self):
        input = """
        var a int = 1 % 2;
        var b int = 1 % 2.0;
        """
        expect = "Type Mismatch: BinaryOp(IntLiteral(1),%,FloatLiteral(2.0))\n"
        self.assertTrue(TestChecker.test(input, expect, 52))

    def test_053(self):
        input = """
        func foo() int {return 1;}
        func HoangPhuc() int {
            return HoangPhuc();
            foo();
        }
        """
        expect = "Type Mismatch: FuncCall(foo,[])\n"
        self.assertTrue(TestChecker.test(input, expect, 53))

    def test_054(self):
        input = """
        var v int = 1.2;
        """
        expect = "Type Mismatch: VarDecl(v,IntType,FloatLiteral(1.2))\n"
        self.assertTrue(TestChecker.test(input, expect, 54))

    def test_055(self):
        input = """
        type S1 struct {HoangPhuc1 int;}
        type S2 struct {HoangPhuc int;}

        var v S1;
        const x = v;
        var z S1 = x;
        var k S2 = x;
        """
        expect = "Type Mismatch: VarDecl(k,Id(S2),Id(x))\n"
        self.assertTrue(TestChecker.test(input, expect, 55))

    def test_056(self):
        input = """
        type S1 struct {HoangPhuc1 int;}
        type S2 struct {HoangPhuc int;}
        type I1 interface {HoangPhuc();}
        type I2 interface {HoangPhuc();}

        func (s S1) HoangPhuc() {return;}

        var a S1;
        var b S2;
        var c I1 = a;
        var d I2 = b;
        """
        expect = "Type Mismatch: VarDecl(d,Id(I2),Id(b))\n"
        self.assertTrue(TestChecker.test(input, expect, 56))

    def test_057(self):
        input = """
        type I1 interface {HoangPhuc();}
        type I2 interface {HoangPhuc();}

        var v I1;
        const x = v;
        var z I1 = x;
        var k I2 = x;
        """
        expect = "Type Mismatch: VarDecl(k,Id(I2),Id(x))\n"
        self.assertTrue(TestChecker.test(input, expect, 57))

    def test_058(self):
        input = """
        type S1 struct {HoangPhuc1 int;}
        type I1 interface {HoangPhuc() S1;}
        type I2 interface {HoangPhuc() S2;}

        func (s S1) HoangPhuc() S1 {return s;}

        var a S1;
        var c I1 = a;
        var d I2 = a;
        """
        expect = "Type Mismatch: VarDecl(d,Id(I2),Id(a))\n"
        self.assertTrue(TestChecker.test(input, expect, 58))

    def test_059(self):
        input = """
        type S1 struct {HoangPhuc int;}
        type I1 interface {HoangPhuc() S1;}
        type I2 interface {HoangPhuc() S2;}

        func (s S1) HoangPhuc() S1 {return s;}

        var a S1;
        var c I1 = a;
        var d I2 = a;
        """
        expect = "Redeclared Method: HoangPhuc\n"
        self.assertTrue(TestChecker.test(input, expect, 59))

    def test_060(self):
        input = """
var HoangPhuc = 1;
var HoangPhuc = 2;
        """
        expect = "Redeclared Variable: HoangPhuc\n"
        self.assertTrue(TestChecker.test(input, expect, 60))

    def test_061(self):
        input = """
var HoangPhuc = 1;
const HoangPhuc = 2;
        """
        expect = "Redeclared Constant: HoangPhuc\n"
        self.assertTrue(TestChecker.test(input, expect, 61))

    def test_062(self):
        input = """
const HoangPhuc = 1;
var HoangPhuc = 2;
        """
        expect = "Redeclared Variable: HoangPhuc\n"
        self.assertTrue(TestChecker.test(input, expect, 62))

    def test_063(self):
        input = """
const HoangPhuc = 1;
func HoangPhuc () {return;}
        """
        expect = "Redeclared Function: HoangPhuc\n"
        self.assertTrue(TestChecker.test(input, expect, 63))

    def test_064(self):
        input = """
func HoangPhuc () {return;}
var HoangPhuc = 1;
        """
        expect = "Redeclared Variable: HoangPhuc\n"
        self.assertTrue(TestChecker.test(input, expect, 64))

    def test_065(self):
        input = """
var getInt = 1;
        """
        expect = "Redeclared Variable: getInt\n"
        self.assertTrue(TestChecker.test(input, expect, 65))

    def test_066(self):
        input = """
type  HoangPhuc struct {
    HoangPhuc int;
}
type TIEN struct {
    HoangPhuc string;
    TIEN int;
    TIEN float;
}
        """
        expect = "Redeclared Field: TIEN\n"
        self.assertTrue(TestChecker.test(input, expect, 66))

    def test_067(self):
        input = """
func (v TIEN) putIntLn () {return;}
func (v TIEN) getInt () {return;}
func (v TIEN) getInt () {return;}
type TIEN struct {
    HoangPhuc int;
}
        """
        expect = "Redeclared Method: getInt\n"
        self.assertTrue(TestChecker.test(input, expect, 67))

    def test_068(self):
        input = """
type HoangPhuc interface {
    HoangPhuc ();
    HoangPhuc (a int);
}
        """
        expect = "Redeclared Prototype: HoangPhuc\n"
        self.assertTrue(TestChecker.test(input, expect, 68))

    def test_069(self):
        input = """
func HoangPhuc (a, a int) {return;}
        """
        expect = "Redeclared Parameter: a\n"
        self.assertTrue(TestChecker.test(input, expect, 69))

    def test_070(self):
        input = """
func HoangPhuc (b int) {
    var b = 1;
    var a = 1;
    const a = 1;
}
        """
        expect = "Redeclared Constant: a\n"
        self.assertTrue(TestChecker.test(input, expect, 70))

    def test_071(self):
        input = """
func HoangPhuc (b int) {
    for var a = 1; a < 1; a += 1 {
        const a = 2;
    }
}
        """
        expect = "Redeclared Constant: a\n"
        self.assertTrue(TestChecker.test(input, expect, 71))

    def test_072(self):
        input = """
var a = 1;
var b = a;
var c = d;
        """
        expect = "Undeclared Identifier: d\n"
        self.assertTrue(TestChecker.test(input, expect, 72))

    def test_073(self):
        input = """
func HoangPhuc () int {return 1;}

func foo () {
    var b = HoangPhuc();
    foo_hoangphuc();
    return;
}
        """
        expect = "Undeclared Function: foo_hoangphuc\n"
        self.assertTrue(TestChecker.test(input, expect, 73))

    def test_074(self):
        input = """
type TIEN struct {
    HoangPhuc int;
}

func (v TIEN) getInt () {
    const c = v.HoangPhuc;
    var d = v.tien;
}
        """
        expect = "Undeclared Field: tien\n"
        self.assertTrue(TestChecker.test(input, expect, 74))

    def test_075(self):
        input = """
type TIEN struct {
    HoangPhuc int;
}

func (v TIEN) getInt () {
    v.getInt ();
    v.putInt ();
}
        """
        expect = "Undeclared Method: putInt\n"
        self.assertTrue(TestChecker.test(input, expect, 75))

    def test_076(self):
        input = """
type TIEN struct {HoangPhuc int;}
type TIEN struct {v int;}
        """
        expect = "Redeclared Type: TIEN\n"
        self.assertTrue(TestChecker.test(input, expect, 76))

    def test_077(self):
        input = """
type TIEN interface {foo();}
type TIEN interface {foo();}
        """
        expect = "Redeclared Type: TIEN\n"
        self.assertTrue(TestChecker.test(input, expect, 77))

    def test_078(self):
        input = """
type TIEN struct {a int;}
type VO struct {a int;}
type TIEN interface {foo();}
        """
        expect = "Redeclared Type: TIEN\n"
        self.assertTrue(TestChecker.test(input, expect, 78))

    def test_079(self):
        input = """
func putInt() {return;}
        """
        expect = "Redeclared Function: putInt\n"
        self.assertTrue(TestChecker.test(input, expect, 79))

    def test_080(self):
        input = """
    type PHUC struct {HoangPhuc int;}
    func (v PHUC) foo (v int) {return;}
    func foo () {return;}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 80))

    def test_081(self):
        input = """
    func (v PHUC) foo (a, b int) {
        var a = 1;
    }

    type PHUC struct {
        HoangPhuc int;
    }

    type Hoang struct {
        HoangPhuc int;
    }

    func (v Hoang) foo (a, b int) {
        var a = 1;
    }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 81))

    def test_082(self):
        input = """
    func foo () {
        const a = 1;
        for a, b := range [3]int {1, 2, 3} {
            break;
        }
    }
        """
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input, expect, 82))

    def test_083(self):
        input = """
    var a = foo();
    func foo () int {
        var a =  koo();
        var c = getInt();
        putInt(c);
        putIntLn(c);
        return 1;
    }
    var d = foo();
    func koo () int {
        var a =  foo ();
        return 1;
    }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 83))

    def test_084(self):
        input = """
    var a = d;
    func foo () {
        const b = 1;
        for a, c := range [3]int{1, 2, 3} {
            var d = c;
        }
        var d = a;
        var a = 1;
    }
    var d = a;
        """
        expect = "Undeclared Identifier: d\n"
        self.assertTrue(TestChecker.test(input, expect, 84))

    def test_085(self):
        input = """
    var v PHUC;
    const b = v.b;        
    type PHUC struct {
        a int;
        b int;
        c int;
    }
    const a = v.a;
    const e = v.e;
        """
        expect = "Undeclared Field: e\n"
        self.assertTrue(TestChecker.test(input, expect, 85))

    def test_086(self):
        input = """
    var v PHUC;

    func foo ()  {
        var x = v;
        const a = x.a;
        const e = x.e;
    }
        
    type PHUC struct {
        a int;
        b int;
        c int;
    }
        """
        expect = "Undeclared Field: e\n"
        self.assertTrue(TestChecker.test(input, expect, 86))

    def test_087(self):
        input = """
    var v PHUC;        
    type PHUC struct {
        a int;
        s Hoang
    }
    type Hoang struct {
        d float
        e float
    }
    const my = v.s.d
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 87))

    def test_088(self):
        input = """
    var a = foo();
    func foo () int {
        var a =  koo();
        var c = getInt();
        putInt(c);
        putIntLn(c);
        return 1;
    }
    var d = foo();
    func koo () int {
        var a =  foo ();
        return 1;
    }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 88))

    def test_089(self):
        input = """
    const a = 2;
    func foo () {
        const a = 1;
        for var a = 1; a < 1; b += 2 {
            const b = 1;
        }
    }
        """
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input, expect, 89))

    def test_090(self):
        input = """
    func (v PHUC) foo (a, b int) {
        const v = 1;
        const a = 1;
    }

    type PHUC struct {
        HoangPhuc int;
    }

    func (v Hoang) foo () {
        const a = 1;
    }

    type Hoang struct {
        HoangPhuc int;
    }

    func (v Hoang) foo (a, b int) {
        const a = 1;
    }
    """
        expect = "Redeclared Method: foo\n"
        self.assertTrue(TestChecker.test(input, expect, 90))

    def test_091(self):
        input = """
    const a = 2;
    func foo () {
        const a = 1;
        for a < 1 {
            const a = 1;
            for a < 1 {
                const a = 1;
                const b = 1;
            }
            const b = 1;
            var a = 1;
        }
    }
    """
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input, expect, 91))

    def test_092(self):
        input = """
    var v PHUC;
    const b = v.foo();        
    type PHUC struct {
        a int;
    } 
    func (v PHUC) foo() int {return 1;}
    func (v PHUC) koo() int {return 1;}
    const c = v.koo();  
    const d = v.zoo();
    """
        expect = "Undeclared Method: zoo\n"
        self.assertTrue(TestChecker.test(input, expect, 92))

    def test_093(self):
        input = """
    var v PHUC;      
    type PHUC struct {
        a int;
    } 
    type Hoang interface {
        foo() int;
    }

    func (v PHUC) foo() int {return 1;}
    func (b PHUC) koo() {b.koo();}
    func foo() {
        var x Hoang;  
        const b = x.foo(); 
        x.koo(); 
    }
    """
        expect = "Undeclared Method: koo\n"
        self.assertTrue(TestChecker.test(input, expect, 93))

    def test_094(self):
        input = """
    const a = 2;
    func foo () {
        const a = 1;
        for a < 1 {
            const a = 1;
            for a < 1 {
                const a = 1;
                const b = 1;
            }
            const b = 1;
            var a = 1;
        }
    }
    """
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input, expect, 94))

    def test_095(self):
        input = """
        type Phuc interface {foo();}
        type Phuc interface {foo();}
        """
        expect = "Redeclared Type: Phuc\n"
        self.assertTrue(TestChecker.test(input, expect, 95))

    def test_096(self):
        input = """
        func foo(){
            var v int;
            const x = v;
            var k float = x;
            var y boolean = x;
        }
        """
        expect = "Type Mismatch: VarDecl(y,BoolType,Id(x))\n"
        self.assertTrue(TestChecker.test(input, expect, 96))

    def test_097(self):
        input = """
        type Phuc struct {
            v int;
        }
        var v Phuc;
        func foo() {
            for 1 {
                var a int = 1.2;
            }
        }
        """
        expect = "Type Mismatch: For(IntLiteral(1),Block([VarDecl(a,IntType,FloatLiteral(1.2))]))\n"
        self.assertTrue(TestChecker.test(input, expect, 97))

    def test_098(self):
        input = """
        var a [2][3] int;
        var b = a[1];
        var c [2] int = b;
        var d [1] string = b;
        """
        expect = "Type Mismatch: VarDecl(c,ArrayType(IntType,[IntLiteral(2)]),Id(b))\n"
        self.assertTrue(TestChecker.test(input, expect, 98))

    def test_099(self):
        input = """
        var a int = 1 % 2;
        var b int = 1 % 2.0;
        """
        expect = "Type Mismatch: BinaryOp(IntLiteral(1),%,FloatLiteral(2.0))\n"
        self.assertTrue(TestChecker.test(input, expect, 99))

    def test_100(self):
        input = """
        func foo() int {return 1;}
        func HoangPhuc() int {
            return HoangPhuc();
            foo();
        }
        """
        expect = "Type Mismatch: FuncCall(foo,[])\n"
        self.assertTrue(TestChecker.test(input, expect, 100))