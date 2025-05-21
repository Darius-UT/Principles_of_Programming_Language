""" 
MSSV: 2212629
Họ tên: Nguyễn Lê Hoàng Phúc
"""

import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_001(self):
        input = """
func fvoid() {putStringLn("GiaiPhongMienNam");}

var global = fint()
func main() {
    fvoid();
    putFloatLn(global + 2.0)

    var local = "a";
    putBoolLn(local <= "b")
    local += "c"
    putStringLn(local)

};

func fint() int {return 1;}
"""
        self.assertTrue(TestCodeGen.test(input,"GiaiPhongMienNam\n3.0\ntrue\nac\n",1)) 

    def test_002(self):
        input = """
func main() {
    putInt(1);
};
"""
        self.assertTrue(TestCodeGen.test(input,"1",2)) 

    def test_003(self):
        input = """
var global = 1;

func main() {
    var local = 2;
};
"""
        self.assertTrue(TestCodeGen.test(input,"",3)) 
        
    def test_004(self):
        input = """
var global = fint();

func main() {
    var local = 2;
};

func fint() int {return 1;}
"""
        self.assertTrue(TestCodeGen.test(input,"",4)) 


    def test_005(self):
        input = """
const a = 2
func main() {
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"""020""",5))

    def test_006(self):
        input = """
func main() {
    var local = "a";
    local += "c"
    putStringLn(local)
    var local2 string;
    //local2 := "Mien Nam giai phong";
    putStringLn(local2)
};
"""
        self.assertTrue(TestCodeGen.test(input,"ac\n\n",6)) 

    def test_007(self):
        input = """
func fvoid() {putStringLn("HoangPhuc");}

var global = fint()
const globalConst = "HoangPhuc"

func main() {
    fvoid();
    putIntLn(global + 1)

    var local = "a";
    putBoolLn(local <= "b")
    local += "c"
    putStringLn(local)

    const myConst = fint()
    const myConst2 = "Hello world"
    putStringLn(myConst2)

    putStringLn(globalConst)
};

func fint() int {return 1;}
"""
        self.assertTrue(TestCodeGen.test(input,"HoangPhuc\n2\ntrue\nac\nHello world\nHoangPhuc\n",7)) 

    def test_008(self):
        input = """ 
func main() {
    putIntLn(1)
    putFloatLn(1.0)
    putStringLn("THONG NHAT DAT NUOC")
    putLn()
} 
"""
        self.assertTrue(TestCodeGen.test(input,"1\n1.0\nTHONG NHAT DAT NUOC\n\n",8)) 


    def test_009(self):
        input = """ 
func main() {
    var a float = 3.0;
    putFloat(1 + a)
}
"""
        self.assertTrue(TestCodeGen.test(input,"4.0",9)) 

    def test_010(self):
        input = """ 
func main() {
    putBoolLn(5.0 > 2.0)
    putBoolLn(5.0 < 2.0)
    putBoolLn(5.0 <= 5.0)
    putBoolLn(5.0 >= 5.0)
    putBoolLn(5.0 == 5.0)
    putBoolLn(5.0 != 5.0)
}
"""
        self.assertTrue(TestCodeGen.test(input,"true\nfalse\ntrue\ntrue\ntrue\nfalse\n",10)) 

    def test_011(self):
        input = """
const a = 2
func main() {
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"""020""",11))

    def test_012(self):
        input = """ 
func foo() int {return 1;}        

func main() {
    putInt(foo())
}
"""
        self.assertTrue(TestCodeGen.test(input,"1",12)) 

    def test_013(self):
        input = """
const a = 2
func main() {
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"""020""",13))

    def test_014(self):
        input = """ 
var a = 1;
func main() {
    b := a + 1;
    putInt(a)
    putInt(b)
}
"""
        self.assertTrue(TestCodeGen.test(input,"12",14)) 

    def test_015(self):
        input = """
