# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u0201\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\5\26\u0108\n\26\3\26\3\26\3\27\3\27\3\30\3")
        buf.write("\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"")
        buf.write("\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(")
        buf.write("\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3-\3-\3.\3.\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\7\66\u0158\n\66\f\66\16\66\u015b")
        buf.write("\13\66\3\67\3\67\3\67\3\67\5\67\u0161\n\67\38\38\38\7")
        buf.write("8\u0166\n8\f8\168\u0169\138\58\u016b\n8\39\39\39\39\5")
        buf.write("9\u0171\n9\39\69\u0174\n9\r9\169\u0175\3:\3:\3:\3:\5:")
        buf.write("\u017c\n:\3:\6:\u017f\n:\r:\16:\u0180\3;\3;\3;\3;\5;\u0187")
        buf.write("\n;\3;\6;\u018a\n;\r;\16;\u018b\3<\3<\5<\u0190\n<\3=\6")
        buf.write("=\u0193\n=\r=\16=\u0194\3=\3=\7=\u0199\n=\f=\16=\u019c")
        buf.write("\13=\3>\3>\5>\u01a0\n>\3>\6>\u01a3\n>\r>\16>\u01a4\3?")
        buf.write("\3?\7?\u01a9\n?\f?\16?\u01ac\13?\3?\3?\3@\3@\5@\u01b2")
        buf.write("\n@\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\5A\u01be\nA\3B\6B\u01c1")
        buf.write("\nB\rB\16B\u01c2\3B\3B\3C\3C\3C\3C\7C\u01cb\nC\fC\16C")
        buf.write("\u01ce\13C\3C\3C\3D\3D\3D\3D\3D\3D\7D\u01d8\nD\fD\16D")
        buf.write("\u01db\13D\3D\3D\3D\3D\3D\3E\3E\3E\3F\3F\7F\u01e7\nF\f")
        buf.write("F\16F\u01ea\13F\3F\3F\3F\5F\u01ef\nF\3F\3F\3G\3G\7G\u01f5")
        buf.write("\nG\fG\16G\u01f8\13G\3G\3G\3G\3H\3H\3H\5H\u0200\nH\3\u01d9")
        buf.write("\2I\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o\2")
        buf.write("q\2s\2u\2w9y\2{\2}:\177\2\u0081\2\u0083;\u0085<\u0087")
        buf.write("=\u0089>\u008b?\u008d@\u008f\2\3\2\21\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\3\2\63;\3\2\62;\3\2\62\63\3\2\629\5\2\62;CHc")
        buf.write("h\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^\5\2\13\13\16\17\"")
        buf.write("\"\4\2\f\f\17\17\3\3\f\f\3\2\17\17\7\2$$^^ppttvv\2\u0218")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2w\3\2\2\2\2}")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\3\u0091")
        buf.write("\3\2\2\2\5\u0094\3\2\2\2\7\u0099\3\2\2\2\t\u009d\3\2\2")
        buf.write("\2\13\u00a4\3\2\2\2\r\u00a9\3\2\2\2\17\u00ae\3\2\2\2\21")
        buf.write("\u00b5\3\2\2\2\23\u00bf\3\2\2\2\25\u00c6\3\2\2\2\27\u00ca")
        buf.write("\3\2\2\2\31\u00d0\3\2\2\2\33\u00d8\3\2\2\2\35\u00de\3")
        buf.write("\2\2\2\37\u00e2\3\2\2\2!\u00eb\3\2\2\2#\u00f1\3\2\2\2")
        buf.write("%\u00f7\3\2\2\2\'\u00fb\3\2\2\2)\u0100\3\2\2\2+\u0107")
        buf.write("\3\2\2\2-\u010b\3\2\2\2/\u010d\3\2\2\2\61\u010f\3\2\2")
        buf.write("\2\63\u0111\3\2\2\2\65\u0113\3\2\2\2\67\u0115\3\2\2\2")
        buf.write("9\u0118\3\2\2\2;\u011b\3\2\2\2=\u011d\3\2\2\2?\u0120\3")
        buf.write("\2\2\2A\u0122\3\2\2\2C\u0125\3\2\2\2E\u0128\3\2\2\2G\u012b")
        buf.write("\3\2\2\2I\u012d\3\2\2\2K\u012f\3\2\2\2M\u0132\3\2\2\2")
        buf.write("O\u0135\3\2\2\2Q\u0138\3\2\2\2S\u013b\3\2\2\2U\u013e\3")
        buf.write("\2\2\2W\u0141\3\2\2\2Y\u0143\3\2\2\2[\u0145\3\2\2\2]\u0147")
        buf.write("\3\2\2\2_\u0149\3\2\2\2a\u014b\3\2\2\2c\u014d\3\2\2\2")
        buf.write("e\u014f\3\2\2\2g\u0151\3\2\2\2i\u0153\3\2\2\2k\u0155\3")
        buf.write("\2\2\2m\u0160\3\2\2\2o\u016a\3\2\2\2q\u0170\3\2\2\2s\u017b")
        buf.write("\3\2\2\2u\u0186\3\2\2\2w\u018d\3\2\2\2y\u0192\3\2\2\2")
        buf.write("{\u019d\3\2\2\2}\u01a6\3\2\2\2\177\u01b1\3\2\2\2\u0081")
        buf.write("\u01bd\3\2\2\2\u0083\u01c0\3\2\2\2\u0085\u01c6\3\2\2\2")
        buf.write("\u0087\u01d1\3\2\2\2\u0089\u01e1\3\2\2\2\u008b\u01e4\3")
        buf.write("\2\2\2\u008d\u01f2\3\2\2\2\u008f\u01ff\3\2\2\2\u0091\u0092")
        buf.write("\7k\2\2\u0092\u0093\7h\2\2\u0093\4\3\2\2\2\u0094\u0095")
        buf.write("\7g\2\2\u0095\u0096\7n\2\2\u0096\u0097\7u\2\2\u0097\u0098")
        buf.write("\7g\2\2\u0098\6\3\2\2\2\u0099\u009a\7h\2\2\u009a\u009b")
        buf.write("\7q\2\2\u009b\u009c\7t\2\2\u009c\b\3\2\2\2\u009d\u009e")
        buf.write("\7t\2\2\u009e\u009f\7g\2\2\u009f\u00a0\7v\2\2\u00a0\u00a1")
        buf.write("\7w\2\2\u00a1\u00a2\7t\2\2\u00a2\u00a3\7p\2\2\u00a3\n")
        buf.write("\3\2\2\2\u00a4\u00a5\7h\2\2\u00a5\u00a6\7w\2\2\u00a6\u00a7")
        buf.write("\7p\2\2\u00a7\u00a8\7e\2\2\u00a8\f\3\2\2\2\u00a9\u00aa")
        buf.write("\7v\2\2\u00aa\u00ab\7{\2\2\u00ab\u00ac\7r\2\2\u00ac\u00ad")
        buf.write("\7g\2\2\u00ad\16\3\2\2\2\u00ae\u00af\7u\2\2\u00af\u00b0")
        buf.write("\7v\2\2\u00b0\u00b1\7t\2\2\u00b1\u00b2\7w\2\2\u00b2\u00b3")
        buf.write("\7e\2\2\u00b3\u00b4\7v\2\2\u00b4\20\3\2\2\2\u00b5\u00b6")
        buf.write("\7k\2\2\u00b6\u00b7\7p\2\2\u00b7\u00b8\7v\2\2\u00b8\u00b9")
        buf.write("\7g\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb\7h\2\2\u00bb\u00bc")
        buf.write("\7c\2\2\u00bc\u00bd\7e\2\2\u00bd\u00be\7g\2\2\u00be\22")
        buf.write("\3\2\2\2\u00bf\u00c0\7u\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2")
        buf.write("\7t\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4\7p\2\2\u00c4\u00c5")
        buf.write("\7i\2\2\u00c5\24\3\2\2\2\u00c6\u00c7\7k\2\2\u00c7\u00c8")
        buf.write("\7p\2\2\u00c8\u00c9\7v\2\2\u00c9\26\3\2\2\2\u00ca\u00cb")
        buf.write("\7h\2\2\u00cb\u00cc\7n\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce")
        buf.write("\7c\2\2\u00ce\u00cf\7v\2\2\u00cf\30\3\2\2\2\u00d0\u00d1")
        buf.write("\7d\2\2\u00d1\u00d2\7q\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4")
        buf.write("\7n\2\2\u00d4\u00d5\7g\2\2\u00d5\u00d6\7c\2\2\u00d6\u00d7")
        buf.write("\7p\2\2\u00d7\32\3\2\2\2\u00d8\u00d9\7e\2\2\u00d9\u00da")
        buf.write("\7q\2\2\u00da\u00db\7p\2\2\u00db\u00dc\7u\2\2\u00dc\u00dd")
        buf.write("\7v\2\2\u00dd\34\3\2\2\2\u00de\u00df\7x\2\2\u00df\u00e0")
        buf.write("\7c\2\2\u00e0\u00e1\7t\2\2\u00e1\36\3\2\2\2\u00e2\u00e3")
        buf.write("\7e\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6")
        buf.write("\7v\2\2\u00e6\u00e7\7k\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9")
        buf.write("\7w\2\2\u00e9\u00ea\7g\2\2\u00ea \3\2\2\2\u00eb\u00ec")
        buf.write("\7d\2\2\u00ec\u00ed\7t\2\2\u00ed\u00ee\7g\2\2\u00ee\u00ef")
        buf.write("\7c\2\2\u00ef\u00f0\7m\2\2\u00f0\"\3\2\2\2\u00f1\u00f2")
        buf.write("\7t\2\2\u00f2\u00f3\7c\2\2\u00f3\u00f4\7p\2\2\u00f4\u00f5")
        buf.write("\7i\2\2\u00f5\u00f6\7g\2\2\u00f6$\3\2\2\2\u00f7\u00f8")
        buf.write("\7p\2\2\u00f8\u00f9\7k\2\2\u00f9\u00fa\7n\2\2\u00fa&\3")
        buf.write("\2\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd\7t\2\2\u00fd\u00fe")
        buf.write("\7w\2\2\u00fe\u00ff\7g\2\2\u00ff(\3\2\2\2\u0100\u0101")
        buf.write("\7h\2\2\u0101\u0102\7c\2\2\u0102\u0103\7n\2\2\u0103\u0104")
        buf.write("\7u\2\2\u0104\u0105\7g\2\2\u0105*\3\2\2\2\u0106\u0108")
        buf.write("\7\17\2\2\u0107\u0106\3\2\2\2\u0107\u0108\3\2\2\2\u0108")
        buf.write("\u0109\3\2\2\2\u0109\u010a\7\f\2\2\u010a,\3\2\2\2\u010b")
        buf.write("\u010c\7-\2\2\u010c.\3\2\2\2\u010d\u010e\7/\2\2\u010e")
        buf.write("\60\3\2\2\2\u010f\u0110\7,\2\2\u0110\62\3\2\2\2\u0111")
        buf.write("\u0112\7\61\2\2\u0112\64\3\2\2\2\u0113\u0114\7\'\2\2\u0114")
        buf.write("\66\3\2\2\2\u0115\u0116\7?\2\2\u0116\u0117\7?\2\2\u0117")
        buf.write("8\3\2\2\2\u0118\u0119\7#\2\2\u0119\u011a\7?\2\2\u011a")
        buf.write(":\3\2\2\2\u011b\u011c\7>\2\2\u011c<\3\2\2\2\u011d\u011e")
        buf.write("\7>\2\2\u011e\u011f\7?\2\2\u011f>\3\2\2\2\u0120\u0121")
        buf.write("\7@\2\2\u0121@\3\2\2\2\u0122\u0123\7@\2\2\u0123\u0124")
        buf.write("\7?\2\2\u0124B\3\2\2\2\u0125\u0126\7(\2\2\u0126\u0127")
        buf.write("\7(\2\2\u0127D\3\2\2\2\u0128\u0129\7~\2\2\u0129\u012a")
        buf.write("\7~\2\2\u012aF\3\2\2\2\u012b\u012c\7#\2\2\u012cH\3\2\2")
        buf.write("\2\u012d\u012e\7?\2\2\u012eJ\3\2\2\2\u012f\u0130\7<\2")
        buf.write("\2\u0130\u0131\7?\2\2\u0131L\3\2\2\2\u0132\u0133\7-\2")
        buf.write("\2\u0133\u0134\7?\2\2\u0134N\3\2\2\2\u0135\u0136\7/\2")
        buf.write("\2\u0136\u0137\7?\2\2\u0137P\3\2\2\2\u0138\u0139\7,\2")
        buf.write("\2\u0139\u013a\7?\2\2\u013aR\3\2\2\2\u013b\u013c\7\61")
        buf.write("\2\2\u013c\u013d\7?\2\2\u013dT\3\2\2\2\u013e\u013f\7\'")
        buf.write("\2\2\u013f\u0140\7?\2\2\u0140V\3\2\2\2\u0141\u0142\7\60")
        buf.write("\2\2\u0142X\3\2\2\2\u0143\u0144\7*\2\2\u0144Z\3\2\2\2")
        buf.write("\u0145\u0146\7+\2\2\u0146\\\3\2\2\2\u0147\u0148\7}\2\2")
        buf.write("\u0148^\3\2\2\2\u0149\u014a\7\177\2\2\u014a`\3\2\2\2\u014b")
        buf.write("\u014c\7]\2\2\u014cb\3\2\2\2\u014d\u014e\7_\2\2\u014e")
        buf.write("d\3\2\2\2\u014f\u0150\7.\2\2\u0150f\3\2\2\2\u0151\u0152")
        buf.write("\7=\2\2\u0152h\3\2\2\2\u0153\u0154\7<\2\2\u0154j\3\2\2")
        buf.write("\2\u0155\u0159\t\2\2\2\u0156\u0158\t\3\2\2\u0157\u0156")
        buf.write("\3\2\2\2\u0158\u015b\3\2\2\2\u0159\u0157\3\2\2\2\u0159")
        buf.write("\u015a\3\2\2\2\u015al\3\2\2\2\u015b\u0159\3\2\2\2\u015c")
        buf.write("\u0161\5o8\2\u015d\u0161\5q9\2\u015e\u0161\5s:\2\u015f")
        buf.write("\u0161\5u;\2\u0160\u015c\3\2\2\2\u0160\u015d\3\2\2\2\u0160")
        buf.write("\u015e\3\2\2\2\u0160\u015f\3\2\2\2\u0161n\3\2\2\2\u0162")
        buf.write("\u016b\7\62\2\2\u0163\u0167\t\4\2\2\u0164\u0166\t\5\2")
        buf.write("\2\u0165\u0164\3\2\2\2\u0166\u0169\3\2\2\2\u0167\u0165")
        buf.write("\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u016b\3\2\2\2\u0169")
        buf.write("\u0167\3\2\2\2\u016a\u0162\3\2\2\2\u016a\u0163\3\2\2\2")
        buf.write("\u016bp\3\2\2\2\u016c\u016d\7\62\2\2\u016d\u0171\7d\2")
        buf.write("\2\u016e\u016f\7\62\2\2\u016f\u0171\7D\2\2\u0170\u016c")
        buf.write("\3\2\2\2\u0170\u016e\3\2\2\2\u0171\u0173\3\2\2\2\u0172")
        buf.write("\u0174\t\6\2\2\u0173\u0172\3\2\2\2\u0174\u0175\3\2\2\2")
        buf.write("\u0175\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176r\3\2\2")
        buf.write("\2\u0177\u0178\7\62\2\2\u0178\u017c\7q\2\2\u0179\u017a")
        buf.write("\7\62\2\2\u017a\u017c\7Q\2\2\u017b\u0177\3\2\2\2\u017b")
        buf.write("\u0179\3\2\2\2\u017c\u017e\3\2\2\2\u017d\u017f\t\7\2\2")
        buf.write("\u017e\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u017e\3")
        buf.write("\2\2\2\u0180\u0181\3\2\2\2\u0181t\3\2\2\2\u0182\u0183")
        buf.write("\7\62\2\2\u0183\u0187\7z\2\2\u0184\u0185\7\62\2\2\u0185")
        buf.write("\u0187\7Z\2\2\u0186\u0182\3\2\2\2\u0186\u0184\3\2\2\2")
        buf.write("\u0187\u0189\3\2\2\2\u0188\u018a\t\b\2\2\u0189\u0188\3")
        buf.write("\2\2\2\u018a\u018b\3\2\2\2\u018b\u0189\3\2\2\2\u018b\u018c")
        buf.write("\3\2\2\2\u018cv\3\2\2\2\u018d\u018f\5y=\2\u018e\u0190")
        buf.write("\5{>\2\u018f\u018e\3\2\2\2\u018f\u0190\3\2\2\2\u0190x")
        buf.write("\3\2\2\2\u0191\u0193\t\5\2\2\u0192\u0191\3\2\2\2\u0193")
        buf.write("\u0194\3\2\2\2\u0194\u0192\3\2\2\2\u0194\u0195\3\2\2\2")
        buf.write("\u0195\u0196\3\2\2\2\u0196\u019a\7\60\2\2\u0197\u0199")
        buf.write("\t\5\2\2\u0198\u0197\3\2\2\2\u0199\u019c\3\2\2\2\u019a")
        buf.write("\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019bz\3\2\2\2\u019c")
        buf.write("\u019a\3\2\2\2\u019d\u019f\t\t\2\2\u019e\u01a0\t\n\2\2")
        buf.write("\u019f\u019e\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a2\3")
        buf.write("\2\2\2\u01a1\u01a3\t\5\2\2\u01a2\u01a1\3\2\2\2\u01a3\u01a4")
        buf.write("\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5")
        buf.write("|\3\2\2\2\u01a6\u01aa\7$\2\2\u01a7\u01a9\5\177@\2\u01a8")
        buf.write("\u01a7\3\2\2\2\u01a9\u01ac\3\2\2\2\u01aa\u01a8\3\2\2\2")
        buf.write("\u01aa\u01ab\3\2\2\2\u01ab\u01ad\3\2\2\2\u01ac\u01aa\3")
        buf.write("\2\2\2\u01ad\u01ae\7$\2\2\u01ae~\3\2\2\2\u01af\u01b2\n")
        buf.write("\13\2\2\u01b0\u01b2\5\u0081A\2\u01b1\u01af\3\2\2\2\u01b1")
        buf.write("\u01b0\3\2\2\2\u01b2\u0080\3\2\2\2\u01b3\u01b4\7^\2\2")
        buf.write("\u01b4\u01be\7p\2\2\u01b5\u01b6\7^\2\2\u01b6\u01be\7v")
        buf.write("\2\2\u01b7\u01b8\7^\2\2\u01b8\u01be\7t\2\2\u01b9\u01ba")
        buf.write("\7^\2\2\u01ba\u01be\7$\2\2\u01bb\u01bc\7^\2\2\u01bc\u01be")
        buf.write("\7^\2\2\u01bd\u01b3\3\2\2\2\u01bd\u01b5\3\2\2\2\u01bd")
        buf.write("\u01b7\3\2\2\2\u01bd\u01b9\3\2\2\2\u01bd\u01bb\3\2\2\2")
        buf.write("\u01be\u0082\3\2\2\2\u01bf\u01c1\t\f\2\2\u01c0\u01bf\3")
        buf.write("\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c2\u01c3")
        buf.write("\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c5\bB\2\2\u01c5")
        buf.write("\u0084\3\2\2\2\u01c6\u01c7\7\61\2\2\u01c7\u01c8\7\61\2")
        buf.write("\2\u01c8\u01cc\3\2\2\2\u01c9\u01cb\n\r\2\2\u01ca\u01c9")
        buf.write("\3\2\2\2\u01cb\u01ce\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cc")
        buf.write("\u01cd\3\2\2\2\u01cd\u01cf\3\2\2\2\u01ce\u01cc\3\2\2\2")
        buf.write("\u01cf\u01d0\bC\2\2\u01d0\u0086\3\2\2\2\u01d1\u01d2\7")
        buf.write("\61\2\2\u01d2\u01d3\7,\2\2\u01d3\u01d9\3\2\2\2\u01d4\u01d8")
        buf.write("\5\u0087D\2\u01d5\u01d8\5\u0085C\2\u01d6\u01d8\13\2\2")
        buf.write("\2\u01d7\u01d4\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d7\u01d6")
        buf.write("\3\2\2\2\u01d8\u01db\3\2\2\2\u01d9\u01da\3\2\2\2\u01d9")
        buf.write("\u01d7\3\2\2\2\u01da\u01dc\3\2\2\2\u01db\u01d9\3\2\2\2")
        buf.write("\u01dc\u01dd\7,\2\2\u01dd\u01de\7\61\2\2\u01de\u01df\3")
        buf.write("\2\2\2\u01df\u01e0\bD\2\2\u01e0\u0088\3\2\2\2\u01e1\u01e2")
        buf.write("\13\2\2\2\u01e2\u01e3\bE\3\2\u01e3\u008a\3\2\2\2\u01e4")
        buf.write("\u01e8\7$\2\2\u01e5\u01e7\5\177@\2\u01e6\u01e5\3\2\2\2")
        buf.write("\u01e7\u01ea\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e8\u01e9\3")
        buf.write("\2\2\2\u01e9\u01ee\3\2\2\2\u01ea\u01e8\3\2\2\2\u01eb\u01ec")
        buf.write("\7\17\2\2\u01ec\u01ef\7\f\2\2\u01ed\u01ef\t\16\2\2\u01ee")
        buf.write("\u01eb\3\2\2\2\u01ee\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2")
        buf.write("\u01f0\u01f1\bF\4\2\u01f1\u008c\3\2\2\2\u01f2\u01f6\7")
        buf.write("$\2\2\u01f3\u01f5\5\177@\2\u01f4\u01f3\3\2\2\2\u01f5\u01f8")
        buf.write("\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7")
        buf.write("\u01f9\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f9\u01fa\5\u008f")
        buf.write("H\2\u01fa\u01fb\bG\5\2\u01fb\u008e\3\2\2\2\u01fc\u0200")
        buf.write("\t\17\2\2\u01fd\u01fe\7^\2\2\u01fe\u0200\n\20\2\2\u01ff")
        buf.write("\u01fc\3\2\2\2\u01ff\u01fd\3\2\2\2\u0200\u0090\3\2\2\2")
        buf.write("\36\2\u0107\u0159\u0160\u0167\u016a\u0170\u0175\u017b")
        buf.write("\u0180\u0186\u018b\u018f\u0194\u019a\u019f\u01a4\u01aa")
        buf.write("\u01b1\u01bd\u01c2\u01cc\u01d7\u01d9\u01e8\u01ee\u01f6")
        buf.write("\u01ff\6\b\2\2\3E\2\3F\3\3G\4")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    ELSE = 2
    FOR = 3
    RETURN = 4
    FUNC = 5
    TYPE = 6
    STRUCT = 7
    INTERFACE = 8
    STRING = 9
    INT = 10
    FLOAT = 11
    BOOLEAN = 12
    CONST = 13
    VAR = 14
    CONTINUE = 15
    BREAK = 16
    RANGE = 17
    NIL = 18
    TRUE = 19
    FALSE = 20
    NEWLINE = 21
    ADD = 22
    SUB = 23
    MUL = 24
    DIV = 25
    MOD = 26
    EQUAL = 27
    NOT_EQUAL = 28
    LESS = 29
    LESS_EQUAL = 30
    GREATER = 31
    GREATER_EQUAL = 32
    AND = 33
    OR = 34
    NOT = 35
    ASSIGN = 36
    ASSIGN_STATE = 37
    ADD_ASSIGN = 38
    SUB_ASSIGN = 39
    MUL_ASSIGN = 40
    DIV_ASSIGN = 41
    MOD_ASSIGN = 42
    DOT = 43
    LPAREN = 44
    RPAREN = 45
    LBRACE = 46
    RBRACE = 47
    LBRACK = 48
    RBRACK = 49
    COMMA = 50
    SEMICOLON = 51
    COLON = 52
    ID = 53
    INTEGER_LIT = 54
    FLOAT_LIT = 55
    STRING_LIT = 56
    WS = 57
    COMMENT_INLINE = 58
    COMMENT_BLOCK = 59
    ERROR_CHAR = 60
    UNCLOSE_STRING = 61
    ILLEGAL_ESCAPE = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", 
            "'='", "':='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "NEWLINE", "ADD", 
            "SUB", "MUL", "DIV", "MOD", "EQUAL", "NOT_EQUAL", "LESS", "LESS_EQUAL", 
            "GREATER", "GREATER_EQUAL", "AND", "OR", "NOT", "ASSIGN", "ASSIGN_STATE", 
            "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
            "DOT", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
            "COMMA", "SEMICOLON", "COLON", "ID", "INTEGER_LIT", "FLOAT_LIT", 
            "STRING_LIT", "WS", "COMMENT_INLINE", "COMMENT_BLOCK", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", 
                  "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", 
                  "NEWLINE", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", 
                  "NOT_EQUAL", "LESS", "LESS_EQUAL", "GREATER", "GREATER_EQUAL", 
                  "AND", "OR", "NOT", "ASSIGN", "ASSIGN_STATE", "ADD_ASSIGN", 
                  "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                  "DOT", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", 
                  "RBRACK", "COMMA", "SEMICOLON", "COLON", "ID", "INTEGER_LIT", 
                  "DEC", "BIN", "OCT", "HEX", "FLOAT_LIT", "REAL_NUM", "EXPONENT_PART", 
                  "STRING_LIT", "CHARACTER", "ESCAPED_SEQ", "WS", "COMMENT_INLINE", 
                  "COMMENT_BLOCK", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ESC_ILLEGAL" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    prev_token = None

    def emit(self):
        tk = self.type

        if tk == self.UNCLOSE_STRING:       
            result = super().emit()
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit()
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            result = super().emit()
            raise ErrorToken(result.text)
        elif tk == self.NEWLINE:
            if self.prev_token and self.prev_token.type in [
                MiniGoLexer.ID, MiniGoLexer.INTEGER_LIT, MiniGoLexer.FLOAT_LIT,
                MiniGoLexer.TRUE, MiniGoLexer.FALSE, MiniGoLexer.STRING_LIT, MiniGoLexer.NIL,
                MiniGoLexer.INT, MiniGoLexer.FLOAT, MiniGoLexer.STRING, MiniGoLexer.BOOLEAN,
                MiniGoLexer.RETURN, MiniGoLexer.CONTINUE, MiniGoLexer.BREAK,
                MiniGoLexer.RPAREN, MiniGoLexer.RBRACK, MiniGoLexer.RBRACE
            ]:
                self.type = MiniGoLexer.SEMICOLON
                self.text = ";"
            else:
                return self.nextToken()

        result = super().emit()
        self.prev_token = result
        return result


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[67] = self.ERROR_CHAR_action 
            actions[68] = self.UNCLOSE_STRING_action 
            actions[69] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             
                if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
                    raise UncloseString(self.text[:-2])
                elif (self.text[-1] == '\n'):
                    raise UncloseString(self.text[:-1])
                else:
                    raise UncloseString(self.text)

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                raise IllegalEscape(self.text)

     


