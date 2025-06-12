# Generated from d:/VisualStudioCode/PPL/initial/initial/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,62,623,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,65,7,65,
        1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,140,8,1,1,2,1,2,1,2,3,2,145,8,2,
        1,3,1,3,1,4,1,4,1,4,3,4,152,8,4,1,5,1,5,1,6,1,6,1,6,3,6,159,8,6,
        1,7,1,7,1,7,1,7,3,7,165,8,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,
        1,10,1,10,1,10,1,10,1,10,3,10,181,8,10,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,3,11,190,8,11,1,12,1,12,1,12,1,12,1,12,1,13,1,13,3,13,
        199,8,13,1,14,1,14,1,14,1,14,1,14,3,14,206,8,14,1,15,1,15,1,15,1,
        15,1,16,1,16,3,16,214,8,16,1,17,1,17,1,17,1,17,1,17,3,17,221,8,17,
        1,18,1,18,1,18,1,18,1,18,1,18,5,18,229,8,18,10,18,12,18,232,9,18,
        1,19,1,19,1,19,1,19,1,19,1,19,5,19,240,8,19,10,19,12,19,243,9,19,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,5,20,266,8,20,10,20,12,20,
        269,9,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,5,21,280,8,
        21,10,21,12,21,283,9,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,1,22,5,22,297,8,22,10,22,12,22,300,9,22,1,23,1,23,
        1,23,1,23,1,23,3,23,307,8,23,1,24,1,24,1,24,1,24,1,24,3,24,314,8,
        24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,5,24,327,
        8,24,10,24,12,24,330,9,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,
        1,26,1,27,1,27,1,27,1,27,1,28,1,28,1,28,3,28,348,8,28,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,5,28,361,8,28,10,28,
        12,28,364,9,28,1,29,1,29,3,29,368,8,29,1,30,1,30,1,30,1,30,3,30,
        374,8,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,384,8,31,1,
        32,1,32,1,32,1,32,1,32,1,32,3,32,392,8,32,1,33,1,33,1,33,1,33,1,
        33,1,33,1,33,1,33,1,33,3,33,403,8,33,1,33,1,33,1,34,1,34,1,34,3,
        34,410,8,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,1,35,1,36,1,
        36,1,36,1,36,3,36,425,8,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,
        38,1,38,1,38,1,38,1,38,3,38,439,8,38,1,38,1,38,1,38,1,39,1,39,1,
        39,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,41,1,
        41,1,41,1,41,3,41,462,8,41,1,42,1,42,1,42,1,42,1,43,1,43,1,43,1,
        43,1,43,1,43,1,43,1,43,1,43,1,44,1,44,1,44,1,44,3,44,481,8,44,1,
        45,1,45,1,45,3,45,486,8,45,1,45,1,45,1,46,1,46,1,46,1,46,1,47,1,
        47,3,47,496,8,47,1,48,1,48,1,48,1,48,1,48,3,48,503,8,48,1,49,1,49,
        1,49,5,49,508,8,49,10,49,12,49,511,9,49,1,49,1,49,1,50,1,50,1,50,
        1,50,1,50,1,51,1,51,1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,52,
        1,52,1,52,5,52,533,8,52,10,52,12,52,536,9,52,1,53,1,53,1,53,1,53,
        1,54,1,54,1,54,1,54,1,54,1,54,1,54,3,54,549,8,54,1,54,3,54,552,8,
        54,1,54,1,54,1,55,1,55,1,55,1,55,3,55,560,8,55,1,56,1,56,1,56,1,
        56,1,56,1,56,1,56,1,56,1,57,1,57,1,57,1,58,1,58,1,58,3,58,576,8,
        58,1,58,1,58,1,59,1,59,1,59,1,59,1,60,1,60,1,60,3,60,587,8,60,1,
        60,1,60,1,60,1,60,1,60,1,60,1,61,1,61,1,61,1,61,1,61,1,61,1,61,1,
        61,1,61,1,61,1,62,1,62,1,62,1,63,1,63,1,63,1,64,1,64,3,64,613,8,
        64,1,64,1,64,1,65,1,65,3,65,619,8,65,1,65,1,65,1,65,0,8,36,38,40,
        42,44,48,56,104,66,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,
        78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,
        116,118,120,122,124,126,128,130,0,4,2,0,18,20,54,56,1,0,9,12,1,0,
        53,54,1,0,37,42,631,0,132,1,0,0,0,2,139,1,0,0,0,4,144,1,0,0,0,6,
        146,1,0,0,0,8,151,1,0,0,0,10,153,1,0,0,0,12,155,1,0,0,0,14,164,1,
        0,0,0,16,166,1,0,0,0,18,170,1,0,0,0,20,180,1,0,0,0,22,189,1,0,0,
        0,24,191,1,0,0,0,26,198,1,0,0,0,28,205,1,0,0,0,30,207,1,0,0,0,32,
        213,1,0,0,0,34,220,1,0,0,0,36,222,1,0,0,0,38,233,1,0,0,0,40,244,
        1,0,0,0,42,270,1,0,0,0,44,284,1,0,0,0,46,306,1,0,0,0,48,313,1,0,
        0,0,50,331,1,0,0,0,52,335,1,0,0,0,54,340,1,0,0,0,56,347,1,0,0,0,
        58,367,1,0,0,0,60,373,1,0,0,0,62,383,1,0,0,0,64,391,1,0,0,0,66,393,
        1,0,0,0,68,406,1,0,0,0,70,414,1,0,0,0,72,420,1,0,0,0,74,429,1,0,
        0,0,76,433,1,0,0,0,78,443,1,0,0,0,80,448,1,0,0,0,82,461,1,0,0,0,
        84,463,1,0,0,0,86,467,1,0,0,0,88,480,1,0,0,0,90,482,1,0,0,0,92,489,
        1,0,0,0,94,495,1,0,0,0,96,502,1,0,0,0,98,504,1,0,0,0,100,514,1,0,
        0,0,102,519,1,0,0,0,104,521,1,0,0,0,106,537,1,0,0,0,108,541,1,0,
        0,0,110,559,1,0,0,0,112,561,1,0,0,0,114,569,1,0,0,0,116,575,1,0,
        0,0,118,579,1,0,0,0,120,583,1,0,0,0,122,594,1,0,0,0,124,604,1,0,
        0,0,126,607,1,0,0,0,128,612,1,0,0,0,130,616,1,0,0,0,132,133,3,2,
        1,0,133,134,5,0,0,1,134,1,1,0,0,0,135,136,3,64,32,0,136,137,3,2,
        1,0,137,140,1,0,0,0,138,140,3,64,32,0,139,135,1,0,0,0,139,138,1,
        0,0,0,140,3,1,0,0,0,141,145,3,6,3,0,142,145,3,18,9,0,143,145,3,24,
        12,0,144,141,1,0,0,0,144,142,1,0,0,0,144,143,1,0,0,0,145,5,1,0,0,
        0,146,147,7,0,0,0,147,7,1,0,0,0,148,152,5,53,0,0,149,152,3,10,5,
        0,150,152,3,12,6,0,151,148,1,0,0,0,151,149,1,0,0,0,151,150,1,0,0,
        0,152,9,1,0,0,0,153,154,7,1,0,0,154,11,1,0,0,0,155,158,3,14,7,0,
        156,159,5,53,0,0,157,159,3,10,5,0,158,156,1,0,0,0,158,157,1,0,0,
        0,159,13,1,0,0,0,160,161,3,16,8,0,161,162,3,14,7,0,162,165,1,0,0,
        0,163,165,3,16,8,0,164,160,1,0,0,0,164,163,1,0,0,0,165,15,1,0,0,
        0,166,167,5,48,0,0,167,168,7,2,0,0,168,169,5,49,0,0,169,17,1,0,0,
        0,170,171,3,12,6,0,171,172,5,46,0,0,172,173,3,20,10,0,173,174,5,
        47,0,0,174,19,1,0,0,0,175,176,3,22,11,0,176,177,5,50,0,0,177,178,
        3,20,10,0,178,181,1,0,0,0,179,181,3,22,11,0,180,175,1,0,0,0,180,
        179,1,0,0,0,181,21,1,0,0,0,182,190,5,53,0,0,183,190,3,6,3,0,184,
        190,3,24,12,0,185,186,5,46,0,0,186,187,3,20,10,0,187,188,5,47,0,
        0,188,190,1,0,0,0,189,182,1,0,0,0,189,183,1,0,0,0,189,184,1,0,0,
        0,189,185,1,0,0,0,190,23,1,0,0,0,191,192,5,53,0,0,192,193,5,46,0,
        0,193,194,3,26,13,0,194,195,5,47,0,0,195,25,1,0,0,0,196,199,3,28,
        14,0,197,199,1,0,0,0,198,196,1,0,0,0,198,197,1,0,0,0,199,27,1,0,
        0,0,200,201,3,30,15,0,201,202,5,50,0,0,202,203,3,28,14,0,203,206,
        1,0,0,0,204,206,3,30,15,0,205,200,1,0,0,0,205,204,1,0,0,0,206,29,
        1,0,0,0,207,208,5,53,0,0,208,209,5,52,0,0,209,210,3,36,18,0,210,
        31,1,0,0,0,211,214,3,34,17,0,212,214,1,0,0,0,213,211,1,0,0,0,213,
        212,1,0,0,0,214,33,1,0,0,0,215,216,3,36,18,0,216,217,5,50,0,0,217,
        218,3,34,17,0,218,221,1,0,0,0,219,221,3,36,18,0,220,215,1,0,0,0,
        220,219,1,0,0,0,221,35,1,0,0,0,222,223,6,18,-1,0,223,224,3,38,19,
        0,224,230,1,0,0,0,225,226,10,2,0,0,226,227,5,34,0,0,227,229,3,38,
        19,0,228,225,1,0,0,0,229,232,1,0,0,0,230,228,1,0,0,0,230,231,1,0,
        0,0,231,37,1,0,0,0,232,230,1,0,0,0,233,234,6,19,-1,0,234,235,3,40,
        20,0,235,241,1,0,0,0,236,237,10,2,0,0,237,238,5,33,0,0,238,240,3,
        40,20,0,239,236,1,0,0,0,240,243,1,0,0,0,241,239,1,0,0,0,241,242,
        1,0,0,0,242,39,1,0,0,0,243,241,1,0,0,0,244,245,6,20,-1,0,245,246,
        3,42,21,0,246,267,1,0,0,0,247,248,10,7,0,0,248,249,5,27,0,0,249,
        266,3,42,21,0,250,251,10,6,0,0,251,252,5,28,0,0,252,266,3,42,21,
        0,253,254,10,5,0,0,254,255,5,29,0,0,255,266,3,42,21,0,256,257,10,
        4,0,0,257,258,5,30,0,0,258,266,3,42,21,0,259,260,10,3,0,0,260,261,
        5,31,0,0,261,266,3,42,21,0,262,263,10,2,0,0,263,264,5,32,0,0,264,
        266,3,42,21,0,265,247,1,0,0,0,265,250,1,0,0,0,265,253,1,0,0,0,265,
        256,1,0,0,0,265,259,1,0,0,0,265,262,1,0,0,0,266,269,1,0,0,0,267,
        265,1,0,0,0,267,268,1,0,0,0,268,41,1,0,0,0,269,267,1,0,0,0,270,271,
        6,21,-1,0,271,272,3,44,22,0,272,281,1,0,0,0,273,274,10,3,0,0,274,
        275,5,22,0,0,275,280,3,44,22,0,276,277,10,2,0,0,277,278,5,23,0,0,
        278,280,3,44,22,0,279,273,1,0,0,0,279,276,1,0,0,0,280,283,1,0,0,
        0,281,279,1,0,0,0,281,282,1,0,0,0,282,43,1,0,0,0,283,281,1,0,0,0,
        284,285,6,22,-1,0,285,286,3,46,23,0,286,298,1,0,0,0,287,288,10,4,
        0,0,288,289,5,24,0,0,289,297,3,46,23,0,290,291,10,3,0,0,291,292,
        5,25,0,0,292,297,3,46,23,0,293,294,10,2,0,0,294,295,5,26,0,0,295,
        297,3,46,23,0,296,287,1,0,0,0,296,290,1,0,0,0,296,293,1,0,0,0,297,
        300,1,0,0,0,298,296,1,0,0,0,298,299,1,0,0,0,299,45,1,0,0,0,300,298,
        1,0,0,0,301,302,5,35,0,0,302,307,3,46,23,0,303,304,5,23,0,0,304,
        307,3,46,23,0,305,307,3,48,24,0,306,301,1,0,0,0,306,303,1,0,0,0,
        306,305,1,0,0,0,307,47,1,0,0,0,308,309,6,24,-1,0,309,314,3,52,26,
        0,310,314,5,53,0,0,311,314,3,4,2,0,312,314,3,50,25,0,313,308,1,0,
        0,0,313,310,1,0,0,0,313,311,1,0,0,0,313,312,1,0,0,0,314,328,1,0,
        0,0,315,316,10,7,0,0,316,317,5,48,0,0,317,318,3,36,18,0,318,319,
        5,49,0,0,319,327,1,0,0,0,320,321,10,6,0,0,321,322,5,43,0,0,322,327,
        5,53,0,0,323,324,10,5,0,0,324,325,5,43,0,0,325,327,3,52,26,0,326,
        315,1,0,0,0,326,320,1,0,0,0,326,323,1,0,0,0,327,330,1,0,0,0,328,
        326,1,0,0,0,328,329,1,0,0,0,329,49,1,0,0,0,330,328,1,0,0,0,331,332,
        5,44,0,0,332,333,3,36,18,0,333,334,5,45,0,0,334,51,1,0,0,0,335,336,
        5,53,0,0,336,337,5,44,0,0,337,338,3,32,16,0,338,339,5,45,0,0,339,
        53,1,0,0,0,340,341,3,56,28,0,341,342,5,43,0,0,342,343,3,52,26,0,
        343,55,1,0,0,0,344,345,6,28,-1,0,345,348,3,52,26,0,346,348,5,53,
        0,0,347,344,1,0,0,0,347,346,1,0,0,0,348,362,1,0,0,0,349,350,10,5,
        0,0,350,351,5,48,0,0,351,352,3,36,18,0,352,353,5,49,0,0,353,361,
        1,0,0,0,354,355,10,4,0,0,355,356,5,43,0,0,356,361,5,53,0,0,357,358,
        10,3,0,0,358,359,5,43,0,0,359,361,3,52,26,0,360,349,1,0,0,0,360,
        354,1,0,0,0,360,357,1,0,0,0,361,364,1,0,0,0,362,360,1,0,0,0,362,
        363,1,0,0,0,363,57,1,0,0,0,364,362,1,0,0,0,365,368,3,60,30,0,366,
        368,1,0,0,0,367,365,1,0,0,0,367,366,1,0,0,0,368,59,1,0,0,0,369,370,
        3,62,31,0,370,371,3,60,30,0,371,374,1,0,0,0,372,374,3,62,31,0,373,
        369,1,0,0,0,373,372,1,0,0,0,374,61,1,0,0,0,375,384,3,64,32,0,376,
        384,3,100,50,0,377,384,3,108,54,0,378,384,3,116,58,0,379,384,3,124,
        62,0,380,384,3,126,63,0,381,384,3,128,64,0,382,384,3,130,65,0,383,
        375,1,0,0,0,383,376,1,0,0,0,383,377,1,0,0,0,383,378,1,0,0,0,383,
        379,1,0,0,0,383,380,1,0,0,0,383,381,1,0,0,0,383,382,1,0,0,0,384,
        63,1,0,0,0,385,392,3,66,33,0,386,392,3,70,35,0,387,392,3,72,36,0,
        388,392,3,76,38,0,389,392,3,80,40,0,390,392,3,86,43,0,391,385,1,
        0,0,0,391,386,1,0,0,0,391,387,1,0,0,0,391,388,1,0,0,0,391,389,1,
        0,0,0,391,390,1,0,0,0,392,65,1,0,0,0,393,394,5,14,0,0,394,402,5,
        53,0,0,395,396,3,8,4,0,396,397,5,36,0,0,397,398,3,36,18,0,398,403,
        1,0,0,0,399,403,3,8,4,0,400,401,5,36,0,0,401,403,3,36,18,0,402,395,
        1,0,0,0,402,399,1,0,0,0,402,400,1,0,0,0,403,404,1,0,0,0,404,405,
        5,51,0,0,405,67,1,0,0,0,406,407,5,14,0,0,407,409,5,53,0,0,408,410,
        3,8,4,0,409,408,1,0,0,0,409,410,1,0,0,0,410,411,1,0,0,0,411,412,
        5,36,0,0,412,413,3,36,18,0,413,69,1,0,0,0,414,415,5,13,0,0,415,416,
        5,53,0,0,416,417,5,36,0,0,417,418,3,36,18,0,418,419,5,51,0,0,419,
        71,1,0,0,0,420,421,5,5,0,0,421,422,5,53,0,0,422,424,3,92,46,0,423,
        425,3,8,4,0,424,423,1,0,0,0,424,425,1,0,0,0,425,426,1,0,0,0,426,
        427,3,74,37,0,427,428,5,51,0,0,428,73,1,0,0,0,429,430,5,46,0,0,430,
        431,3,60,30,0,431,432,5,47,0,0,432,75,1,0,0,0,433,434,5,5,0,0,434,
        435,3,78,39,0,435,436,5,53,0,0,436,438,3,92,46,0,437,439,3,8,4,0,
        438,437,1,0,0,0,438,439,1,0,0,0,439,440,1,0,0,0,440,441,3,74,37,
        0,441,442,5,51,0,0,442,77,1,0,0,0,443,444,5,44,0,0,444,445,5,53,
        0,0,445,446,5,53,0,0,446,447,5,45,0,0,447,79,1,0,0,0,448,449,5,6,
        0,0,449,450,5,53,0,0,450,451,5,7,0,0,451,452,5,46,0,0,452,453,3,
        82,41,0,453,454,5,47,0,0,454,455,1,0,0,0,455,456,5,51,0,0,456,81,
        1,0,0,0,457,458,3,84,42,0,458,459,3,82,41,0,459,462,1,0,0,0,460,
        462,3,84,42,0,461,457,1,0,0,0,461,460,1,0,0,0,462,83,1,0,0,0,463,
        464,5,53,0,0,464,465,3,8,4,0,465,466,5,51,0,0,466,85,1,0,0,0,467,
        468,5,6,0,0,468,469,5,53,0,0,469,470,5,8,0,0,470,471,5,46,0,0,471,
        472,3,88,44,0,472,473,5,47,0,0,473,474,1,0,0,0,474,475,5,51,0,0,
        475,87,1,0,0,0,476,477,3,90,45,0,477,478,3,88,44,0,478,481,1,0,0,
        0,479,481,3,90,45,0,480,476,1,0,0,0,480,479,1,0,0,0,481,89,1,0,0,
        0,482,483,5,53,0,0,483,485,3,92,46,0,484,486,3,8,4,0,485,484,1,0,
        0,0,485,486,1,0,0,0,486,487,1,0,0,0,487,488,5,51,0,0,488,91,1,0,
        0,0,489,490,5,44,0,0,490,491,3,94,47,0,491,492,5,45,0,0,492,93,1,
        0,0,0,493,496,3,96,48,0,494,496,1,0,0,0,495,493,1,0,0,0,495,494,
        1,0,0,0,496,95,1,0,0,0,497,498,3,98,49,0,498,499,5,50,0,0,499,500,
        3,96,48,0,500,503,1,0,0,0,501,503,3,98,49,0,502,497,1,0,0,0,502,
        501,1,0,0,0,503,97,1,0,0,0,504,509,5,53,0,0,505,506,5,50,0,0,506,
        508,5,53,0,0,507,505,1,0,0,0,508,511,1,0,0,0,509,507,1,0,0,0,509,
        510,1,0,0,0,510,512,1,0,0,0,511,509,1,0,0,0,512,513,3,8,4,0,513,
        99,1,0,0,0,514,515,3,104,52,0,515,516,3,102,51,0,516,517,3,36,18,
        0,517,518,5,51,0,0,518,101,1,0,0,0,519,520,7,3,0,0,520,103,1,0,0,
        0,521,522,6,52,-1,0,522,523,5,53,0,0,523,534,1,0,0,0,524,525,10,
        2,0,0,525,526,5,48,0,0,526,527,3,36,18,0,527,528,5,49,0,0,528,533,
        1,0,0,0,529,530,10,1,0,0,530,531,5,43,0,0,531,533,5,53,0,0,532,524,
        1,0,0,0,532,529,1,0,0,0,533,536,1,0,0,0,534,532,1,0,0,0,534,535,
        1,0,0,0,535,105,1,0,0,0,536,534,1,0,0,0,537,538,5,53,0,0,538,539,
        3,102,51,0,539,540,3,36,18,0,540,107,1,0,0,0,541,542,5,1,0,0,542,
        543,5,44,0,0,543,544,3,36,18,0,544,545,5,45,0,0,545,546,1,0,0,0,
        546,548,3,74,37,0,547,549,3,110,55,0,548,547,1,0,0,0,548,549,1,0,
        0,0,549,551,1,0,0,0,550,552,3,114,57,0,551,550,1,0,0,0,551,552,1,
        0,0,0,552,553,1,0,0,0,553,554,5,51,0,0,554,109,1,0,0,0,555,556,3,
        112,56,0,556,557,3,110,55,0,557,560,1,0,0,0,558,560,3,112,56,0,559,
        555,1,0,0,0,559,558,1,0,0,0,560,111,1,0,0,0,561,562,5,2,0,0,562,
        563,5,1,0,0,563,564,5,44,0,0,564,565,3,36,18,0,565,566,5,45,0,0,
        566,567,1,0,0,0,567,568,3,74,37,0,568,113,1,0,0,0,569,570,5,2,0,
        0,570,571,3,74,37,0,571,115,1,0,0,0,572,576,3,122,61,0,573,576,3,
        120,60,0,574,576,3,118,59,0,575,572,1,0,0,0,575,573,1,0,0,0,575,
        574,1,0,0,0,576,577,1,0,0,0,577,578,5,51,0,0,578,117,1,0,0,0,579,
        580,5,3,0,0,580,581,3,36,18,0,581,582,3,74,37,0,582,119,1,0,0,0,
        583,586,5,3,0,0,584,587,3,68,34,0,585,587,3,106,53,0,586,584,1,0,
        0,0,586,585,1,0,0,0,587,588,1,0,0,0,588,589,5,51,0,0,589,590,3,36,
        18,0,590,591,5,51,0,0,591,592,3,106,53,0,592,593,3,74,37,0,593,121,
        1,0,0,0,594,595,5,3,0,0,595,596,5,53,0,0,596,597,5,50,0,0,597,598,
        5,53,0,0,598,599,5,37,0,0,599,600,5,17,0,0,600,601,3,36,18,0,601,
        602,1,0,0,0,602,603,3,74,37,0,603,123,1,0,0,0,604,605,5,16,0,0,605,
        606,5,51,0,0,606,125,1,0,0,0,607,608,5,15,0,0,608,609,5,51,0,0,609,
        127,1,0,0,0,610,613,3,52,26,0,611,613,3,54,27,0,612,610,1,0,0,0,
        612,611,1,0,0,0,613,614,1,0,0,0,614,615,5,51,0,0,615,129,1,0,0,0,
        616,618,5,4,0,0,617,619,3,36,18,0,618,617,1,0,0,0,618,619,1,0,0,
        0,619,620,1,0,0,0,620,621,5,51,0,0,621,131,1,0,0,0,49,139,144,151,
        158,164,180,189,198,205,213,220,230,241,265,267,279,281,296,298,
        306,313,326,328,347,360,362,367,373,383,391,402,409,424,438,461,
        480,485,495,502,509,532,534,548,551,559,575,586,612,618
    ]