const a = 2
func main() {
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"""020""",15))

    def test_016(self):
        input = """ 
var a float = 3;
func main() {
    putFloatLn(a)
    var a float = 4;
    putFloatLn(a)
    a := 2
    putFloat(a)
}
"""
        self.assertTrue(TestCodeGen.test(input,"3.0\n4.0\n2.0",16)) 




    def test_017(self):
        input = """
func main() {
    var a [1] int ;
    a[0] := 1
    putInt(a[0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"1",17))


    def test_018(self):
        input = """
func main() {
    var a [2][1] int = [2][1] int {{12},{20}};
    a[0] := [1] int {43}
    putIntLn(a[0][0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"43\n",18))

    def test_019(self):
        input = """
func main() {
    var a [1][1][1] int;
    a[0][0][0] := 1
    putInt(a[0][0][0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"1",19))

    def test_020(self):
        input = """
func main() {
    var a [3][2][4] float;
    a[0][1][0] := 124.4
    putFloat(a[0][1][0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"124.4",20))

    def test_021(self):
        input = """
const a = 2
func main() {
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"""020""",21))

    def test_022(self):
        input = """
const a = 2
func main() {
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"""020""",22))
    def test_023(self):
        input = """
const b = [3][2]float {{1.4, 64},{6.0, 634.2},{10.0, 1.0}};

func f(variable [3][2]float) [2]float {
    return variable[0];
}

func main() {
    var a [2] float = f(b);
    putFloatLn(a[0]);
    putFloatLn(a[1]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"1.4\n64.0\n",23))

    def test_024(self):
        input = """
var b = [3][2]float {{1.4, 64},{6.0, 634.2},{10.0, 1.0}};

func main() {
    b[0] := [2]float{30.0, 4}
    putFloatLn(b[1][0])
    putFloatLn(b[1][1])
}
    """
        self.assertTrue(TestCodeGen.test(input,"6.0\n634.2\n",24))

    def test_025(self):
        input = """
var b int = 124;

func main() {
    var a [2] int;
    a[0] := 100
    a[1] += a[0] + a[0]
    putInt(a[1])

    b := 42
    putInt(b)
}
    """
        self.assertTrue(TestCodeGen.test(input,"20042",25))

    def test_026(self):
        input = """
var a string;
func main() {
    var b string;
    putString(a)
    putString(b)
}
    """
        self.assertTrue(TestCodeGen.test(input,"",26))


    def test_027(self):
        input = """
func main() {
    var a [2] int;
    a[0] := 100
    a[a[0] - 99] += a[0]
    putInt(a[1])
}
    """
        self.assertTrue(TestCodeGen.test(input,"100",27))

    def test_028(self):
        input = """
func main() {
    var a [2][3] int;
    a[a[1][1]] := [3] int {1,2,3}
    putInt(a[0][0] + a[0][2])
}
    """
        self.assertTrue(TestCodeGen.test(input,"4",28))

    def test_029(self):
        input = """
func main() {
    var a [2][2] float ;
    a[1][0] := 10
    putFloat(a[1][0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"10.0",29))








    def test_030(self):
        input = """
const a = 2
func main() {
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"""020""",30))

    def test_031(self):
        input = """
const a = 2
func main() {
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"""020""",31))

    def test_032(self):
        input = """
const a = 2
func main() {
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"""020""",32))



    def test_033(self):
        input = """
func main() {
    var i = 0;
    for i < 3 {
        putInt(i);
        i += 1;
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "0123", 33))

    def test_034(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        if (i == 3) {
            break;
        }
        putInt(i);
        i += 1;
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "0123", 34))

    def test_035(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        i += 1;
        if (i % 2 == 0) {
            continue;
        }
        putInt(i);
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "1355", 35))

    def test_036(self):
        input = """
func foo() int {return foo1();}
var a = foo() + foo1();
func main() {
    putInt(a)
    a := foo()
    putInt(a)
}
func foo1() int {return 1;}
        """
        self.assertTrue(TestCodeGen.test(input, "21", 36))

    def test_037(self):
        input = """
const a = 2
func main() {
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
        """
        self.assertTrue(TestCodeGen.test(input, "020", 37))




    def test_038(self):
        input = """
func main() {
    var a [2] int = [2] int {10, 20};
    putInt(a[0])
}
"""
        self.assertTrue(TestCodeGen.test(input,"10",38)) 
    

    def test_039(self):
        input = """
func main() {
    var a [2][3] float = [2][3] int {{10, 20, 30}, {40, 50, 60}};
    putFloat(a[1][0])
}
"""
        self.assertTrue(TestCodeGen.test(input,"40.0",39)) 

    def test_040(self):
        input = """
func main() {
    var a [2] int;
    putInt(a[0])
    putInt(a[1])
}
"""
        self.assertTrue(TestCodeGen.test(input,"00",40)) 


    def test_041(self):
        input = """
func main() {
    var a [2][3] int ;
    putInt(a[0][0])
    putInt(a[0][1])
    putInt(a[0][2])
    putInt(a[1][0])
    putInt(a[1][1])
    putInt(a[1][2])
}
"""
        self.assertTrue(TestCodeGen.test(input,"000000",41)) 


    def test_042(self):
        input = """
func main() {
    var a [2][3][2] int ;
    putInt(a[0][0][0])
}
"""
        self.assertTrue(TestCodeGen.test(input,"0",42)) 


    def test_043(self):
        input = """
func main() {
    var a [2] int;
    a[0] := 100
    putInt(a[0])
}
"""
        self.assertTrue(TestCodeGen.test(input,"100",43)) 



    def test_044(self):
        input = """
func main() {
    var a [2][3] int;
    a[a[1][1]] := [3] int {1,2,3}
    putInt(a[0][0] + a[0][2])
}
"""
        self.assertTrue(TestCodeGen.test(input,"4",44)) 


    def test_045(self):
        input = """
func main() {
    var a [2][3] float;
    a[0][0] += 2.0
    putFloat(a[0][0] + a[0][1])
}
"""
        self.assertTrue(TestCodeGen.test(input,"2.0",45)) 


    def test_046(self):
        input = """
func main() {
    var a [2][3] string;
    a[0][0] := "VOTIEN"
    putString(a[0][0] + a[0][1])
}
"""
        self.assertTrue(TestCodeGen.test(input,"VOTIEN",46)) 


    def test_047(self):
        input = """
func main() {
    putInt(1);
};
"""
        self.assertTrue(TestCodeGen.test(input,"1",47)) 

    def test_048(self):
        input = """
var global = 1;

func main() {
    var local = 2;
};
"""
        self.assertTrue(TestCodeGen.test(input,"",48)) 
        
    def test_049(self):
        input = """
var global = fint();

func main() {
    var local = 2;
};

func fint() int {return 1;}
"""
        self.assertTrue(TestCodeGen.test(input,"",49)) 


    def test_050(self):
        input = """
const a = 2
func main() {
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"""020""",50)) 


    def test_051(self):
        input = """
