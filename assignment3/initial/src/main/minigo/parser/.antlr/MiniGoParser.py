# Generated from d:/VisualStudioCode/PPL/assignment3/initial/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
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
        4,1,62,656,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,65,7,65,
        2,66,7,66,2,67,7,67,2,68,7,68,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,146,
        8,1,1,2,1,2,1,2,3,2,151,8,2,1,3,1,3,1,4,1,4,1,4,3,4,158,8,4,1,5,
        1,5,1,6,1,6,1,6,3,6,165,8,6,1,7,1,7,1,7,1,7,3,7,171,8,7,1,8,1,8,
        1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,3,10,187,8,
        10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,196,8,11,1,12,1,12,1,
        12,1,12,1,12,1,13,1,13,3,13,205,8,13,1,14,1,14,1,14,1,14,1,14,3,
        14,212,8,14,1,15,1,15,1,15,1,15,1,16,1,16,3,16,220,8,16,1,17,1,17,
        1,17,1,17,1,17,3,17,227,8,17,1,18,1,18,1,18,1,18,1,18,1,18,5,18,
        235,8,18,10,18,12,18,238,9,18,1,19,1,19,1,19,1,19,1,19,1,19,5,19,
        246,8,19,10,19,12,19,249,9,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,5,20,272,8,20,10,20,12,20,275,9,20,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,5,21,286,8,21,10,21,12,21,289,9,21,1,22,1,22,
        1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,5,22,303,8,22,
        10,22,12,22,306,9,22,1,23,1,23,1,23,1,23,1,23,3,23,313,8,23,1,24,
        1,24,1,24,1,24,1,24,3,24,320,8,24,1,24,1,24,1,24,1,24,1,24,1,24,
        1,24,1,24,1,24,1,24,1,24,5,24,333,8,24,10,24,12,24,336,9,24,1,25,
        1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,28,
        1,28,1,28,3,28,354,8,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,5,28,367,8,28,10,28,12,28,370,9,28,1,29,1,29,3,29,
        374,8,29,1,30,1,30,1,30,1,30,3,30,380,8,30,1,31,1,31,1,31,1,31,1,
        31,1,31,1,31,1,31,3,31,390,8,31,1,32,1,32,1,32,1,32,1,32,1,32,3,
        32,398,8,32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,3,33,409,
        8,33,1,33,1,33,1,34,1,34,1,34,3,34,416,8,34,1,34,1,34,1,34,1,35,
        1,35,1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,36,1,36,1,36,1,36,3,36,
        434,8,36,1,36,1,36,1,36,1,37,1,37,3,37,441,8,37,1,38,1,38,1,38,1,
        38,1,38,3,38,448,8,38,1,39,1,39,1,39,5,39,453,8,39,10,39,12,39,456,
        9,39,1,39,1,39,1,40,1,40,1,40,1,40,1,41,1,41,1,41,1,41,1,41,1,41,
        1,41,1,41,3,41,472,8,41,1,41,1,41,1,41,1,42,1,42,1,42,1,42,1,42,
        1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,44,1,44,1,44,1,44,
        3,44,495,8,44,1,45,1,45,1,45,1,45,1,46,1,46,1,46,1,46,1,46,1,46,
        1,46,1,46,1,46,1,47,1,47,1,47,1,47,3,47,514,8,47,1,48,1,48,1,48,
        3,48,519,8,48,1,48,1,48,1,49,1,49,1,49,1,49,1,50,1,50,3,50,529,8,
        50,1,51,1,51,1,51,1,51,1,51,3,51,536,8,51,1,52,1,52,1,52,5,52,541,
        8,52,10,52,12,52,544,9,52,1,52,1,52,1,53,1,53,1,53,1,53,1,53,1,54,
        1,54,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,5,55,
        566,8,55,10,55,12,55,569,9,55,1,56,1,56,1,56,1,56,1,57,1,57,1,57,
        1,57,1,57,1,57,1,57,3,57,582,8,57,1,57,3,57,585,8,57,1,57,1,57,1,
        58,1,58,1,58,1,58,3,58,593,8,58,1,59,1,59,1,59,1,59,1,59,1,59,1,
        59,1,59,1,60,1,60,1,60,1,61,1,61,1,61,3,61,609,8,61,1,61,1,61,1,
        62,1,62,1,62,1,62,1,63,1,63,1,63,3,63,620,8,63,1,63,1,63,1,63,1,
        63,1,63,1,63,1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,
        65,1,65,1,65,1,66,1,66,1,66,1,67,1,67,3,67,646,8,67,1,67,1,67,1,
        68,1,68,3,68,652,8,68,1,68,1,68,1,68,0,8,36,38,40,42,44,48,56,110,
        69,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,
        88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,118,120,122,
        124,126,128,130,132,134,136,0,4,2,0,18,20,54,56,1,0,9,12,1,0,53,
        54,1,0,37,42,664,0,138,1,0,0,0,2,145,1,0,0,0,4,150,1,0,0,0,6,152,
        1,0,0,0,8,157,1,0,0,0,10,159,1,0,0,0,12,161,1,0,0,0,14,170,1,0,0,
        0,16,172,1,0,0,0,18,176,1,0,0,0,20,186,1,0,0,0,22,195,1,0,0,0,24,
        197,1,0,0,0,26,204,1,0,0,0,28,211,1,0,0,0,30,213,1,0,0,0,32,219,
        1,0,0,0,34,226,1,0,0,0,36,228,1,0,0,0,38,239,1,0,0,0,40,250,1,0,
        0,0,42,276,1,0,0,0,44,290,1,0,0,0,46,312,1,0,0,0,48,319,1,0,0,0,
        50,337,1,0,0,0,52,341,1,0,0,0,54,346,1,0,0,0,56,353,1,0,0,0,58,373,
        1,0,0,0,60,379,1,0,0,0,62,389,1,0,0,0,64,397,1,0,0,0,66,399,1,0,
        0,0,68,412,1,0,0,0,70,420,1,0,0,0,72,426,1,0,0,0,74,440,1,0,0,0,
        76,447,1,0,0,0,78,449,1,0,0,0,80,459,1,0,0,0,82,463,1,0,0,0,84,476,
        1,0,0,0,86,481,1,0,0,0,88,494,1,0,0,0,90,496,1,0,0,0,92,500,1,0,
        0,0,94,513,1,0,0,0,96,515,1,0,0,0,98,522,1,0,0,0,100,528,1,0,0,0,
        102,535,1,0,0,0,104,537,1,0,0,0,106,547,1,0,0,0,108,552,1,0,0,0,
        110,554,1,0,0,0,112,570,1,0,0,0,114,574,1,0,0,0,116,592,1,0,0,0,
        118,594,1,0,0,0,120,602,1,0,0,0,122,608,1,0,0,0,124,612,1,0,0,0,
        126,616,1,0,0,0,128,627,1,0,0,0,130,637,1,0,0,0,132,640,1,0,0,0,
        134,645,1,0,0,0,136,649,1,0,0,0,138,139,3,2,1,0,139,140,5,0,0,1,
        140,1,1,0,0,0,141,142,3,64,32,0,142,143,3,2,1,0,143,146,1,0,0,0,
        144,146,3,64,32,0,145,141,1,0,0,0,145,144,1,0,0,0,146,3,1,0,0,0,
        147,151,3,6,3,0,148,151,3,18,9,0,149,151,3,24,12,0,150,147,1,0,0,
        0,150,148,1,0,0,0,150,149,1,0,0,0,151,5,1,0,0,0,152,153,7,0,0,0,
        153,7,1,0,0,0,154,158,5,53,0,0,155,158,3,10,5,0,156,158,3,12,6,0,
        157,154,1,0,0,0,157,155,1,0,0,0,157,156,1,0,0,0,158,9,1,0,0,0,159,
        160,7,1,0,0,160,11,1,0,0,0,161,164,3,14,7,0,162,165,5,53,0,0,163,
        165,3,10,5,0,164,162,1,0,0,0,164,163,1,0,0,0,165,13,1,0,0,0,166,
        167,3,16,8,0,167,168,3,14,7,0,168,171,1,0,0,0,169,171,3,16,8,0,170,
        166,1,0,0,0,170,169,1,0,0,0,171,15,1,0,0,0,172,173,5,48,0,0,173,
        174,7,2,0,0,174,175,5,49,0,0,175,17,1,0,0,0,176,177,3,12,6,0,177,
        178,5,46,0,0,178,179,3,20,10,0,179,180,5,47,0,0,180,19,1,0,0,0,181,
        182,3,22,11,0,182,183,5,50,0,0,183,184,3,20,10,0,184,187,1,0,0,0,
        185,187,3,22,11,0,186,181,1,0,0,0,186,185,1,0,0,0,187,21,1,0,0,0,
        188,196,5,53,0,0,189,196,3,6,3,0,190,196,3,24,12,0,191,192,5,46,
        0,0,192,193,3,20,10,0,193,194,5,47,0,0,194,196,1,0,0,0,195,188,1,
        0,0,0,195,189,1,0,0,0,195,190,1,0,0,0,195,191,1,0,0,0,196,23,1,0,
        0,0,197,198,5,53,0,0,198,199,5,46,0,0,199,200,3,26,13,0,200,201,
        5,47,0,0,201,25,1,0,0,0,202,205,3,28,14,0,203,205,1,0,0,0,204,202,
        1,0,0,0,204,203,1,0,0,0,205,27,1,0,0,0,206,207,3,30,15,0,207,208,
        5,50,0,0,208,209,3,28,14,0,209,212,1,0,0,0,210,212,3,30,15,0,211,
        206,1,0,0,0,211,210,1,0,0,0,212,29,1,0,0,0,213,214,5,53,0,0,214,
        215,5,52,0,0,215,216,3,36,18,0,216,31,1,0,0,0,217,220,3,34,17,0,
        218,220,1,0,0,0,219,217,1,0,0,0,219,218,1,0,0,0,220,33,1,0,0,0,221,
        222,3,36,18,0,222,223,5,50,0,0,223,224,3,34,17,0,224,227,1,0,0,0,
        225,227,3,36,18,0,226,221,1,0,0,0,226,225,1,0,0,0,227,35,1,0,0,0,
        228,229,6,18,-1,0,229,230,3,38,19,0,230,236,1,0,0,0,231,232,10,2,
        0,0,232,233,5,34,0,0,233,235,3,38,19,0,234,231,1,0,0,0,235,238,1,
        0,0,0,236,234,1,0,0,0,236,237,1,0,0,0,237,37,1,0,0,0,238,236,1,0,
        0,0,239,240,6,19,-1,0,240,241,3,40,20,0,241,247,1,0,0,0,242,243,
        10,2,0,0,243,244,5,33,0,0,244,246,3,40,20,0,245,242,1,0,0,0,246,
        249,1,0,0,0,247,245,1,0,0,0,247,248,1,0,0,0,248,39,1,0,0,0,249,247,
        1,0,0,0,250,251,6,20,-1,0,251,252,3,42,21,0,252,273,1,0,0,0,253,
        254,10,7,0,0,254,255,5,27,0,0,255,272,3,42,21,0,256,257,10,6,0,0,
        257,258,5,28,0,0,258,272,3,42,21,0,259,260,10,5,0,0,260,261,5,29,
        0,0,261,272,3,42,21,0,262,263,10,4,0,0,263,264,5,30,0,0,264,272,
        3,42,21,0,265,266,10,3,0,0,266,267,5,31,0,0,267,272,3,42,21,0,268,
        269,10,2,0,0,269,270,5,32,0,0,270,272,3,42,21,0,271,253,1,0,0,0,
        271,256,1,0,0,0,271,259,1,0,0,0,271,262,1,0,0,0,271,265,1,0,0,0,
        271,268,1,0,0,0,272,275,1,0,0,0,273,271,1,0,0,0,273,274,1,0,0,0,
        274,41,1,0,0,0,275,273,1,0,0,0,276,277,6,21,-1,0,277,278,3,44,22,
        0,278,287,1,0,0,0,279,280,10,3,0,0,280,281,5,22,0,0,281,286,3,44,
        22,0,282,283,10,2,0,0,283,284,5,23,0,0,284,286,3,44,22,0,285,279,
        1,0,0,0,285,282,1,0,0,0,286,289,1,0,0,0,287,285,1,0,0,0,287,288,
        1,0,0,0,288,43,1,0,0,0,289,287,1,0,0,0,290,291,6,22,-1,0,291,292,
        3,46,23,0,292,304,1,0,0,0,293,294,10,4,0,0,294,295,5,24,0,0,295,
        303,3,46,23,0,296,297,10,3,0,0,297,298,5,25,0,0,298,303,3,46,23,
        0,299,300,10,2,0,0,300,301,5,26,0,0,301,303,3,46,23,0,302,293,1,
        0,0,0,302,296,1,0,0,0,302,299,1,0,0,0,303,306,1,0,0,0,304,302,1,
        0,0,0,304,305,1,0,0,0,305,45,1,0,0,0,306,304,1,0,0,0,307,308,5,35,
        0,0,308,313,3,46,23,0,309,310,5,23,0,0,310,313,3,46,23,0,311,313,
        3,48,24,0,312,307,1,0,0,0,312,309,1,0,0,0,312,311,1,0,0,0,313,47,
        1,0,0,0,314,315,6,24,-1,0,315,320,3,52,26,0,316,320,5,53,0,0,317,
        320,3,4,2,0,318,320,3,50,25,0,319,314,1,0,0,0,319,316,1,0,0,0,319,
        317,1,0,0,0,319,318,1,0,0,0,320,334,1,0,0,0,321,322,10,7,0,0,322,
        323,5,48,0,0,323,324,3,36,18,0,324,325,5,49,0,0,325,333,1,0,0,0,
        326,327,10,6,0,0,327,328,5,43,0,0,328,333,5,53,0,0,329,330,10,5,
        0,0,330,331,5,43,0,0,331,333,3,52,26,0,332,321,1,0,0,0,332,326,1,
        0,0,0,332,329,1,0,0,0,333,336,1,0,0,0,334,332,1,0,0,0,334,335,1,
        0,0,0,335,49,1,0,0,0,336,334,1,0,0,0,337,338,5,44,0,0,338,339,3,
        36,18,0,339,340,5,45,0,0,340,51,1,0,0,0,341,342,5,53,0,0,342,343,
        5,44,0,0,343,344,3,32,16,0,344,345,5,45,0,0,345,53,1,0,0,0,346,347,
        3,56,28,0,347,348,5,43,0,0,348,349,3,52,26,0,349,55,1,0,0,0,350,
        351,6,28,-1,0,351,354,3,52,26,0,352,354,5,53,0,0,353,350,1,0,0,0,
        353,352,1,0,0,0,354,368,1,0,0,0,355,356,10,5,0,0,356,357,5,48,0,
        0,357,358,3,36,18,0,358,359,5,49,0,0,359,367,1,0,0,0,360,361,10,
        4,0,0,361,362,5,43,0,0,362,367,5,53,0,0,363,364,10,3,0,0,364,365,
        5,43,0,0,365,367,3,52,26,0,366,355,1,0,0,0,366,360,1,0,0,0,366,363,
        1,0,0,0,367,370,1,0,0,0,368,366,1,0,0,0,368,369,1,0,0,0,369,57,1,
        0,0,0,370,368,1,0,0,0,371,374,3,60,30,0,372,374,1,0,0,0,373,371,
        1,0,0,0,373,372,1,0,0,0,374,59,1,0,0,0,375,376,3,62,31,0,376,377,
        3,60,30,0,377,380,1,0,0,0,378,380,3,62,31,0,379,375,1,0,0,0,379,
        378,1,0,0,0,380,61,1,0,0,0,381,390,3,64,32,0,382,390,3,106,53,0,
        383,390,3,114,57,0,384,390,3,122,61,0,385,390,3,130,65,0,386,390,
        3,132,66,0,387,390,3,134,67,0,388,390,3,136,68,0,389,381,1,0,0,0,
        389,382,1,0,0,0,389,383,1,0,0,0,389,384,1,0,0,0,389,385,1,0,0,0,
        389,386,1,0,0,0,389,387,1,0,0,0,389,388,1,0,0,0,390,63,1,0,0,0,391,
        398,3,66,33,0,392,398,3,70,35,0,393,398,3,72,36,0,394,398,3,82,41,
        0,395,398,3,86,43,0,396,398,3,92,46,0,397,391,1,0,0,0,397,392,1,
        0,0,0,397,393,1,0,0,0,397,394,1,0,0,0,397,395,1,0,0,0,397,396,1,
        0,0,0,398,65,1,0,0,0,399,400,5,14,0,0,400,408,5,53,0,0,401,402,3,
        8,4,0,402,403,5,36,0,0,403,404,3,36,18,0,404,409,1,0,0,0,405,409,
        3,8,4,0,406,407,5,36,0,0,407,409,3,36,18,0,408,401,1,0,0,0,408,405,
        1,0,0,0,408,406,1,0,0,0,409,410,1,0,0,0,410,411,5,51,0,0,411,67,
        1,0,0,0,412,413,5,14,0,0,413,415,5,53,0,0,414,416,3,8,4,0,415,414,
        1,0,0,0,415,416,1,0,0,0,416,417,1,0,0,0,417,418,5,36,0,0,418,419,
        3,36,18,0,419,69,1,0,0,0,420,421,5,13,0,0,421,422,5,53,0,0,422,423,
        5,36,0,0,423,424,3,36,18,0,424,425,5,51,0,0,425,71,1,0,0,0,426,427,
        5,5,0,0,427,428,5,53,0,0,428,429,5,44,0,0,429,430,3,74,37,0,430,
        431,5,45,0,0,431,433,1,0,0,0,432,434,3,8,4,0,433,432,1,0,0,0,433,
        434,1,0,0,0,434,435,1,0,0,0,435,436,3,80,40,0,436,437,5,51,0,0,437,
        73,1,0,0,0,438,441,3,76,38,0,439,441,1,0,0,0,440,438,1,0,0,0,440,
        439,1,0,0,0,441,75,1,0,0,0,442,443,3,78,39,0,443,444,5,50,0,0,444,
        445,3,76,38,0,445,448,1,0,0,0,446,448,3,78,39,0,447,442,1,0,0,0,
        447,446,1,0,0,0,448,77,1,0,0,0,449,454,5,53,0,0,450,451,5,50,0,0,
        451,453,5,53,0,0,452,450,1,0,0,0,453,456,1,0,0,0,454,452,1,0,0,0,
        454,455,1,0,0,0,455,457,1,0,0,0,456,454,1,0,0,0,457,458,3,8,4,0,
        458,79,1,0,0,0,459,460,5,46,0,0,460,461,3,60,30,0,461,462,5,47,0,
        0,462,81,1,0,0,0,463,464,5,5,0,0,464,465,3,84,42,0,465,466,5,53,
        0,0,466,467,5,44,0,0,467,468,3,74,37,0,468,469,5,45,0,0,469,471,
        1,0,0,0,470,472,3,8,4,0,471,470,1,0,0,0,471,472,1,0,0,0,472,473,
        1,0,0,0,473,474,3,80,40,0,474,475,5,51,0,0,475,83,1,0,0,0,476,477,
        5,44,0,0,477,478,5,53,0,0,478,479,5,53,0,0,479,480,5,45,0,0,480,
        85,1,0,0,0,481,482,5,6,0,0,482,483,5,53,0,0,483,484,5,7,0,0,484,
        485,5,46,0,0,485,486,3,88,44,0,486,487,5,47,0,0,487,488,1,0,0,0,
        488,489,5,51,0,0,489,87,1,0,0,0,490,491,3,90,45,0,491,492,3,88,44,
        0,492,495,1,0,0,0,493,495,3,90,45,0,494,490,1,0,0,0,494,493,1,0,
        0,0,495,89,1,0,0,0,496,497,5,53,0,0,497,498,3,8,4,0,498,499,5,51,
        0,0,499,91,1,0,0,0,500,501,5,6,0,0,501,502,5,53,0,0,502,503,5,8,
        0,0,503,504,5,46,0,0,504,505,3,94,47,0,505,506,5,47,0,0,506,507,
        1,0,0,0,507,508,5,51,0,0,508,93,1,0,0,0,509,510,3,96,48,0,510,511,
        3,94,47,0,511,514,1,0,0,0,512,514,3,96,48,0,513,509,1,0,0,0,513,
        512,1,0,0,0,514,95,1,0,0,0,515,516,5,53,0,0,516,518,3,98,49,0,517,
        519,3,8,4,0,518,517,1,0,0,0,518,519,1,0,0,0,519,520,1,0,0,0,520,
        521,5,51,0,0,521,97,1,0,0,0,522,523,5,44,0,0,523,524,3,100,50,0,
        524,525,5,45,0,0,525,99,1,0,0,0,526,529,3,102,51,0,527,529,1,0,0,
        0,528,526,1,0,0,0,528,527,1,0,0,0,529,101,1,0,0,0,530,531,3,104,
        52,0,531,532,5,50,0,0,532,533,3,102,51,0,533,536,1,0,0,0,534,536,
        3,104,52,0,535,530,1,0,0,0,535,534,1,0,0,0,536,103,1,0,0,0,537,542,
        5,53,0,0,538,539,5,50,0,0,539,541,5,53,0,0,540,538,1,0,0,0,541,544,
        1,0,0,0,542,540,1,0,0,0,542,543,1,0,0,0,543,545,1,0,0,0,544,542,
        1,0,0,0,545,546,3,8,4,0,546,105,1,0,0,0,547,548,3,110,55,0,548,549,
        3,108,54,0,549,550,3,36,18,0,550,551,5,51,0,0,551,107,1,0,0,0,552,
        553,7,3,0,0,553,109,1,0,0,0,554,555,6,55,-1,0,555,556,5,53,0,0,556,
        567,1,0,0,0,557,558,10,2,0,0,558,559,5,48,0,0,559,560,3,36,18,0,
        560,561,5,49,0,0,561,566,1,0,0,0,562,563,10,1,0,0,563,564,5,43,0,
        0,564,566,5,53,0,0,565,557,1,0,0,0,565,562,1,0,0,0,566,569,1,0,0,
        0,567,565,1,0,0,0,567,568,1,0,0,0,568,111,1,0,0,0,569,567,1,0,0,
        0,570,571,5,53,0,0,571,572,3,108,54,0,572,573,3,36,18,0,573,113,
        1,0,0,0,574,575,5,1,0,0,575,576,5,44,0,0,576,577,3,36,18,0,577,578,
        5,45,0,0,578,579,1,0,0,0,579,581,3,80,40,0,580,582,3,116,58,0,581,
        580,1,0,0,0,581,582,1,0,0,0,582,584,1,0,0,0,583,585,3,120,60,0,584,
        583,1,0,0,0,584,585,1,0,0,0,585,586,1,0,0,0,586,587,5,51,0,0,587,
        115,1,0,0,0,588,589,3,118,59,0,589,590,3,116,58,0,590,593,1,0,0,
        0,591,593,3,118,59,0,592,588,1,0,0,0,592,591,1,0,0,0,593,117,1,0,
        0,0,594,595,5,2,0,0,595,596,5,1,0,0,596,597,5,44,0,0,597,598,3,36,
        18,0,598,599,5,45,0,0,599,600,1,0,0,0,600,601,3,80,40,0,601,119,
        1,0,0,0,602,603,5,2,0,0,603,604,3,80,40,0,604,121,1,0,0,0,605,609,
        3,128,64,0,606,609,3,126,63,0,607,609,3,124,62,0,608,605,1,0,0,0,
        608,606,1,0,0,0,608,607,1,0,0,0,609,610,1,0,0,0,610,611,5,51,0,0,
        611,123,1,0,0,0,612,613,5,3,0,0,613,614,3,36,18,0,614,615,3,80,40,
        0,615,125,1,0,0,0,616,619,5,3,0,0,617,620,3,68,34,0,618,620,3,112,
        56,0,619,617,1,0,0,0,619,618,1,0,0,0,620,621,1,0,0,0,621,622,5,51,
        0,0,622,623,3,36,18,0,623,624,5,51,0,0,624,625,3,112,56,0,625,626,
        3,80,40,0,626,127,1,0,0,0,627,628,5,3,0,0,628,629,5,53,0,0,629,630,
        5,50,0,0,630,631,5,53,0,0,631,632,5,37,0,0,632,633,5,17,0,0,633,
        634,3,36,18,0,634,635,1,0,0,0,635,636,3,80,40,0,636,129,1,0,0,0,
        637,638,5,16,0,0,638,639,5,51,0,0,639,131,1,0,0,0,640,641,5,15,0,
        0,641,642,5,51,0,0,642,133,1,0,0,0,643,646,3,52,26,0,644,646,3,54,
        27,0,645,643,1,0,0,0,645,644,1,0,0,0,646,647,1,0,0,0,647,648,5,51,
        0,0,648,135,1,0,0,0,649,651,5,4,0,0,650,652,3,36,18,0,651,650,1,
        0,0,0,651,652,1,0,0,0,652,653,1,0,0,0,653,654,5,51,0,0,654,137,1,
        0,0,0,52,145,150,157,164,170,186,195,204,211,219,226,236,247,271,
        273,285,287,302,304,312,319,332,334,353,366,368,373,379,389,397,
        408,415,433,440,447,454,471,494,513,518,528,535,542,565,567,581,
        584,592,608,619,645,651
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
    RULE_list_function_parameter = 37
    RULE_list_function_parameter_prime = 38
    RULE_list_function_parameter_element = 39
    RULE_function_body_container = 40
    RULE_method_declared = 41
    RULE_receiver_container = 42
    RULE_struct_declared = 43
    RULE_struct_declared_body = 44
    RULE_struct_declared_body_element = 45
    RULE_interface_declared = 46
    RULE_interface_declared_body = 47
    RULE_interface_declared_element = 48
    RULE_interface_parameter_container = 49
    RULE_list_interface_parameter = 50
    RULE_list_interface_parameter_prime = 51
    RULE_list_interface_parameter_element = 52
    RULE_assignment_statement = 53
    RULE_assignment_operator = 54
    RULE_lhs_assignment_statement = 55
    RULE_assignment_statement_without_semi_for_loop = 56
    RULE_if_statement = 57
    RULE_else_if_clause = 58
    RULE_else_if_clause_content = 59
    RULE_else_clause = 60
    RULE_for_statement = 61
    RULE_basic_for_loop = 62
    RULE_initialization_for_loop = 63
    RULE_array_for_loop = 64
    RULE_break_statement = 65
    RULE_continue_statement = 66
    RULE_call_statement = 67
    RULE_return_statement = 68

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
                   "constants_declared", "function_declared", "list_function_parameter", 
                   "list_function_parameter_prime", "list_function_parameter_element", 
                   "function_body_container", "method_declared", "receiver_container", 
                   "struct_declared", "struct_declared_body", "struct_declared_body_element", 
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
            self.state = 138
            self.declared_statement_list()
            self.state = 139
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
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.declared_statement()

                self.state = 142
                self.declared_statement_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
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
            self.state = 150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18, 19, 20, 54, 55, 56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.literal_primitive()
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.array_lit_instance()
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 3)
                self.state = 149
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
            self.state = 152
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
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.match(MiniGoParser.ID)
                pass
            elif token in [9, 10, 11, 12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.primitive_type()
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 3)
                self.state = 156
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
            self.state = 159
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
            self.state = 161
            self.array_dimention()
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.state = 162
                self.match(MiniGoParser.ID)
                pass
            elif token in [9, 10, 11, 12]:
                self.state = 163
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
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.array_dimention_element()

                self.state = 167
                self.array_dimention()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
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
            self.state = 172
            self.match(MiniGoParser.LBRACK)
            self.state = 173
            _la = self._input.LA(1)
            if not(_la==53 or _la==54):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 174
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
            self.state = 176
            self.array_type()
            self.state = 177
            self.match(MiniGoParser.LBRACE)
            self.state = 178
            self.list_array_value()
            self.state = 179
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
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.list_array_value_element()
                self.state = 182
                self.match(MiniGoParser.COMMA)

                self.state = 183
                self.list_array_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
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
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.literal_primitive()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 190
                self.struct_lit_instance()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 191
                self.match(MiniGoParser.LBRACE)
                self.state = 192
                self.list_array_value()
                self.state = 193
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
            self.state = 197
            self.match(MiniGoParser.ID)
            self.state = 198
            self.match(MiniGoParser.LBRACE)
            self.state = 199
            self.struct_lit_instance_body()
            self.state = 200
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
            self.state = 204
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
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
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.struct_lit_instance_body_element()
                self.state = 207
                self.match(MiniGoParser.COMMA)
                self.state = 208
                self.struct_lit_instance_body_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
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
            self.state = 213
            self.match(MiniGoParser.ID)
            self.state = 214
            self.match(MiniGoParser.COLON)
            self.state = 215
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
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18, 19, 20, 23, 35, 44, 48, 53, 54, 55, 56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
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
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.expression(0)
                self.state = 222
                self.match(MiniGoParser.COMMA)
                self.state = 223
                self.list_expression_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
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
            self.state = 229
            self.expression1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 236
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 231
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 232
                    self.match(MiniGoParser.OR)
                    self.state = 233
                    self.expression1(0) 
                self.state = 238
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
            self.state = 240
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 247
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 242
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 243
                    self.match(MiniGoParser.AND)
                    self.state = 244
                    self.expression2(0) 
                self.state = 249
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
            self.state = 251
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 273
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 271
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 253
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 254
                        self.match(MiniGoParser.EQUAL)
                        self.state = 255
                        self.expression3(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 256
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 257
                        self.match(MiniGoParser.NOT_EQUAL)
                        self.state = 258
                        self.expression3(0)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 259
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 260
                        self.match(MiniGoParser.LESS)
                        self.state = 261
                        self.expression3(0)
                        pass

                    elif la_ == 4:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 262
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 263
                        self.match(MiniGoParser.LESS_EQUAL)
                        self.state = 264
                        self.expression3(0)
                        pass

                    elif la_ == 5:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 265
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 266
                        self.match(MiniGoParser.GREATER)
                        self.state = 267
                        self.expression3(0)
                        pass

                    elif la_ == 6:
                        localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                        self.state = 268
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 269
                        self.match(MiniGoParser.GREATER_EQUAL)
                        self.state = 270
                        self.expression3(0)
                        pass

             
                self.state = 275
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
            self.state = 277
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 287
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 285
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                        self.state = 279
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 280
                        self.match(MiniGoParser.ADD)
                        self.state = 281
                        self.expression4(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                        self.state = 282
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 283
                        self.match(MiniGoParser.SUB)
                        self.state = 284
                        self.expression4(0)
                        pass

             
                self.state = 289
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
            self.state = 291
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 304
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 302
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                        self.state = 293
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 294
                        self.match(MiniGoParser.MUL)
                        self.state = 295
                        self.expression5()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                        self.state = 296
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 297
                        self.match(MiniGoParser.DIV)
                        self.state = 298
                        self.expression5()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                        self.state = 299
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 300
                        self.match(MiniGoParser.MOD)
                        self.state = 301
                        self.expression5()
                        pass

             
                self.state = 306
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
            self.state = 312
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.match(MiniGoParser.NOT)
                self.state = 308
                self.expression5()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
                self.match(MiniGoParser.SUB)
                self.state = 310
                self.expression5()
                pass
            elif token in [18, 19, 20, 44, 48, 53, 54, 55, 56]:
                self.enterOuterAlt(localctx, 3)
                self.state = 311
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
            self.state = 319
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 315
                self.function_call()
                pass

            elif la_ == 2:
                self.state = 316
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.state = 317
                self.literal()
                pass

            elif la_ == 4:
                self.state = 318
                self.expression7()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 334
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 332
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 321
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")

                        self.state = 322
                        self.match(MiniGoParser.LBRACK)
                        self.state = 323
                        self.expression(0)
                        self.state = 324
                        self.match(MiniGoParser.RBRACK)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 326
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 327
                        self.match(MiniGoParser.DOT)
                        self.state = 328
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 329
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 330
                        self.match(MiniGoParser.DOT)

                        self.state = 331
                        self.function_call()
                        pass

             
                self.state = 336
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
            self.state = 337
            self.match(MiniGoParser.LPAREN)
            self.state = 338
            self.expression(0)
            self.state = 339
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
            self.state = 341
            self.match(MiniGoParser.ID)
            self.state = 342
            self.match(MiniGoParser.LPAREN)
            self.state = 343
            self.list_expression()
            self.state = 344
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
            self.state = 346
            self.temp_expression6(0)
            self.state = 347
            self.match(MiniGoParser.DOT)

            self.state = 348
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
            self.state = 353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 351
                self.function_call()
                pass

            elif la_ == 2:
                self.state = 352
                self.match(MiniGoParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 368
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 366
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Temp_expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_temp_expression6)
                        self.state = 355
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")

                        self.state = 356
                        self.match(MiniGoParser.LBRACK)
                        self.state = 357
                        self.expression(0)
                        self.state = 358
                        self.match(MiniGoParser.RBRACK)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Temp_expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_temp_expression6)
                        self.state = 360
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 361
                        self.match(MiniGoParser.DOT)
                        self.state = 362
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Temp_expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_temp_expression6)
                        self.state = 363
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 364
                        self.match(MiniGoParser.DOT)
                        self.state = 365
                        self.function_call()
                        pass

             
                self.state = 370
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
            self.state = 373
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 4, 5, 6, 13, 14, 15, 16, 53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 371
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
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.statement()

                self.state = 376
                self.list_statement_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
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
            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.declared_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 382
                self.assignment_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 383
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 384
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 385
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 386
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 387
                self.call_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 388
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
            self.state = 397
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 391
                self.variables_declared()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 392
                self.constants_declared()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 393
                self.function_declared()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 394
                self.method_declared()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 395
                self.struct_declared()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 396
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
            self.state = 399
            self.match(MiniGoParser.VAR)
            self.state = 400
            self.match(MiniGoParser.ID)
            self.state = 408
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 401
                self.mytype()
                self.state = 402
                self.match(MiniGoParser.ASSIGN)
                self.state = 403
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 405
                self.mytype()
                pass

            elif la_ == 3:
                self.state = 406
                self.match(MiniGoParser.ASSIGN)
                self.state = 407
                self.expression(0)
                pass


            self.state = 410
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
            self.state = 412
            self.match(MiniGoParser.VAR)
            self.state = 413
            self.match(MiniGoParser.ID)
            self.state = 415
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9288674231459328) != 0):
                self.state = 414
                self.mytype()


            self.state = 417
            self.match(MiniGoParser.ASSIGN)
            self.state = 418
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
            self.state = 420
            self.match(MiniGoParser.CONST)
            self.state = 421
            self.match(MiniGoParser.ID)
            self.state = 422
            self.match(MiniGoParser.ASSIGN)
            self.state = 423
            self.expression(0)
            self.state = 424
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

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def list_function_parameter(self):
            return self.getTypedRuleContext(MiniGoParser.List_function_parameterContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

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
            self.state = 426
            self.match(MiniGoParser.FUNC)
            self.state = 427
            self.match(MiniGoParser.ID)

            self.state = 428
            self.match(MiniGoParser.LPAREN)
            self.state = 429
            self.list_function_parameter()
            self.state = 430
            self.match(MiniGoParser.RPAREN)
            self.state = 433
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9288674231459328) != 0):
                self.state = 432
                self.mytype()


            self.state = 435
            self.function_body_container()
            self.state = 436
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_function_parameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_function_parameter_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_function_parameter_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_function_parameter




    def list_function_parameter(self):

        localctx = MiniGoParser.List_function_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_list_function_parameter)
        try:
            self.state = 440
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 438
                self.list_function_parameter_prime()
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


    class List_function_parameter_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_function_parameter_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_function_parameter_elementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_function_parameter_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_function_parameter_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_function_parameter_prime




    def list_function_parameter_prime(self):

        localctx = MiniGoParser.List_function_parameter_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_list_function_parameter_prime)
        try:
            self.state = 447
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 442
                self.list_function_parameter_element()
                self.state = 443
                self.match(MiniGoParser.COMMA)
                self.state = 444
                self.list_function_parameter_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 446
                self.list_function_parameter_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_function_parameter_elementContext(ParserRuleContext):
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
            return MiniGoParser.RULE_list_function_parameter_element




    def list_function_parameter_element(self):

        localctx = MiniGoParser.List_function_parameter_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_list_function_parameter_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.match(MiniGoParser.ID)
            self.state = 454
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 450
                self.match(MiniGoParser.COMMA)
                self.state = 451
                self.match(MiniGoParser.ID)
                self.state = 456
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 457
            self.mytype()
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
        self.enterRule(localctx, 80, self.RULE_function_body_container)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.match(MiniGoParser.LBRACE)
            self.state = 460
            self.list_statement_prime()
            self.state = 461
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


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def list_function_parameter(self):
            return self.getTypedRuleContext(MiniGoParser.List_function_parameterContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def function_body_container(self):
            return self.getTypedRuleContext(MiniGoParser.Function_body_containerContext,0)


        def mytype(self):
            return self.getTypedRuleContext(MiniGoParser.MytypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_declared




    def method_declared(self):

        localctx = MiniGoParser.Method_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_method_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            self.match(MiniGoParser.FUNC)

            self.state = 464
            self.receiver_container()
            self.state = 465
            self.match(MiniGoParser.ID)

            self.state = 466
            self.match(MiniGoParser.LPAREN)
            self.state = 467
            self.list_function_parameter()
            self.state = 468
            self.match(MiniGoParser.RPAREN)
            self.state = 471
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9288674231459328) != 0):
                self.state = 470
                self.mytype()


            self.state = 473
            self.function_body_container()
            self.state = 474
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
        self.enterRule(localctx, 84, self.RULE_receiver_container)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.match(MiniGoParser.LPAREN)
            self.state = 477
            self.match(MiniGoParser.ID)
            self.state = 478
            self.match(MiniGoParser.ID)
            self.state = 479
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
        self.enterRule(localctx, 86, self.RULE_struct_declared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self.match(MiniGoParser.TYPE)
            self.state = 482
            self.match(MiniGoParser.ID)
            self.state = 483
            self.match(MiniGoParser.STRUCT)

            self.state = 484
            self.match(MiniGoParser.LBRACE)
            self.state = 485
            self.struct_declared_body()
            self.state = 486
            self.match(MiniGoParser.RBRACE)
            self.state = 488
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
        self.enterRule(localctx, 88, self.RULE_struct_declared_body)
        try:
            self.state = 494
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 490
                self.struct_declared_body_element()

                self.state = 491
                self.struct_declared_body()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 493
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
        self.enterRule(localctx, 90, self.RULE_struct_declared_body_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
            self.match(MiniGoParser.ID)

            self.state = 497
            self.mytype()
            self.state = 498
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
        self.enterRule(localctx, 92, self.RULE_interface_declared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            self.match(MiniGoParser.TYPE)
            self.state = 501
            self.match(MiniGoParser.ID)
            self.state = 502
            self.match(MiniGoParser.INTERFACE)

            self.state = 503
            self.match(MiniGoParser.LBRACE)
            self.state = 504
            self.interface_declared_body()
            self.state = 505
            self.match(MiniGoParser.RBRACE)
            self.state = 507
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
        self.enterRule(localctx, 94, self.RULE_interface_declared_body)
        try:
            self.state = 513
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 509
                self.interface_declared_element()

                self.state = 510
                self.interface_declared_body()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 512
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
        self.enterRule(localctx, 96, self.RULE_interface_declared_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.match(MiniGoParser.ID)

            self.state = 516
            self.interface_parameter_container()
            self.state = 518
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9288674231459328) != 0):
                self.state = 517
                self.mytype()


            self.state = 520
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
        self.enterRule(localctx, 98, self.RULE_interface_parameter_container)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
            self.match(MiniGoParser.LPAREN)
            self.state = 523
            self.list_interface_parameter()
            self.state = 524
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
        self.enterRule(localctx, 100, self.RULE_list_interface_parameter)
        try:
            self.state = 528
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 526
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
        self.enterRule(localctx, 102, self.RULE_list_interface_parameter_prime)
        try:
            self.state = 535
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 530
                self.list_interface_parameter_element()
                self.state = 531
                self.match(MiniGoParser.COMMA)
                self.state = 532
                self.list_interface_parameter_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 534
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
        self.enterRule(localctx, 104, self.RULE_list_interface_parameter_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 537
            self.match(MiniGoParser.ID)
            self.state = 542
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 538
                self.match(MiniGoParser.COMMA)
                self.state = 539
                self.match(MiniGoParser.ID)
                self.state = 544
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 545
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
        self.enterRule(localctx, 106, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
            self.lhs_assignment_statement(0)

            self.state = 548
            self.assignment_operator()

            self.state = 549
            self.expression(0)
            self.state = 550
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
        self.enterRule(localctx, 108, self.RULE_assignment_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 552
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
        _startState = 110
        self.enterRecursionRule(localctx, 110, self.RULE_lhs_assignment_statement, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 555
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 567
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 565
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Lhs_assignment_statementContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs_assignment_statement)
                        self.state = 557
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                        self.state = 558
                        self.match(MiniGoParser.LBRACK)
                        self.state = 559
                        self.expression(0)
                        self.state = 560
                        self.match(MiniGoParser.RBRACK)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Lhs_assignment_statementContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs_assignment_statement)
                        self.state = 562
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 563
                        self.match(MiniGoParser.DOT)
                        self.state = 564
                        self.match(MiniGoParser.ID)
                        pass

             
                self.state = 569
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

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
        self.enterRule(localctx, 112, self.RULE_assignment_statement_without_semi_for_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
            self.match(MiniGoParser.ID)

            self.state = 571
            self.assignment_operator()

            self.state = 572
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
        self.enterRule(localctx, 114, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            self.match(MiniGoParser.IF)

            self.state = 575
            self.match(MiniGoParser.LPAREN)
            self.state = 576
            self.expression(0)
            self.state = 577
            self.match(MiniGoParser.RPAREN)

            self.state = 579
            self.function_body_container()
            self.state = 581
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 580
                self.else_if_clause()


            self.state = 584
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 583
                self.else_clause()


            self.state = 586
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
        self.enterRule(localctx, 116, self.RULE_else_if_clause)
        try:
            self.state = 592
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 588
                self.else_if_clause_content()
                self.state = 589
                self.else_if_clause()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 591
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
        self.enterRule(localctx, 118, self.RULE_else_if_clause_content)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
            self.match(MiniGoParser.ELSE)
            self.state = 595
            self.match(MiniGoParser.IF)

            self.state = 596
            self.match(MiniGoParser.LPAREN)
            self.state = 597
            self.expression(0)
            self.state = 598
            self.match(MiniGoParser.RPAREN)

            self.state = 600
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
        self.enterRule(localctx, 120, self.RULE_else_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 602
            self.match(MiniGoParser.ELSE)
            self.state = 603
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
        self.enterRule(localctx, 122, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 608
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.state = 605
                self.array_for_loop()
                pass

            elif la_ == 2:
                self.state = 606
                self.initialization_for_loop()
                pass

            elif la_ == 3:
                self.state = 607
                self.basic_for_loop()
                pass


            self.state = 610
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
        self.enterRule(localctx, 124, self.RULE_basic_for_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 612
            self.match(MiniGoParser.FOR)
            self.state = 613
            self.expression(0)

            self.state = 614
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
        self.enterRule(localctx, 126, self.RULE_initialization_for_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 616
            self.match(MiniGoParser.FOR)
            self.state = 619
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.state = 617
                self.variables_declared_without_semi_for_loop()
                pass
            elif token in [53]:
                self.state = 618
                self.assignment_statement_without_semi_for_loop()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 621
            self.match(MiniGoParser.SEMICOLON)

            self.state = 622
            self.expression(0)
            self.state = 623
            self.match(MiniGoParser.SEMICOLON)

            self.state = 624
            self.assignment_statement_without_semi_for_loop()

            self.state = 625
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
        self.enterRule(localctx, 128, self.RULE_array_for_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 627
            self.match(MiniGoParser.FOR)

            self.state = 628
            self.match(MiniGoParser.ID)
            self.state = 629
            self.match(MiniGoParser.COMMA)

            self.state = 630
            self.match(MiniGoParser.ID)
            self.state = 631
            self.match(MiniGoParser.ASSIGN_STATE)
            self.state = 632
            self.match(MiniGoParser.RANGE)
            self.state = 633
            self.expression(0)

            self.state = 635
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
        self.enterRule(localctx, 130, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 637
            self.match(MiniGoParser.BREAK)
            self.state = 638
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
        self.enterRule(localctx, 132, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 640
            self.match(MiniGoParser.CONTINUE)
            self.state = 641
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
        self.enterRule(localctx, 134, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 645
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 643
                self.function_call()
                pass

            elif la_ == 2:
                self.state = 644
                self.method_call()
                pass


            self.state = 647
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
        self.enterRule(localctx, 136, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 649
            self.match(MiniGoParser.RETURN)
            self.state = 651
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 135407090353831936) != 0):
                self.state = 650
                self.expression(0)


            self.state = 653
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
        self._predicates[55] = self.lhs_assignment_statement_sempred
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
         