class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'&&'", "'||'", "'!'", "'='", "':='", "'+='", "'-='", 
                     "'*='", "'/='", "'%='", "'.'", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "NIL", "TRUE", "FALSE", "NEWLINE", "ADD", "SUB", "MUL", 
                      "DIV", "MOD", "EQUAL", "NOT_EQUAL", "LESS", "LESS_EQUAL", 
                      "GREATER", "GREATER_EQUAL", "AND", "OR", "NOT", "ASSIGN", 
                      "ASSIGN_STATE", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", 
                      "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "LBRACK", "RBRACK", "COMMA", "SEMICOLON", 
                      "COLON", "ID", "INTEGER_LIT", "FLOAT_LIT", "STRING_LIT", 
                      "WS", "COMMENT_INLINE", "COMMENT_BLOCK", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_declared_statement_list = 1
    RULE_literal = 2
    RULE_literal_primitive = 3
    RULE_mytype = 4
    RULE_primitive_type = 5
    RULE_array_type = 6
    RULE_array_dimention = 7
    RULE_array_dimention_element = 8
    RULE_array_lit_instance = 9
    RULE_list_array_value = 10
    RULE_list_array_value_element = 11
    RULE_struct_lit_instance = 12
    RULE_struct_lit_instance_body = 13
    RULE_struct_lit_instance_body_prime = 14
    RULE_struct_lit_instance_body_element = 15
    RULE_list_expression = 16
    RULE_list_expression_prime = 17
    RULE_expression = 18
    RULE_expression1 = 19
    RULE_expression2 = 20
    RULE_expression3 = 21
    RULE_expression4 = 22
    RULE_expression5 = 23
    RULE_expression6 = 24
    RULE_expression7 = 25
    RULE_function_call = 26
    RULE_method_call = 27
    RULE_temp_expression6 = 28
    RULE_list_statement = 29
    RULE_list_statement_prime = 30
    RULE_statement = 31
    RULE_declared_statement = 32
    RULE_variables_declared = 33
    RULE_variables_declared_without_semi_for_loop = 34
    RULE_constants_declared = 35
    RULE_function_declared = 36
    RULE_function_body_container = 37
    RULE_method_declared = 38
    RULE_receiver_container = 39
    RULE_struct_declared = 40
    RULE_struct_declared_body = 41
    RULE_struct_declared_body_element = 42
    RULE_interface_declared = 43
    RULE_interface_declared_body = 44
    RULE_interface_declared_element = 45
    RULE_interface_parameter_container = 46
    RULE_list_interface_parameter = 47
    RULE_list_interface_parameter_prime = 48
    RULE_list_interface_parameter_element = 49
    RULE_assignment_statement = 50
    RULE_assignment_operator = 51
    RULE_lhs_assignment_statement = 52
    RULE_assignment_statement_without_semi_for_loop = 53
    RULE_if_statement = 54
    RULE_else_if_clause = 55
    RULE_else_if_clause_content = 56
    RULE_else_clause = 57
    RULE_for_statement = 58
    RULE_basic_for_loop = 59
    RULE_initialization_for_loop = 60
    RULE_array_for_loop = 61
    RULE_break_statement = 62
    RULE_continue_statement = 63
    RULE_call_statement = 64
    RULE_return_statement = 65

    ruleNames =  [ "program", "declared_statement_list", "literal", "literal_primitive", 
                   "mytype", "primitive_type", "array_type", "array_dimention", 
                   "array_dimention_element", "array_lit_instance", "list_array_value", 
                   "list_array_value_element", "struct_lit_instance", "struct_lit_instance_body", 
                   "struct_lit_instance_body_prime", "struct_lit_instance_body_element", 
                   "list_expression", "list_expression_prime", "expression", 
                   "expression1", "expression2", "expression3", "expression4", 
                   "expression5", "expression6", "expression7", "function_call", 
                   "method_call", "temp_expression6", "list_statement", 
                   "list_statement_prime", "statement", "declared_statement", 
                   "variables_declared", "variables_declared_without_semi_for_loop", 
                   "constants_declared", "function_declared", "function_body_container", 
                   "method_declared", "receiver_container", "struct_declared", 
                   "struct_declared_body", "struct_declared_body_element", 
                   "interface_declared", "interface_declared_body", "interface_declared_element", 
                   "interface_parameter_container", "list_interface_parameter", 
                   "list_interface_parameter_prime", "list_interface_parameter_element", 
                   "assignment_statement", "assignment_operator", "lhs_assignment_statement", 
                   "assignment_statement_without_semi_for_loop", "if_statement", 
                   "else_if_clause", "else_if_clause_content", "else_clause", 
                   "for_statement", "basic_for_loop", "initialization_for_loop", 
                   "array_for_loop", "break_statement", "continue_statement", 
                   "call_statement", "return_statement" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    RETURN=4
    FUNC=5
    TYPE=6
    STRUCT=7
    INTERFACE=8
    STRING=9
    INT=10
    FLOAT=11
    BOOLEAN=12
    CONST=13
    VAR=14
    CONTINUE=15
    BREAK=16
    RANGE=17
    NIL=18
    TRUE=19
    FALSE=20
    NEWLINE=21
    ADD=22
    SUB=23
    MUL=24
    DIV=25
    MOD=26
    EQUAL=27
    NOT_EQUAL=28
    LESS=29
    LESS_EQUAL=30
    GREATER=31
    GREATER_EQUAL=32
    AND=33
    OR=34
    NOT=35
    ASSIGN=36
    ASSIGN_STATE=37
    ADD_ASSIGN=38
    SUB_ASSIGN=39
    MUL_ASSIGN=40
    DIV_ASSIGN=41
    MOD_ASSIGN=42
    DOT=43
    LPAREN=44
    RPAREN=45
    LBRACE=46
    RBRACE=47
    LBRACK=48
    RBRACK=49
    COMMA=50
    SEMICOLON=51
    COLON=52
    ID=53
    INTEGER_LIT=54
    FLOAT_LIT=55
    STRING_LIT=56
    WS=57
    COMMENT_INLINE=58
    COMMENT_BLOCK=59
    ERROR_CHAR=60
    UNCLOSE_STRING=61
    ILLEGAL_ESCAPE=62

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declared_statement_list(self):
            return self.getTypedRuleContext(MiniGoParser.Declared_statement_listContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.declared_statement_list()
            self.state = 133
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declared_statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declared_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Declared_statementContext,0)


        def declared_statement_list(self):
            return self.getTypedRuleContext(MiniGoParser.Declared_statement_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declared_statement_list




    def declared_statement_list(self):

        localctx = MiniGoParser.Declared_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declared_statement_list)
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.declared_statement()

                self.state = 136
                self.declared_statement_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.declared_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal_primitive(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_primitiveContext,0)


        def array_lit_instance(self):
            return self.getTypedRuleContext(MiniGoParser.Array_lit_instanceContext,0)


        def struct_lit_instance(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_lit_instanceContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_literal)
        try:
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18, 19, 20, 54, 55, 56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.literal_primitive()
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.array_lit_instance()
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 3)
                self.state = 143
                self.struct_lit_instance()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_primitiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LIT(self):
            return self.getToken(MiniGoParser.INTEGER_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_literal_primitive




    def literal_primitive(self):

        localctx = MiniGoParser.Literal_primitiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_literal_primitive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 126100789568208896) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MytypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_mytype




    def mytype(self):

        localctx = MiniGoParser.MytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_mytype)
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.match(MiniGoParser.ID)
                pass
            elif token in [9, 10, 11, 12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.primitive_type()
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitive_type




    def primitive_type(self):

        localctx = MiniGoParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_dimention(self):
            return self.getTypedRuleContext(MiniGoParser.Array_dimentionContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_type




    def array_type(self):

        localctx = MiniGoParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.array_dimention()
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.state = 156
                self.match(MiniGoParser.ID)
                pass
            elif token in [9, 10, 11, 12]:
                self.state = 157
                self.primitive_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_dimentionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_dimention_element(self):
            return self.getTypedRuleContext(MiniGoParser.Array_dimention_elementContext,0)


        def array_dimention(self):
            return self.getTypedRuleContext(MiniGoParser.Array_dimentionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_dimention




    def array_dimention(self):

        localctx = MiniGoParser.Array_dimentionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array_dimention)
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.array_dimention_element()

                self.state = 161
                self.array_dimention()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.array_dimention_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_dimention_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def INTEGER_LIT(self):
            return self.getToken(MiniGoParser.INTEGER_LIT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_dimention_element




    def array_dimention_element(self):

        localctx = MiniGoParser.Array_dimention_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_dimention_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(MiniGoParser.LBRACK)
            self.state = 167
            _la = self._input.LA(1)
            if not(_la==53 or _la==54):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 168
            self.match(MiniGoParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_lit_instanceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_array_value(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_valueContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_lit_instance




    def array_lit_instance(self):

        localctx = MiniGoParser.Array_lit_instanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array_lit_instance)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.array_type()
            self.state = 171
            self.match(MiniGoParser.LBRACE)
            self.state = 172
            self.list_array_value()
            self.state = 173
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_array_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_array_value_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_value_elementContext,0)


        def list_array_value(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_valueContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_array_value




    def list_array_value(self):

        localctx = MiniGoParser.List_array_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_list_array_value)
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.list_array_value_element()
                self.state = 176
                self.match(MiniGoParser.COMMA)

                self.state = 177
                self.list_array_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.list_array_value_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_array_value_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def literal_primitive(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_primitiveContext,0)


        def struct_lit_instance(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_lit_instanceContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_array_value(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_valueContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_list_array_value_element




    def list_array_value_element(self):

        localctx = MiniGoParser.List_array_value_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_list_array_value_element)
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.literal_primitive()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 184
                self.struct_lit_instance()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 185
                self.match(MiniGoParser.LBRACE)
                self.state = 186
                self.list_array_value()
                self.state = 187
                self.match(MiniGoParser.RBRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_lit_instanceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def struct_lit_instance_body(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_lit_instance_bodyContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_lit_instance




    def struct_lit_instance(self):

        localctx = MiniGoParser.Struct_lit_instanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_struct_lit_instance)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(MiniGoParser.ID)
            self.state = 192
            self.match(MiniGoParser.LBRACE)
            self.state = 193
            self.struct_lit_instance_body()
            self.state = 194
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_lit_instance_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_lit_instance_body_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_lit_instance_body_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_lit_instance_body




    def struct_lit_instance_body(self):

        localctx = MiniGoParser.Struct_lit_instance_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_struct_lit_instance_body)
        try:
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.struct_lit_instance_body_prime()
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_lit_instance_body_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_lit_instance_body_element(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_lit_instance_body_elementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def struct_lit_instance_body_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_lit_instance_body_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_lit_instance_body_prime




    def struct_lit_instance_body_prime(self):

        localctx = MiniGoParser.Struct_lit_instance_body_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_struct_lit_instance_body_prime)
        try:
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.struct_lit_instance_body_element()
                self.state = 201
                self.match(MiniGoParser.COMMA)
                self.state = 202
                self.struct_lit_instance_body_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.struct_lit_instance_body_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_lit_instance_body_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_lit_instance_body_element




    def struct_lit_instance_body_element(self):

        localctx = MiniGoParser.Struct_lit_instance_body_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_struct_lit_instance_body_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(MiniGoParser.ID)
            self.state = 208
            self.match(MiniGoParser.COLON)
            self.state = 209
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_expression_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_expression_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_expression




    def list_expression(self):

        localctx = MiniGoParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_list_expression)
        try:
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18, 19, 20, 23, 35, 44, 48, 53, 54, 55, 56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.list_expression_prime()
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expression_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_expression_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_expression_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_expression_prime




    def list_expression_prime(self):

        localctx = MiniGoParser.List_expression_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_list_expression_prime)
        try:
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.expression(0)
                self.state = 216
                self.match(MiniGoParser.COMMA)
                self.state = 217
                self.list_expression_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.expression1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 230
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 225
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 226
                    self.match(MiniGoParser.OR)
                    self.state = 227
                    self.expression1(0) 
                self.state = 232
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression1



    def expression1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 241
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 236
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 237
                    self.match(MiniGoParser.AND)
                    self.state = 238
                    self.expression2(0) 
                self.state = 243
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(MiniGoParser.NOT_EQUAL, 0)

        def LESS(self):
            return self.getToken(MiniGoParser.LESS, 0)

        def LESS_EQUAL(self):
            return self.getToken(MiniGoParser.LESS_EQUAL, 0)

        def GREATER(self):
            return self.getToken(MiniGoParser.GREATER, 0)

        def GREATER_EQUAL(self):
            return self.getToken(MiniGoParser.GREATER_EQUAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression2



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expression2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 267
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 265
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 247
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 248
                        self.match(MiniGoParser.EQUAL)
                        self.state = 249
                        self.expression3(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 250
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 251
                        self.match(MiniGoParser.NOT_EQUAL)
                        self.state = 252
                        self.expression3(0)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 253
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 254
                        self.match(MiniGoParser.LESS)
                        self.state = 255
                        self.expression3(0)
                        pass

                    elif la_ == 4:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 256
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 257
                        self.match(MiniGoParser.LESS_EQUAL)
                        self.state = 258
                        self.expression3(0)
                        pass

                    elif la_ == 5:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 259
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 260
                        self.match(MiniGoParser.GREATER)
                        self.state = 261
                        self.expression3(0)
                        pass

                    elif la_ == 6:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 262
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 263
                        self.match(MiniGoParser.GREATER_EQUAL)
                        self.state = 264
                        self.expression3(0)
                        pass

             
                self.state = 269
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression3



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expression3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 281
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 279
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                        self.state = 273
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 274
                        self.match(MiniGoParser.ADD)
                        self.state = 275
                        self.expression4(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                        self.state = 276
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 277
                        self.match(MiniGoParser.SUB)
                        self.state = 278
                        self.expression4(0)
                        pass

             
                self.state = 283
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression4



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expression4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 298
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 296
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                        self.state = 287
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 288
                        self.match(MiniGoParser.MUL)
                        self.state = 289
                        self.expression5()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                        self.state = 290
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 291
                        self.match(MiniGoParser.DIV)
                        self.state = 292
                        self.expression5()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                        self.state = 293
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 294
                        self.match(MiniGoParser.MOD)
                        self.state = 295
                        self.expression5()
                        pass

             
                self.state = 300
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression5




    def expression5(self):

        localctx = MiniGoParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expression5)
        try:
            self.state = 306
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.match(MiniGoParser.NOT)
                self.state = 302
                self.expression5()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.match(MiniGoParser.SUB)
                self.state = 304
                self.expression5()
                pass
            elif token in [18, 19, 20, 44, 48, 53, 54, 55, 56]:
                self.enterOuterAlt(localctx, 3)
                self.state = 305
                self.expression6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(MiniGoParser.Function_callContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def expression7(self):
            return self.getTypedRuleContext(MiniGoParser.Expression7Context,0)


        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression6



    def expression6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expression6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 309
                self.function_call()
                pass

            elif la_ == 2:
                self.state = 310
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.state = 311
                self.literal()
                pass

            elif la_ == 4:
                self.state = 312
                self.expression7()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 328
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 326
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 315
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")

                        self.state = 316
                        self.match(MiniGoParser.LBRACK)
                        self.state = 317
                        self.expression(0)
                        self.state = 318
                        self.match(MiniGoParser.RBRACK)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 320
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 321
                        self.match(MiniGoParser.DOT)
                        self.state = 322
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 323
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 324
                        self.match(MiniGoParser.DOT)

                        self.state = 325
                        self.function_call()
                        pass

             
                self.state = 330
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression7




    def expression7(self):

        localctx = MiniGoParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expression7)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(MiniGoParser.LPAREN)
            self.state = 332
            self.expression(0)
            self.state = 333
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_function_call




    def function_call(self):

        localctx = MiniGoParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_function_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(MiniGoParser.ID)
            self.state = 336
            self.match(MiniGoParser.LPAREN)
            self.state = 337
            self.list_expression()
            self.state = 338
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def temp_expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Temp_expression6Context,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def function_call(self):
            return self.getTypedRuleContext(MiniGoParser.Function_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_call




    def method_call(self):

        localctx = MiniGoParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_method_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.temp_expression6(0)
            self.state = 341
            self.match(MiniGoParser.DOT)

            self.state = 342
            self.function_call()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Temp_expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(MiniGoParser.Function_callContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def temp_expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Temp_expression6Context,0)


        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_temp_expression6



    def temp_expression6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Temp_expression6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_temp_expression6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 345
                self.function_call()
                pass

            elif la_ == 2:
                self.state = 346
                self.match(MiniGoParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 362
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 360
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Temp_expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_temp_expression6)
                        self.state = 349
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")

                        self.state = 350
                        self.match(MiniGoParser.LBRACK)
                        self.state = 351
                        self.expression(0)
                        self.state = 352
                        self.match(MiniGoParser.RBRACK)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Temp_expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_temp_expression6)
                        self.state = 354
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 355
                        self.match(MiniGoParser.DOT)
                        self.state = 356
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Temp_expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_temp_expression6)
                        self.state = 357
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 358
                        self.match(MiniGoParser.DOT)
                        self.state = 359
                        self.function_call()
                        pass

             
                self.state = 364
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class List_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_statement_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_statement_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_statement




    def list_statement(self):

        localctx = MiniGoParser.List_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_list_statement)
        try:
            self.state = 367
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 4, 5, 6, 13, 14, 15, 16, 53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.list_statement_prime()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_statement_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def list_statement_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_statement_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_statement_prime




    def list_statement_prime(self):

        localctx = MiniGoParser.List_statement_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_list_statement_prime)
        try:
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.statement()

                self.state = 370
                self.list_statement_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 372
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declared_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Declared_statementContext,0)


        def assignment_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(MiniGoParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Call_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Return_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_statement)
        try:
            self.state = 383
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.declared_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 376
                self.assignment_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 377
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 378
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 379
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 380
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 381
                self.call_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 382
                self.return_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declared_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variables_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Variables_declaredContext,0)


        def constants_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Constants_declaredContext,0)


        def function_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Function_declaredContext,0)


        def method_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declaredContext,0)


        def struct_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declaredContext,0)


        def interface_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declaredContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declared_statement




    def declared_statement(self):

        localctx = MiniGoParser.Declared_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_declared_statement)
        try:
            self.state = 391
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 385
                self.variables_declared()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 386
                self.constants_declared()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 387
                self.function_declared()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 388
                self.method_declared()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 389
                self.struct_declared()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 390
                self.interface_declared()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variables_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def mytype(self):
            return self.getTypedRuleContext(MiniGoParser.MytypeContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_variables_declared




    def variables_declared(self):

        localctx = MiniGoParser.Variables_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_variables_declared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(MiniGoParser.VAR)
            self.state = 394
            self.match(MiniGoParser.ID)
            self.state = 402
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 395
                self.mytype()
                self.state = 396
                self.match(MiniGoParser.ASSIGN)
                self.state = 397
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 399
                self.mytype()
                pass

            elif la_ == 3:
                self.state = 400
                self.match(MiniGoParser.ASSIGN)
                self.state = 401
                self.expression(0)
                pass


            self.state = 404
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variables_declared_without_semi_for_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def mytype(self):
            return self.getTypedRuleContext(MiniGoParser.MytypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_variables_declared_without_semi_for_loop




    def variables_declared_without_semi_for_loop(self):

        localctx = MiniGoParser.Variables_declared_without_semi_for_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_variables_declared_without_semi_for_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(MiniGoParser.VAR)
            self.state = 407
            self.match(MiniGoParser.ID)
            self.state = 409
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9288674231459328) != 0):
                self.state = 408
                self.mytype()


            self.state = 411
            self.match(MiniGoParser.ASSIGN)
            self.state = 412
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constants_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_constants_declared




    def constants_declared(self):

        localctx = MiniGoParser.Constants_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_constants_declared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(MiniGoParser.CONST)
            self.state = 415
            self.match(MiniGoParser.ID)
            self.state = 416
            self.match(MiniGoParser.ASSIGN)
            self.state = 417
            self.expression(0)
            self.state = 418
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def interface_parameter_container(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_parameter_containerContext,0)


        def function_body_container(self):
            return self.getTypedRuleContext(MiniGoParser.Function_body_containerContext,0)


        def mytype(self):
            return self.getTypedRuleContext(MiniGoParser.MytypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_function_declared




    def function_declared(self):

        localctx = MiniGoParser.Function_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_function_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(MiniGoParser.FUNC)
            self.state = 421
            self.match(MiniGoParser.ID)

            self.state = 422
            self.interface_parameter_container()
            self.state = 424
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9288674231459328) != 0):
                self.state = 423
                self.mytype()


            self.state = 426
            self.function_body_container()
            self.state = 427
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_body_containerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_statement_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_statement_primeContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_function_body_container




    def function_body_container(self):

        localctx = MiniGoParser.Function_body_containerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_function_body_container)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(MiniGoParser.LBRACE)
            self.state = 430
            self.list_statement_prime()
            self.state = 431
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def receiver_container(self):
            return self.getTypedRuleContext(MiniGoParser.Receiver_containerContext,0)


        def interface_parameter_container(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_parameter_containerContext,0)


        def function_body_container(self):
            return self.getTypedRuleContext(MiniGoParser.Function_body_containerContext,0)


        def mytype(self):
            return self.getTypedRuleContext(MiniGoParser.MytypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_declared




    def method_declared(self):

        localctx = MiniGoParser.Method_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_method_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.match(MiniGoParser.FUNC)

            self.state = 434
            self.receiver_container()
            self.state = 435
            self.match(MiniGoParser.ID)

            self.state = 436
            self.interface_parameter_container()
            self.state = 438
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9288674231459328) != 0):
                self.state = 437
                self.mytype()


            self.state = 440
            self.function_body_container()
            self.state = 441
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Receiver_containerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_receiver_container




    def receiver_container(self):

        localctx = MiniGoParser.Receiver_containerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_receiver_container)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.match(MiniGoParser.LPAREN)
            self.state = 444
            self.match(MiniGoParser.ID)
            self.state = 445
            self.match(MiniGoParser.ID)
            self.state = 446
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def struct_declared_body(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declared_bodyContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_declared




    def struct_declared(self):

        localctx = MiniGoParser.Struct_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_struct_declared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.match(MiniGoParser.TYPE)
            self.state = 449
            self.match(MiniGoParser.ID)
            self.state = 450
            self.match(MiniGoParser.STRUCT)

            self.state = 451
            self.match(MiniGoParser.LBRACE)
            self.state = 452
            self.struct_declared_body()
            self.state = 453
            self.match(MiniGoParser.RBRACE)
            self.state = 455
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declared_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_declared_body_element(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declared_body_elementContext,0)


        def struct_declared_body(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declared_bodyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_declared_body




    def struct_declared_body(self):

        localctx = MiniGoParser.Struct_declared_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_struct_declared_body)
        try:
            self.state = 461
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                self.struct_declared_body_element()

                self.state = 458
                self.struct_declared_body()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 460
                self.struct_declared_body_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declared_body_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def mytype(self):
            return self.getTypedRuleContext(MiniGoParser.MytypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_declared_body_element




    def struct_declared_body_element(self):

        localctx = MiniGoParser.Struct_declared_body_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_struct_declared_body_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            self.match(MiniGoParser.ID)

            self.state = 464
            self.mytype()
            self.state = 465
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def interface_declared_body(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declared_bodyContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_declared




    def interface_declared(self):

        localctx = MiniGoParser.Interface_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_interface_declared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            self.match(MiniGoParser.TYPE)
            self.state = 468
            self.match(MiniGoParser.ID)
            self.state = 469
            self.match(MiniGoParser.INTERFACE)

            self.state = 470
            self.match(MiniGoParser.LBRACE)
            self.state = 471
            self.interface_declared_body()
            self.state = 472
            self.match(MiniGoParser.RBRACE)
            self.state = 474
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declared_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface_declared_element(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declared_elementContext,0)


        def interface_declared_body(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declared_bodyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_declared_body




    def interface_declared_body(self):

        localctx = MiniGoParser.Interface_declared_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_interface_declared_body)
        try:
            self.state = 480
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 476
                self.interface_declared_element()

                self.state = 477
                self.interface_declared_body()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 479
                self.interface_declared_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declared_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def interface_parameter_container(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_parameter_containerContext,0)


        def mytype(self):
            return self.getTypedRuleContext(MiniGoParser.MytypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_declared_element




    def interface_declared_element(self):

        localctx = MiniGoParser.Interface_declared_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_interface_declared_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.match(MiniGoParser.ID)

            self.state = 483
            self.interface_parameter_container()
            self.state = 485
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9288674231459328) != 0):
                self.state = 484
                self.mytype()


            self.state = 487
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_parameter_containerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def list_interface_parameter(self):
            return self.getTypedRuleContext(MiniGoParser.List_interface_parameterContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_parameter_container




    def interface_parameter_container(self):

        localctx = MiniGoParser.Interface_parameter_containerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_interface_parameter_container)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self.match(MiniGoParser.LPAREN)
            self.state = 490
            self.list_interface_parameter()
            self.state = 491
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_interface_parameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_interface_parameter_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_interface_parameter_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_interface_parameter




    def list_interface_parameter(self):

        localctx = MiniGoParser.List_interface_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_list_interface_parameter)
        try:
            self.state = 495
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 493
                self.list_interface_parameter_prime()
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_interface_parameter_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_interface_parameter_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_interface_parameter_elementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_interface_parameter_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_interface_parameter_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_interface_parameter_prime




    def list_interface_parameter_prime(self):

        localctx = MiniGoParser.List_interface_parameter_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_list_interface_parameter_prime)
        try:
            self.state = 502
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 497
                self.list_interface_parameter_element()
                self.state = 498
                self.match(MiniGoParser.COMMA)
                self.state = 499
                self.list_interface_parameter_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 501
                self.list_interface_parameter_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_interface_parameter_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def mytype(self):
            return self.getTypedRuleContext(MiniGoParser.MytypeContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_list_interface_parameter_element




    def list_interface_parameter_element(self):

        localctx = MiniGoParser.List_interface_parameter_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_list_interface_parameter_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.match(MiniGoParser.ID)
            self.state = 509
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 505
                self.match(MiniGoParser.COMMA)
                self.state = 506
                self.match(MiniGoParser.ID)
                self.state = 511
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 512
            self.mytype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def lhs_assignment_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Lhs_assignment_statementContext,0)


        def assignment_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_operatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_statement




    def assignment_statement(self):

        localctx = MiniGoParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self.lhs_assignment_statement(0)

            self.state = 515
            self.assignment_operator()

            self.state = 516
            self.expression(0)
            self.state = 517
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN_STATE(self):
            return self.getToken(MiniGoParser.ASSIGN_STATE, 0)

        def ADD_ASSIGN(self):
            return self.getToken(MiniGoParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(MiniGoParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(MiniGoParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_operator




    def assignment_operator(self):

        localctx = MiniGoParser.Assignment_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_assignment_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8658654068736) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lhs_assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def lhs_assignment_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Lhs_assignment_statementContext,0)


        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs_assignment_statement



    def lhs_assignment_statement(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Lhs_assignment_statementContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 104
        self.enterRecursionRule(localctx, 104, self.RULE_lhs_assignment_statement, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 534
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 532
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Lhs_assignment_statementContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs_assignment_statement)
                        self.state = 524
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                        self.state = 525
                        self.match(MiniGoParser.LBRACK)
                        self.state = 526
                        self.expression(0)
                        self.state = 527
                        self.match(MiniGoParser.RBRACK)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Lhs_assignment_statementContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs_assignment_statement)
                        self.state = 529
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 530
                        self.match(MiniGoParser.DOT)
                        self.state = 531
                        self.match(MiniGoParser.ID)
                        pass

             
                self.state = 536
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Assignment_statement_without_semi_for_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def assignment_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_operatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_statement_without_semi_for_loop




    def assignment_statement_without_semi_for_loop(self):

        localctx = MiniGoParser.Assignment_statement_without_semi_for_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_assignment_statement_without_semi_for_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 537
            self.match(MiniGoParser.ID)

            self.state = 538
            self.assignment_operator()

            self.state = 539
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def function_body_container(self):
            return self.getTypedRuleContext(MiniGoParser.Function_body_containerContext,0)


        def else_if_clause(self):
            return self.getTypedRuleContext(MiniGoParser.Else_if_clauseContext,0)


        def else_clause(self):
            return self.getTypedRuleContext(MiniGoParser.Else_clauseContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_statement




    def if_statement(self):

        localctx = MiniGoParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 541
            self.match(MiniGoParser.IF)

            self.state = 542
            self.match(MiniGoParser.LPAREN)
            self.state = 543
            self.expression(0)
            self.state = 544
            self.match(MiniGoParser.RPAREN)

            self.state = 546
            self.function_body_container()
            self.state = 548
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 547
                self.else_if_clause()


            self.state = 551
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 550
                self.else_clause()


            self.state = 553
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def else_if_clause(self):
            return self.getTypedRuleContext(MiniGoParser.Else_if_clauseContext,0)


        def else_if_clause_content(self):
            return self.getTypedRuleContext(MiniGoParser.Else_if_clause_contentContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_if_clause




    def else_if_clause(self):

        localctx = MiniGoParser.Else_if_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_else_if_clause)
        try:
            self.state = 559
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 555
                self.else_if_clause_content()
                self.state = 556
                self.else_if_clause()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 558
                self.else_if_clause_content()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_clause_contentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def function_body_container(self):
            return self.getTypedRuleContext(MiniGoParser.Function_body_containerContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_if_clause_content




    def else_if_clause_content(self):

        localctx = MiniGoParser.Else_if_clause_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_else_if_clause_content)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
            self.match(MiniGoParser.ELSE)
            self.state = 562
            self.match(MiniGoParser.IF)

            self.state = 563
            self.match(MiniGoParser.LPAREN)
            self.state = 564
            self.expression(0)
            self.state = 565
            self.match(MiniGoParser.RPAREN)

            self.state = 567
            self.function_body_container()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def function_body_container(self):
            return self.getTypedRuleContext(MiniGoParser.Function_body_containerContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_clause




    def else_clause(self):

        localctx = MiniGoParser.Else_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_else_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.match(MiniGoParser.ELSE)
            self.state = 570
            self.function_body_container()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def array_for_loop(self):
            return self.getTypedRuleContext(MiniGoParser.Array_for_loopContext,0)


        def initialization_for_loop(self):
            return self.getTypedRuleContext(MiniGoParser.Initialization_for_loopContext,0)


        def basic_for_loop(self):
            return self.getTypedRuleContext(MiniGoParser.Basic_for_loopContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_statement




    def for_statement(self):

        localctx = MiniGoParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 575
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 572
                self.array_for_loop()
                pass

            elif la_ == 2:
                self.state = 573
                self.initialization_for_loop()
                pass

            elif la_ == 3:
                self.state = 574
                self.basic_for_loop()
                pass


            self.state = 577
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_for_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def function_body_container(self):
            return self.getTypedRuleContext(MiniGoParser.Function_body_containerContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_basic_for_loop




    def basic_for_loop(self):

        localctx = MiniGoParser.Basic_for_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_basic_for_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 579
            self.match(MiniGoParser.FOR)
            self.state = 580
            self.expression(0)

            self.state = 581
            self.function_body_container()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Initialization_for_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def variables_declared_without_semi_for_loop(self):
            return self.getTypedRuleContext(MiniGoParser.Variables_declared_without_semi_for_loopContext,0)


        def assignment_statement_without_semi_for_loop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Assignment_statement_without_semi_for_loopContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Assignment_statement_without_semi_for_loopContext,i)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def function_body_container(self):
            return self.getTypedRuleContext(MiniGoParser.Function_body_containerContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_initialization_for_loop




    def initialization_for_loop(self):

        localctx = MiniGoParser.Initialization_for_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_initialization_for_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 583
            self.match(MiniGoParser.FOR)
            self.state = 586
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.state = 584
                self.variables_declared_without_semi_for_loop()
                pass
            elif token in [53]:
                self.state = 585
                self.assignment_statement_without_semi_for_loop()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 588
            self.match(MiniGoParser.SEMICOLON)

            self.state = 589
            self.expression(0)
            self.state = 590
            self.match(MiniGoParser.SEMICOLON)

            self.state = 591
            self.assignment_statement_without_semi_for_loop()

            self.state = 592
            self.function_body_container()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_for_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def ASSIGN_STATE(self):
            return self.getToken(MiniGoParser.ASSIGN_STATE, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def function_body_container(self):
            return self.getTypedRuleContext(MiniGoParser.Function_body_containerContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_for_loop




    def array_for_loop(self):

        localctx = MiniGoParser.Array_for_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_array_for_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
            self.match(MiniGoParser.FOR)

            self.state = 595
            self.match(MiniGoParser.ID)
            self.state = 596
            self.match(MiniGoParser.COMMA)

            self.state = 597
            self.match(MiniGoParser.ID)
            self.state = 598
            self.match(MiniGoParser.ASSIGN_STATE)
            self.state = 599
            self.match(MiniGoParser.RANGE)
            self.state = 600
            self.expression(0)

            self.state = 602
            self.function_body_container()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_statement




    def break_statement(self):

        localctx = MiniGoParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            self.match(MiniGoParser.BREAK)
            self.state = 605
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_statement




    def continue_statement(self):

        localctx = MiniGoParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 607
            self.match(MiniGoParser.CONTINUE)
            self.state = 608
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def function_call(self):
            return self.getTypedRuleContext(MiniGoParser.Function_callContext,0)


        def method_call(self):
            return self.getTypedRuleContext(MiniGoParser.Method_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_statement




    def call_statement(self):

        localctx = MiniGoParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 612
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.state = 610
                self.function_call()
                pass

            elif la_ == 2:
                self.state = 611
                self.method_call()
                pass


            self.state = 614
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_statement




    def return_statement(self):

        localctx = MiniGoParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 616
            self.match(MiniGoParser.RETURN)
            self.state = 618
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 135407090353831936) != 0):
                self.state = 617
                self.expression(0)


            self.state = 620
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[18] = self.expression_sempred
        self._predicates[19] = self.expression1_sempred
        self._predicates[20] = self.expression2_sempred
        self._predicates[21] = self.expression3_sempred
        self._predicates[22] = self.expression4_sempred
        self._predicates[24] = self.expression6_sempred
        self._predicates[28] = self.temp_expression6_sempred
        self._predicates[52] = self.lhs_assignment_statement_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression1_sempred(self, localctx:Expression1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 2)
         

    def expression6_sempred(self, localctx:Expression6Context, predIndex:int):
            if predIndex == 13:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 5)
         

    def temp_expression6_sempred(self, localctx:Temp_expression6Context, predIndex:int):
            if predIndex == 16:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 3)
         

    def lhs_assignment_statement_sempred(self, localctx:Lhs_assignment_statementContext, predIndex:int):
            if predIndex == 19:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 20:
                return self.precpred(self._ctx, 1)
         