func main() {
    var local = "a";
    local += "c"
    putStringLn(local)

};
"""
        self.assertTrue(TestCodeGen.test(input,"ac\n",51)) 

    def test_052(self):
        input = """
func fvoid() {putStringLn("HoangPhuc");}

var global = fint()
const globalConst = "HoangPhuc"

func main() {
    fvoid();
    putIntLn(global + 1)

    var local = "a";
    putBoolLn(local <= "b")
    local += "c"
    putStringLn(local)

    const myConst = fint()
    const myConst2 = "Hello world"
    putStringLn(myConst2)

    putStringLn(globalConst)
};

func fint() int {return 1;}
"""
        self.assertTrue(TestCodeGen.test(input,"HoangPhuc\n2\ntrue\nac\nHello world\nHoangPhuc\n",52)) 

    def test_053(self):
        input = """ 
func main() {
    putIntLn(1)
    putFloatLn(1.0)
    putStringLn("THONG NHAT DAT NUOC")
    putLn()
} 
"""
        self.assertTrue(TestCodeGen.test(input,"1\n1.0\nTHONG NHAT DAT NUOC\n\n",53)) 


    def test_054(self):
        input = """ 
func main() {
    var a float = 3.0;
    putFloat(1 + a)
}
"""
        self.assertTrue(TestCodeGen.test(input,"4.0",54)) 

    def test_055(self):
        input = """ 
func main() {
    putBoolLn(5.0 > 2.0)
    putBoolLn(5.0 < 2.0)
    putBoolLn(5.0 <= 5.0)
    putBoolLn(5.0 >= 5.0)
    putBoolLn(5.0 == 5.0)
    putBoolLn(5.0 != 5.0)
}
"""
        self.assertTrue(TestCodeGen.test(input,"true\nfalse\ntrue\ntrue\ntrue\nfalse\n",55)) 

    def test_056(self):
        input = """
const a = 2
func main() {
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"""020""",56))

    def test_057(self):
        input = """ 
func foo() int {return 1;}        

func main() {
    putInt(foo())
}
"""
        self.assertTrue(TestCodeGen.test(input,"1",57)) 

    def test_058(self):
        input = """
const a = 2
func main() {
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"""020""",58))

    def test_059(self):
        input = """ 
var a = 1;
func main() {
    b := a + 1;
    putInt(a)
    putInt(b)
}
"""
        self.assertTrue(TestCodeGen.test(input,"12",59)) 

    def test_060(self):
        input = """
const a = 2
func main() {
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"""020""",60))

    def test_061(self):
        input = """ 
var a float = 3;
func main() {
    putFloatLn(a)
    var a float = 4;
    putFloatLn(a)
    a := 2
    putFloat(a)
}
"""
        self.assertTrue(TestCodeGen.test(input,"3.0\n4.0\n2.0",61)) 




    def test_062(self):
        input = """
func main() {
    var a [1] int ;
    a[0] := 1
    putInt(a[0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"1",62))


    def test_063(self):
        input = """
func main() {
    var a [2][1] float = [2][1] float {{12},{20}};
    a[0] := [1] float{43}
    putFloatLn(a[0][0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"43.0\n",63))

    def test_064(self):
        input = """
func main() {
    var a [1][1][1] int;
    a[0][0][0] := 1
    putInt(a[0][0][0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"1",64))

    def test_065(self):
        input = """
func main() {
    var a [3][2][4] float;
    a[0][1][0] := 124.4
    putFloat(a[0][1][0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"124.4",65))

    def test_066(self):
        input = """
const a = 2
func main() {
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"""020""",66))

    def test_067(self):
        input = """
var a string;
func main() {
    var b string;
    putString(a)
    putString(b)
}
    """
        self.assertTrue(TestCodeGen.test(input,"",67))

    def test_068(self):
        input = """
func createArray() [3] int {
        return [3] int {10, 20, 30};
    }

func main() {
    var a [3] int = createArray();
    putInt(a[0]);
    putInt(a[1]);
    putInt(a[2]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"102030",68))


    def test_069(self):
        input = """
const a = 2
func main() {
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"""020""",69))

    def test_070(self):
        input = """
func main() {
    var i = 2;
    for i > 0 {
        putInt(i);
        i -= 1;
    }
    putInt(i);
}
    """
        self.assertTrue(TestCodeGen.test(input,"210",70))

    def test_071(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        if (i == 3) {
            break;
        }
        putInt(i);
        i += 1;
    }
    putInt(i);
}
    """
        self.assertTrue(TestCodeGen.test(input,"0123",71))

    def test_072(self):
        input = """
func main() {
    var i int;
    for i := 0; i < 2; i += 1 {
        putInt(i)
    }
    putInt(i)
}
    """
        self.assertTrue(TestCodeGen.test(input,"012",72))

    def test_073(self):
        input = """
func main() {
    var i int;
    for i := 0; i < 5; i += 1 {
        if (i % 2 == 0) {
            continue;
        }
        putInt(i);
    }
    putInt(i);
}
    """
        self.assertTrue(TestCodeGen.test(input,"135",73))

    def test_074(self):
        input = """
func main() {
    var i int = 10;
    for var i int = 0; i < 2; i += 1 {
        putIntLn(i)
    }
    putInt(i)
}
    """
        self.assertTrue(TestCodeGen.test(input,"""0
1
10""",74))

    
    def test_075(self):
        input = """
func main() {
    var i int ;
    for i := 0; i < 2; i += 1 {
        var i int = 10;
        putIntLn(i)
        break;
    }
    putInt(i)
}
    """
        self.assertTrue(TestCodeGen.test(input,"""10
0""",75))

    def test_076(self):
        input = """
const a = 2
func main() {
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"""020""",76))

    def test_077(self):
        input = """
func main() {
    const a = 1 + 1
    var b [a] int = [a] int {10}
    putInt(b[0])
}
    """
        self.assertTrue(TestCodeGen.test(input,"""10""",77))

    def test_078(self):
        input = """
const a = 1* 2
func main() {
    var b [a][a] int = [a][a] int {{10, 20}, {30, 40}};
    putInt(b[0][1])
}
    """
        self.assertTrue(TestCodeGen.test(input,"""20""",78))

    
    
    def test_079(self):
        input = """
const a = 1 + 1
const c = 5 - a
func main() {
    var b [a][c] int;
    putInt(b[0][0]);
    b[0][0] := 20;
    putInt(b[0][0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"""020""",79))

    
    def test_080(self):
        input = """
const a = 2
func main() {
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"""020""",80))

    def test_081(self):
        input = """
const a = 2
func main() {
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"""020""",81))

    def test_082(self):
        input = """
const a = 2
func main() {
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"""020""",82))

    def test_083(self):
        input = """
const a = 2
func main() {
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"""020""",83))

    def test_084(self):
        input = """
func main() {
    const a = 2
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
        """
        self.assertTrue(TestCodeGen.test(input, "020", 84))

    def test_085(self):
        input = """
type Course interface {study();}
type PPL3 struct {number int;}
func (p PPL3) study() {putInt(5);}

func main(){
    
    putIntLn(4)
    
}
    """
        self.assertTrue(TestCodeGen.test(input,"""4\n""",85))

    def test_086(self):
        input = """
type Course interface {study();}
type PPL3 struct {number int;}
func (p PPL3) study() {putInt(p.number);}

func main(){
    putIntLn(4)
}
    """
        self.assertTrue(TestCodeGen.test(input,"""4\n""",86))

    def test_087(self):
        input = """
func main() {
    const a = 2
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
        """
        self.assertTrue(TestCodeGen.test(input, "020", 87))

    def test_088(self):
        input = """
func main() {
    const a = 2
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
        """
        self.assertTrue(TestCodeGen.test(input, "020", 88))

    def test_089(self):
        input = """
func main() {
    const a = 2
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
        """
        self.assertTrue(TestCodeGen.test(input, "020", 89))

    def test_090(self):
        input = """
func main() {
    const a = 2
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
        """
        self.assertTrue(TestCodeGen.test(input, "020", 90))

    def test_091(self):
        input = """
func main() {
    const a = 2
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
        """
        self.assertTrue(TestCodeGen.test(input, "020", 91))

    def test_092(self):
        input = """
func main() {
    const a = 2
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
        """
        self.assertTrue(TestCodeGen.test(input, "020", 92))

    def test_093(self):
        input = """
func main() {
    const a = 2
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
        """
        self.assertTrue(TestCodeGen.test(input, "020", 93))

    def test_094(self):
        input = """
func main() {
    const a = 2
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
        """
        self.assertTrue(TestCodeGen.test(input, "020", 94))

    def test_095(self):
        input = """
func main() {
    const a = 2
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
        """
        self.assertTrue(TestCodeGen.test(input, "020", 95))

    def test_096(self):
        input = """
func main() {
    const a = 2
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
        """
        self.assertTrue(TestCodeGen.test(input, "020", 96))

    def test_097(self):
        input = """
func main() {
    const a = 2
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
        """
        self.assertTrue(TestCodeGen.test(input, "020", 97))

    def test_098(self):
        input = """
func main() {
    const a = 2
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
        """
        self.assertTrue(TestCodeGen.test(input, "020", 98))

    def test_099(self):
        input = """
func main() {
    const a = 2
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
        """
        self.assertTrue(TestCodeGen.test(input, "020", 99))

    def test_100(self):
        input = """
func main() {
    const a = 2
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
        """
        self.assertTrue(TestCodeGen.test(input, "020", 100))

