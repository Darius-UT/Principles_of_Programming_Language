# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u0292\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0094\n")
        buf.write("\3\3\4\3\4\3\4\5\4\u0099\n\4\3\5\3\5\3\6\3\6\3\6\5\6\u00a0")
        buf.write("\n\6\3\7\3\7\3\b\3\b\3\b\5\b\u00a7\n\b\3\t\3\t\3\t\3\t")
        buf.write("\5\t\u00ad\n\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\5\f\u00bd\n\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\5\r\u00c6\n\r\3\16\3\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\5\17\u00cf\n\17\3\20\3\20\3\20\3\20\3\20\5\20\u00d6")
        buf.write("\n\20\3\21\3\21\3\21\3\21\3\22\3\22\5\22\u00de\n\22\3")
        buf.write("\23\3\23\3\23\3\23\3\23\5\23\u00e5\n\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\7\24\u00ed\n\24\f\24\16\24\u00f0\13\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u00f8\n\25\f\25\16")
        buf.write("\25\u00fb\13\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\7\26\u0112\n\26\f\26\16\26\u0115\13\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u0120\n")
        buf.write("\27\f\27\16\27\u0123\13\27\3\30\3\30\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u0131\n\30\f\30")
        buf.write("\16\30\u0134\13\30\3\31\3\31\3\31\3\31\3\31\5\31\u013b")
        buf.write("\n\31\3\32\3\32\3\32\3\32\3\32\5\32\u0142\n\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\7\32")
        buf.write("\u014f\n\32\f\32\16\32\u0152\13\32\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\5\36\u0164\n\36\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\7\36\u0171\n\36\f\36\16\36\u0174")
        buf.write("\13\36\3\37\3\37\5\37\u0178\n\37\3 \3 \3 \3 \5 \u017e")
        buf.write("\n \3!\3!\3!\3!\3!\3!\3!\3!\5!\u0188\n!\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\5\"\u0190\n\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\5")
        buf.write("#\u019b\n#\3#\3#\3$\3$\3$\5$\u01a2\n$\3$\3$\3$\3%\3%\3")
        buf.write("%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\5&\u01b4\n&\3&\3&\3&\3")
        buf.write("\'\3\'\5\'\u01bb\n\'\3(\3(\3(\3(\3(\5(\u01c2\n(\3)\3)")
        buf.write("\3)\7)\u01c7\n)\f)\16)\u01ca\13)\3)\3)\3*\3*\3*\3*\3+")
        buf.write("\3+\3+\3+\3+\3+\3+\3+\5+\u01da\n+\3+\3+\3+\3,\3,\3,\3")
        buf.write(",\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\5.\u01f1\n")
        buf.write(".\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\61\5\61\u0204\n\61\3\62\3\62\3")
        buf.write("\62\5\62\u0209\n\62\3\62\3\62\3\63\3\63\3\63\3\63\3\64")
        buf.write("\3\64\5\64\u0213\n\64\3\65\3\65\3\65\3\65\3\65\5\65\u021a")
        buf.write("\n\65\3\66\3\66\3\66\7\66\u021f\n\66\f\66\16\66\u0222")
        buf.write("\13\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\38\38\39\39")
        buf.write("\39\39\39\39\39\39\39\39\39\79\u0238\n9\f9\169\u023b\13")
        buf.write("9\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3;\5;\u0248\n;\3;\5;\u024b")
        buf.write("\n;\3;\3;\3<\3<\3<\3<\5<\u0253\n<\3=\3=\3=\3=\3=\3=\3")
        buf.write("=\3=\3>\3>\3>\3?\3?\3?\5?\u0263\n?\3?\3?\3@\3@\3@\3@\3")
        buf.write("A\3A\3A\5A\u026e\nA\3A\3A\3A\3A\3A\3A\3B\3B\3B\3B\3B\3")
        buf.write("B\3B\3B\3B\3B\3C\3C\3C\3D\3D\3D\3E\3E\5E\u0288\nE\3E\3")
        buf.write("E\3F\3F\5F\u028e\nF\3F\3F\3F\2\n&(*,.\62:pG\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086")
        buf.write("\u0088\u008a\2\6\4\2\24\268:\3\2\13\16\3\2\678\3\2\',")
        buf.write("\2\u029a\2\u008c\3\2\2\2\4\u0093\3\2\2\2\6\u0098\3\2\2")
        buf.write("\2\b\u009a\3\2\2\2\n\u009f\3\2\2\2\f\u00a1\3\2\2\2\16")
        buf.write("\u00a3\3\2\2\2\20\u00ac\3\2\2\2\22\u00ae\3\2\2\2\24\u00b2")
        buf.write("\3\2\2\2\26\u00bc\3\2\2\2\30\u00c5\3\2\2\2\32\u00c7\3")
        buf.write("\2\2\2\34\u00ce\3\2\2\2\36\u00d5\3\2\2\2 \u00d7\3\2\2")
        buf.write("\2\"\u00dd\3\2\2\2$\u00e4\3\2\2\2&\u00e6\3\2\2\2(\u00f1")
        buf.write("\3\2\2\2*\u00fc\3\2\2\2,\u0116\3\2\2\2.\u0124\3\2\2\2")
        buf.write("\60\u013a\3\2\2\2\62\u0141\3\2\2\2\64\u0153\3\2\2\2\66")
        buf.write("\u0157\3\2\2\28\u015c\3\2\2\2:\u0163\3\2\2\2<\u0177\3")
        buf.write("\2\2\2>\u017d\3\2\2\2@\u0187\3\2\2\2B\u018f\3\2\2\2D\u0191")
        buf.write("\3\2\2\2F\u019e\3\2\2\2H\u01a6\3\2\2\2J\u01ac\3\2\2\2")
        buf.write("L\u01ba\3\2\2\2N\u01c1\3\2\2\2P\u01c3\3\2\2\2R\u01cd\3")
        buf.write("\2\2\2T\u01d1\3\2\2\2V\u01de\3\2\2\2X\u01e3\3\2\2\2Z\u01f0")
        buf.write("\3\2\2\2\\\u01f2\3\2\2\2^\u01f6\3\2\2\2`\u0203\3\2\2\2")
        buf.write("b\u0205\3\2\2\2d\u020c\3\2\2\2f\u0212\3\2\2\2h\u0219\3")
        buf.write("\2\2\2j\u021b\3\2\2\2l\u0225\3\2\2\2n\u022a\3\2\2\2p\u022c")
        buf.write("\3\2\2\2r\u023c\3\2\2\2t\u0240\3\2\2\2v\u0252\3\2\2\2")
        buf.write("x\u0254\3\2\2\2z\u025c\3\2\2\2|\u0262\3\2\2\2~\u0266\3")
        buf.write("\2\2\2\u0080\u026a\3\2\2\2\u0082\u0275\3\2\2\2\u0084\u027f")
        buf.write("\3\2\2\2\u0086\u0282\3\2\2\2\u0088\u0287\3\2\2\2\u008a")
        buf.write("\u028b\3\2\2\2\u008c\u008d\5\4\3\2\u008d\u008e\7\2\2\3")
        buf.write("\u008e\3\3\2\2\2\u008f\u0090\5B\"\2\u0090\u0091\5\4\3")
        buf.write("\2\u0091\u0094\3\2\2\2\u0092\u0094\5B\"\2\u0093\u008f")
        buf.write("\3\2\2\2\u0093\u0092\3\2\2\2\u0094\5\3\2\2\2\u0095\u0099")
        buf.write("\5\b\5\2\u0096\u0099\5\24\13\2\u0097\u0099\5\32\16\2\u0098")
        buf.write("\u0095\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0097\3\2\2\2")
        buf.write("\u0099\7\3\2\2\2\u009a\u009b\t\2\2\2\u009b\t\3\2\2\2\u009c")
        buf.write("\u00a0\7\67\2\2\u009d\u00a0\5\f\7\2\u009e\u00a0\5\16\b")
        buf.write("\2\u009f\u009c\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u009e")
        buf.write("\3\2\2\2\u00a0\13\3\2\2\2\u00a1\u00a2\t\3\2\2\u00a2\r")
        buf.write("\3\2\2\2\u00a3\u00a6\5\20\t\2\u00a4\u00a7\7\67\2\2\u00a5")
        buf.write("\u00a7\5\f\7\2\u00a6\u00a4\3\2\2\2\u00a6\u00a5\3\2\2\2")
        buf.write("\u00a7\17\3\2\2\2\u00a8\u00a9\5\22\n\2\u00a9\u00aa\5\20")
        buf.write("\t\2\u00aa\u00ad\3\2\2\2\u00ab\u00ad\5\22\n\2\u00ac\u00a8")
        buf.write("\3\2\2\2\u00ac\u00ab\3\2\2\2\u00ad\21\3\2\2\2\u00ae\u00af")
        buf.write("\7\62\2\2\u00af\u00b0\t\4\2\2\u00b0\u00b1\7\63\2\2\u00b1")
        buf.write("\23\3\2\2\2\u00b2\u00b3\5\16\b\2\u00b3\u00b4\7\60\2\2")
        buf.write("\u00b4\u00b5\5\26\f\2\u00b5\u00b6\7\61\2\2\u00b6\25\3")
        buf.write("\2\2\2\u00b7\u00b8\5\30\r\2\u00b8\u00b9\7\64\2\2\u00b9")
        buf.write("\u00ba\5\26\f\2\u00ba\u00bd\3\2\2\2\u00bb\u00bd\5\30\r")
        buf.write("\2\u00bc\u00b7\3\2\2\2\u00bc\u00bb\3\2\2\2\u00bd\27\3")
        buf.write("\2\2\2\u00be\u00c6\7\67\2\2\u00bf\u00c6\5\b\5\2\u00c0")
        buf.write("\u00c6\5\32\16\2\u00c1\u00c2\7\60\2\2\u00c2\u00c3\5\26")
        buf.write("\f\2\u00c3\u00c4\7\61\2\2\u00c4\u00c6\3\2\2\2\u00c5\u00be")
        buf.write("\3\2\2\2\u00c5\u00bf\3\2\2\2\u00c5\u00c0\3\2\2\2\u00c5")
        buf.write("\u00c1\3\2\2\2\u00c6\31\3\2\2\2\u00c7\u00c8\7\67\2\2\u00c8")
        buf.write("\u00c9\7\60\2\2\u00c9\u00ca\5\34\17\2\u00ca\u00cb\7\61")
        buf.write("\2\2\u00cb\33\3\2\2\2\u00cc\u00cf\5\36\20\2\u00cd\u00cf")
        buf.write("\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cd\3\2\2\2\u00cf")
        buf.write("\35\3\2\2\2\u00d0\u00d1\5 \21\2\u00d1\u00d2\7\64\2\2\u00d2")
        buf.write("\u00d3\5\36\20\2\u00d3\u00d6\3\2\2\2\u00d4\u00d6\5 \21")
        buf.write("\2\u00d5\u00d0\3\2\2\2\u00d5\u00d4\3\2\2\2\u00d6\37\3")
        buf.write("\2\2\2\u00d7\u00d8\7\67\2\2\u00d8\u00d9\7\66\2\2\u00d9")
        buf.write("\u00da\5&\24\2\u00da!\3\2\2\2\u00db\u00de\5$\23\2\u00dc")
        buf.write("\u00de\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd\u00dc\3\2\2\2")
        buf.write("\u00de#\3\2\2\2\u00df\u00e0\5&\24\2\u00e0\u00e1\7\64\2")
        buf.write("\2\u00e1\u00e2\5$\23\2\u00e2\u00e5\3\2\2\2\u00e3\u00e5")
        buf.write("\5&\24\2\u00e4\u00df\3\2\2\2\u00e4\u00e3\3\2\2\2\u00e5")
        buf.write("%\3\2\2\2\u00e6\u00e7\b\24\1\2\u00e7\u00e8\5(\25\2\u00e8")
        buf.write("\u00ee\3\2\2\2\u00e9\u00ea\f\4\2\2\u00ea\u00eb\7$\2\2")
        buf.write("\u00eb\u00ed\5(\25\2\u00ec\u00e9\3\2\2\2\u00ed\u00f0\3")
        buf.write("\2\2\2\u00ee\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\'")
        buf.write("\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f1\u00f2\b\25\1\2\u00f2")
        buf.write("\u00f3\5*\26\2\u00f3\u00f9\3\2\2\2\u00f4\u00f5\f\4\2\2")
        buf.write("\u00f5\u00f6\7#\2\2\u00f6\u00f8\5*\26\2\u00f7\u00f4\3")
        buf.write("\2\2\2\u00f8\u00fb\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9\u00fa")
        buf.write("\3\2\2\2\u00fa)\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fc\u00fd")
        buf.write("\b\26\1\2\u00fd\u00fe\5,\27\2\u00fe\u0113\3\2\2\2\u00ff")
        buf.write("\u0100\f\t\2\2\u0100\u0101\7\35\2\2\u0101\u0112\5,\27")
        buf.write("\2\u0102\u0103\f\b\2\2\u0103\u0104\7\36\2\2\u0104\u0112")
        buf.write("\5,\27\2\u0105\u0106\f\7\2\2\u0106\u0107\7\37\2\2\u0107")
        buf.write("\u0112\5,\27\2\u0108\u0109\f\6\2\2\u0109\u010a\7 \2\2")
        buf.write("\u010a\u0112\5,\27\2\u010b\u010c\f\5\2\2\u010c\u010d\7")
        buf.write("!\2\2\u010d\u0112\5,\27\2\u010e\u010f\f\4\2\2\u010f\u0110")
        buf.write("\7\"\2\2\u0110\u0112\5,\27\2\u0111\u00ff\3\2\2\2\u0111")
        buf.write("\u0102\3\2\2\2\u0111\u0105\3\2\2\2\u0111\u0108\3\2\2\2")
        buf.write("\u0111\u010b\3\2\2\2\u0111\u010e\3\2\2\2\u0112\u0115\3")
        buf.write("\2\2\2\u0113\u0111\3\2\2\2\u0113\u0114\3\2\2\2\u0114+")
        buf.write("\3\2\2\2\u0115\u0113\3\2\2\2\u0116\u0117\b\27\1\2\u0117")
        buf.write("\u0118\5.\30\2\u0118\u0121\3\2\2\2\u0119\u011a\f\5\2\2")
        buf.write("\u011a\u011b\7\30\2\2\u011b\u0120\5.\30\2\u011c\u011d")
        buf.write("\f\4\2\2\u011d\u011e\7\31\2\2\u011e\u0120\5.\30\2\u011f")
        buf.write("\u0119\3\2\2\2\u011f\u011c\3\2\2\2\u0120\u0123\3\2\2\2")
        buf.write("\u0121\u011f\3\2\2\2\u0121\u0122\3\2\2\2\u0122-\3\2\2")
        buf.write("\2\u0123\u0121\3\2\2\2\u0124\u0125\b\30\1\2\u0125\u0126")
        buf.write("\5\60\31\2\u0126\u0132\3\2\2\2\u0127\u0128\f\6\2\2\u0128")
        buf.write("\u0129\7\32\2\2\u0129\u0131\5\60\31\2\u012a\u012b\f\5")
        buf.write("\2\2\u012b\u012c\7\33\2\2\u012c\u0131\5\60\31\2\u012d")
        buf.write("\u012e\f\4\2\2\u012e\u012f\7\34\2\2\u012f\u0131\5\60\31")
        buf.write("\2\u0130\u0127\3\2\2\2\u0130\u012a\3\2\2\2\u0130\u012d")
        buf.write("\3\2\2\2\u0131\u0134\3\2\2\2\u0132\u0130\3\2\2\2\u0132")
        buf.write("\u0133\3\2\2\2\u0133/\3\2\2\2\u0134\u0132\3\2\2\2\u0135")
        buf.write("\u0136\7%\2\2\u0136\u013b\5\60\31\2\u0137\u0138\7\31\2")
        buf.write("\2\u0138\u013b\5\60\31\2\u0139\u013b\5\62\32\2\u013a\u0135")
        buf.write("\3\2\2\2\u013a\u0137\3\2\2\2\u013a\u0139\3\2\2\2\u013b")
        buf.write("\61\3\2\2\2\u013c\u013d\b\32\1\2\u013d\u0142\5\66\34\2")
        buf.write("\u013e\u0142\7\67\2\2\u013f\u0142\5\6\4\2\u0140\u0142")
        buf.write("\5\64\33\2\u0141\u013c\3\2\2\2\u0141\u013e\3\2\2\2\u0141")
        buf.write("\u013f\3\2\2\2\u0141\u0140\3\2\2\2\u0142\u0150\3\2\2\2")
        buf.write("\u0143\u0144\f\t\2\2\u0144\u0145\7\62\2\2\u0145\u0146")
        buf.write("\5&\24\2\u0146\u0147\7\63\2\2\u0147\u014f\3\2\2\2\u0148")
        buf.write("\u0149\f\b\2\2\u0149\u014a\7-\2\2\u014a\u014f\7\67\2\2")
        buf.write("\u014b\u014c\f\7\2\2\u014c\u014d\7-\2\2\u014d\u014f\5")
        buf.write("\66\34\2\u014e\u0143\3\2\2\2\u014e\u0148\3\2\2\2\u014e")
        buf.write("\u014b\3\2\2\2\u014f\u0152\3\2\2\2\u0150\u014e\3\2\2\2")
        buf.write("\u0150\u0151\3\2\2\2\u0151\63\3\2\2\2\u0152\u0150\3\2")
        buf.write("\2\2\u0153\u0154\7.\2\2\u0154\u0155\5&\24\2\u0155\u0156")
        buf.write("\7/\2\2\u0156\65\3\2\2\2\u0157\u0158\7\67\2\2\u0158\u0159")
        buf.write("\7.\2\2\u0159\u015a\5\"\22\2\u015a\u015b\7/\2\2\u015b")
        buf.write("\67\3\2\2\2\u015c\u015d\5:\36\2\u015d\u015e\7-\2\2\u015e")
        buf.write("\u015f\5\66\34\2\u015f9\3\2\2\2\u0160\u0161\b\36\1\2\u0161")
        buf.write("\u0164\5\66\34\2\u0162\u0164\7\67\2\2\u0163\u0160\3\2")
        buf.write("\2\2\u0163\u0162\3\2\2\2\u0164\u0172\3\2\2\2\u0165\u0166")
        buf.write("\f\7\2\2\u0166\u0167\7\62\2\2\u0167\u0168\5&\24\2\u0168")
        buf.write("\u0169\7\63\2\2\u0169\u0171\3\2\2\2\u016a\u016b\f\6\2")
        buf.write("\2\u016b\u016c\7-\2\2\u016c\u0171\7\67\2\2\u016d\u016e")
        buf.write("\f\5\2\2\u016e\u016f\7-\2\2\u016f\u0171\5\66\34\2\u0170")
        buf.write("\u0165\3\2\2\2\u0170\u016a\3\2\2\2\u0170\u016d\3\2\2\2")
        buf.write("\u0171\u0174\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0173\3")
        buf.write("\2\2\2\u0173;\3\2\2\2\u0174\u0172\3\2\2\2\u0175\u0178")
        buf.write("\5> \2\u0176\u0178\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0176")
        buf.write("\3\2\2\2\u0178=\3\2\2\2\u0179\u017a\5@!\2\u017a\u017b")
        buf.write("\5> \2\u017b\u017e\3\2\2\2\u017c\u017e\5@!\2\u017d\u0179")
        buf.write("\3\2\2\2\u017d\u017c\3\2\2\2\u017e?\3\2\2\2\u017f\u0188")
        buf.write("\5B\"\2\u0180\u0188\5l\67\2\u0181\u0188\5t;\2\u0182\u0188")
        buf.write("\5|?\2\u0183\u0188\5\u0084C\2\u0184\u0188\5\u0086D\2\u0185")
        buf.write("\u0188\5\u0088E\2\u0186\u0188\5\u008aF\2\u0187\u017f\3")
        buf.write("\2\2\2\u0187\u0180\3\2\2\2\u0187\u0181\3\2\2\2\u0187\u0182")
        buf.write("\3\2\2\2\u0187\u0183\3\2\2\2\u0187\u0184\3\2\2\2\u0187")
        buf.write("\u0185\3\2\2\2\u0187\u0186\3\2\2\2\u0188A\3\2\2\2\u0189")
        buf.write("\u0190\5D#\2\u018a\u0190\5H%\2\u018b\u0190\5J&\2\u018c")
        buf.write("\u0190\5T+\2\u018d\u0190\5X-\2\u018e\u0190\5^\60\2\u018f")
        buf.write("\u0189\3\2\2\2\u018f\u018a\3\2\2\2\u018f\u018b\3\2\2\2")
        buf.write("\u018f\u018c\3\2\2\2\u018f\u018d\3\2\2\2\u018f\u018e\3")
        buf.write("\2\2\2\u0190C\3\2\2\2\u0191\u0192\7\20\2\2\u0192\u019a")
        buf.write("\7\67\2\2\u0193\u0194\5\n\6\2\u0194\u0195\7&\2\2\u0195")
        buf.write("\u0196\5&\24\2\u0196\u019b\3\2\2\2\u0197\u019b\5\n\6\2")
        buf.write("\u0198\u0199\7&\2\2\u0199\u019b\5&\24\2\u019a\u0193\3")
        buf.write("\2\2\2\u019a\u0197\3\2\2\2\u019a\u0198\3\2\2\2\u019b\u019c")
        buf.write("\3\2\2\2\u019c\u019d\7\65\2\2\u019dE\3\2\2\2\u019e\u019f")
        buf.write("\7\20\2\2\u019f\u01a1\7\67\2\2\u01a0\u01a2\5\n\6\2\u01a1")
        buf.write("\u01a0\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a3\3\2\2\2")
        buf.write("\u01a3\u01a4\7&\2\2\u01a4\u01a5\5&\24\2\u01a5G\3\2\2\2")
        buf.write("\u01a6\u01a7\7\17\2\2\u01a7\u01a8\7\67\2\2\u01a8\u01a9")
        buf.write("\7&\2\2\u01a9\u01aa\5&\24\2\u01aa\u01ab\7\65\2\2\u01ab")
        buf.write("I\3\2\2\2\u01ac\u01ad\7\7\2\2\u01ad\u01ae\7\67\2\2\u01ae")
        buf.write("\u01af\7.\2\2\u01af\u01b0\5L\'\2\u01b0\u01b1\7/\2\2\u01b1")
        buf.write("\u01b3\3\2\2\2\u01b2\u01b4\5\n\6\2\u01b3\u01b2\3\2\2\2")
        buf.write("\u01b3\u01b4\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b6\5")
        buf.write("R*\2\u01b6\u01b7\7\65\2\2\u01b7K\3\2\2\2\u01b8\u01bb\5")
        buf.write("N(\2\u01b9\u01bb\3\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01b9")
        buf.write("\3\2\2\2\u01bbM\3\2\2\2\u01bc\u01bd\5P)\2\u01bd\u01be")
        buf.write("\7\64\2\2\u01be\u01bf\5N(\2\u01bf\u01c2\3\2\2\2\u01c0")
        buf.write("\u01c2\5P)\2\u01c1\u01bc\3\2\2\2\u01c1\u01c0\3\2\2\2\u01c2")
        buf.write("O\3\2\2\2\u01c3\u01c8\7\67\2\2\u01c4\u01c5\7\64\2\2\u01c5")
        buf.write("\u01c7\7\67\2\2\u01c6\u01c4\3\2\2\2\u01c7\u01ca\3\2\2")
        buf.write("\2\u01c8\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01cb")
        buf.write("\3\2\2\2\u01ca\u01c8\3\2\2\2\u01cb\u01cc\5\n\6\2\u01cc")
        buf.write("Q\3\2\2\2\u01cd\u01ce\7\60\2\2\u01ce\u01cf\5> \2\u01cf")
        buf.write("\u01d0\7\61\2\2\u01d0S\3\2\2\2\u01d1\u01d2\7\7\2\2\u01d2")
        buf.write("\u01d3\5V,\2\u01d3\u01d4\7\67\2\2\u01d4\u01d5\7.\2\2\u01d5")
        buf.write("\u01d6\5L\'\2\u01d6\u01d7\7/\2\2\u01d7\u01d9\3\2\2\2\u01d8")
        buf.write("\u01da\5\n\6\2\u01d9\u01d8\3\2\2\2\u01d9\u01da\3\2\2\2")
        buf.write("\u01da\u01db\3\2\2\2\u01db\u01dc\5R*\2\u01dc\u01dd\7\65")
        buf.write("\2\2\u01ddU\3\2\2\2\u01de\u01df\7.\2\2\u01df\u01e0\7\67")
        buf.write("\2\2\u01e0\u01e1\7\67\2\2\u01e1\u01e2\7/\2\2\u01e2W\3")
        buf.write("\2\2\2\u01e3\u01e4\7\b\2\2\u01e4\u01e5\7\67\2\2\u01e5")
        buf.write("\u01e6\7\t\2\2\u01e6\u01e7\7\60\2\2\u01e7\u01e8\5Z.\2")
        buf.write("\u01e8\u01e9\7\61\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01eb")
        buf.write("\7\65\2\2\u01ebY\3\2\2\2\u01ec\u01ed\5\\/\2\u01ed\u01ee")
        buf.write("\5Z.\2\u01ee\u01f1\3\2\2\2\u01ef\u01f1\5\\/\2\u01f0\u01ec")
        buf.write("\3\2\2\2\u01f0\u01ef\3\2\2\2\u01f1[\3\2\2\2\u01f2\u01f3")
        buf.write("\7\67\2\2\u01f3\u01f4\5\n\6\2\u01f4\u01f5\7\65\2\2\u01f5")
        buf.write("]\3\2\2\2\u01f6\u01f7\7\b\2\2\u01f7\u01f8\7\67\2\2\u01f8")
        buf.write("\u01f9\7\n\2\2\u01f9\u01fa\7\60\2\2\u01fa\u01fb\5`\61")
        buf.write("\2\u01fb\u01fc\7\61\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01fe")
        buf.write("\7\65\2\2\u01fe_\3\2\2\2\u01ff\u0200\5b\62\2\u0200\u0201")
        buf.write("\5`\61\2\u0201\u0204\3\2\2\2\u0202\u0204\5b\62\2\u0203")
        buf.write("\u01ff\3\2\2\2\u0203\u0202\3\2\2\2\u0204a\3\2\2\2\u0205")
        buf.write("\u0206\7\67\2\2\u0206\u0208\5d\63\2\u0207\u0209\5\n\6")
        buf.write("\2\u0208\u0207\3\2\2\2\u0208\u0209\3\2\2\2\u0209\u020a")
        buf.write("\3\2\2\2\u020a\u020b\7\65\2\2\u020bc\3\2\2\2\u020c\u020d")
        buf.write("\7.\2\2\u020d\u020e\5f\64\2\u020e\u020f\7/\2\2\u020fe")
        buf.write("\3\2\2\2\u0210\u0213\5h\65\2\u0211\u0213\3\2\2\2\u0212")
        buf.write("\u0210\3\2\2\2\u0212\u0211\3\2\2\2\u0213g\3\2\2\2\u0214")
        buf.write("\u0215\5j\66\2\u0215\u0216\7\64\2\2\u0216\u0217\5h\65")
        buf.write("\2\u0217\u021a\3\2\2\2\u0218\u021a\5j\66\2\u0219\u0214")
        buf.write("\3\2\2\2\u0219\u0218\3\2\2\2\u021ai\3\2\2\2\u021b\u0220")
        buf.write("\7\67\2\2\u021c\u021d\7\64\2\2\u021d\u021f\7\67\2\2\u021e")
        buf.write("\u021c\3\2\2\2\u021f\u0222\3\2\2\2\u0220\u021e\3\2\2\2")
        buf.write("\u0220\u0221\3\2\2\2\u0221\u0223\3\2\2\2\u0222\u0220\3")
        buf.write("\2\2\2\u0223\u0224\5\n\6\2\u0224k\3\2\2\2\u0225\u0226")
        buf.write("\5p9\2\u0226\u0227\5n8\2\u0227\u0228\5&\24\2\u0228\u0229")
        buf.write("\7\65\2\2\u0229m\3\2\2\2\u022a\u022b\t\5\2\2\u022bo\3")
        buf.write("\2\2\2\u022c\u022d\b9\1\2\u022d\u022e\7\67\2\2\u022e\u0239")
        buf.write("\3\2\2\2\u022f\u0230\f\4\2\2\u0230\u0231\7\62\2\2\u0231")
        buf.write("\u0232\5&\24\2\u0232\u0233\7\63\2\2\u0233\u0238\3\2\2")
        buf.write("\2\u0234\u0235\f\3\2\2\u0235\u0236\7-\2\2\u0236\u0238")
        buf.write("\7\67\2\2\u0237\u022f\3\2\2\2\u0237\u0234\3\2\2\2\u0238")
        buf.write("\u023b\3\2\2\2\u0239\u0237\3\2\2\2\u0239\u023a\3\2\2\2")
        buf.write("\u023aq\3\2\2\2\u023b\u0239\3\2\2\2\u023c\u023d\7\67\2")
        buf.write("\2\u023d\u023e\5n8\2\u023e\u023f\5&\24\2\u023fs\3\2\2")
        buf.write("\2\u0240\u0241\7\3\2\2\u0241\u0242\7.\2\2\u0242\u0243")
        buf.write("\5&\24\2\u0243\u0244\7/\2\2\u0244\u0245\3\2\2\2\u0245")
        buf.write("\u0247\5R*\2\u0246\u0248\5v<\2\u0247\u0246\3\2\2\2\u0247")
        buf.write("\u0248\3\2\2\2\u0248\u024a\3\2\2\2\u0249\u024b\5z>\2\u024a")
        buf.write("\u0249\3\2\2\2\u024a\u024b\3\2\2\2\u024b\u024c\3\2\2\2")
        buf.write("\u024c\u024d\7\65\2\2\u024du\3\2\2\2\u024e\u024f\5x=\2")
        buf.write("\u024f\u0250\5v<\2\u0250\u0253\3\2\2\2\u0251\u0253\5x")
        buf.write("=\2\u0252\u024e\3\2\2\2\u0252\u0251\3\2\2\2\u0253w\3\2")
        buf.write("\2\2\u0254\u0255\7\4\2\2\u0255\u0256\7\3\2\2\u0256\u0257")
        buf.write("\7.\2\2\u0257\u0258\5&\24\2\u0258\u0259\7/\2\2\u0259\u025a")
        buf.write("\3\2\2\2\u025a\u025b\5R*\2\u025by\3\2\2\2\u025c\u025d")
        buf.write("\7\4\2\2\u025d\u025e\5R*\2\u025e{\3\2\2\2\u025f\u0263")
        buf.write("\5\u0082B\2\u0260\u0263\5\u0080A\2\u0261\u0263\5~@\2\u0262")
        buf.write("\u025f\3\2\2\2\u0262\u0260\3\2\2\2\u0262\u0261\3\2\2\2")
        buf.write("\u0263\u0264\3\2\2\2\u0264\u0265\7\65\2\2\u0265}\3\2\2")
        buf.write("\2\u0266\u0267\7\5\2\2\u0267\u0268\5&\24\2\u0268\u0269")
        buf.write("\5R*\2\u0269\177\3\2\2\2\u026a\u026d\7\5\2\2\u026b\u026e")
        buf.write("\5F$\2\u026c\u026e\5r:\2\u026d\u026b\3\2\2\2\u026d\u026c")
        buf.write("\3\2\2\2\u026e\u026f\3\2\2\2\u026f\u0270\7\65\2\2\u0270")
        buf.write("\u0271\5&\24\2\u0271\u0272\7\65\2\2\u0272\u0273\5r:\2")
        buf.write("\u0273\u0274\5R*\2\u0274\u0081\3\2\2\2\u0275\u0276\7\5")
        buf.write("\2\2\u0276\u0277\7\67\2\2\u0277\u0278\7\64\2\2\u0278\u0279")
        buf.write("\7\67\2\2\u0279\u027a\7\'\2\2\u027a\u027b\7\23\2\2\u027b")
        buf.write("\u027c\5&\24\2\u027c\u027d\3\2\2\2\u027d\u027e\5R*\2\u027e")
        buf.write("\u0083\3\2\2\2\u027f\u0280\7\22\2\2\u0280\u0281\7\65\2")
        buf.write("\2\u0281\u0085\3\2\2\2\u0282\u0283\7\21\2\2\u0283\u0284")
        buf.write("\7\65\2\2\u0284\u0087\3\2\2\2\u0285\u0288\5\66\34\2\u0286")
        buf.write("\u0288\58\35\2\u0287\u0285\3\2\2\2\u0287\u0286\3\2\2\2")
        buf.write("\u0288\u0289\3\2\2\2\u0289\u028a\7\65\2\2\u028a\u0089")
        buf.write("\3\2\2\2\u028b\u028d\7\6\2\2\u028c\u028e\5&\24\2\u028d")
        buf.write("\u028c\3\2\2\2\u028d\u028e\3\2\2\2\u028e\u028f\3\2\2\2")
        buf.write("\u028f\u0290\7\65\2\2\u0290\u008b\3\2\2\2\66\u0093\u0098")
        buf.write("\u009f\u00a6\u00ac\u00bc\u00c5\u00ce\u00d5\u00dd\u00e4")
        buf.write("\u00ee\u00f9\u0111\u0113\u011f\u0121\u0130\u0132\u013a")
        buf.write("\u0141\u014e\u0150\u0163\u0170\u0172\u0177\u017d\u0187")
        buf.write("\u018f\u019a\u01a1\u01b3\u01ba\u01c1\u01c8\u01d9\u01f0")
        buf.write("\u0203\u0208\u0212\u0219\u0220\u0237\u0239\u0247\u024a")
        buf.write("\u0252\u0262\u026d\u0287\u028d")
        return buf.getvalue()


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
        self.checkVersion("4.9.2")
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared_statement_list" ):
                return visitor.visitDeclared_statement_list(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_literal)
        try:
            self.state = 150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.INTEGER_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.literal_primitive()
                pass
            elif token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.array_lit_instance()
                pass
            elif token in [MiniGoParser.ID]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_primitive" ):
                return visitor.visitLiteral_primitive(self)
            else:
                return visitor.visitChildren(self)




    def literal_primitive(self):

        localctx = MiniGoParser.Literal_primitiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_literal_primitive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.INTEGER_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMytype" ):
                return visitor.visitMytype(self)
            else:
                return visitor.visitChildren(self)




    def mytype(self):

        localctx = MiniGoParser.MytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_mytype)
        try:
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.primitive_type()
                pass
            elif token in [MiniGoParser.LBRACK]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = MiniGoParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




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
            if token in [MiniGoParser.ID]:
                self.state = 162
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_dimention" ):
                return visitor.visitArray_dimention(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_dimention_element" ):
                return visitor.visitArray_dimention_element(self)
            else:
                return visitor.visitChildren(self)




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
            if not(_la==MiniGoParser.ID or _la==MiniGoParser.INTEGER_LIT):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit_instance" ):
                return visitor.visitArray_lit_instance(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_array_value" ):
                return visitor.visitList_array_value(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_array_value_element" ):
                return visitor.visitList_array_value_element(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_lit_instance" ):
                return visitor.visitStruct_lit_instance(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_lit_instance_body" ):
                return visitor.visitStruct_lit_instance_body(self)
            else:
                return visitor.visitChildren(self)




    def struct_lit_instance_body(self):

        localctx = MiniGoParser.Struct_lit_instance_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_struct_lit_instance_body)
        try:
            self.state = 204
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.struct_lit_instance_body_prime()
                pass
            elif token in [MiniGoParser.RBRACE]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_lit_instance_body_prime" ):
                return visitor.visitStruct_lit_instance_body_prime(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_lit_instance_body_element" ):
                return visitor.visitStruct_lit_instance_body_element(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expression" ):
                return visitor.visitList_expression(self)
            else:
                return visitor.visitChildren(self)




    def list_expression(self):

        localctx = MiniGoParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_list_expression)
        try:
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LPAREN, MiniGoParser.LBRACK, MiniGoParser.ID, MiniGoParser.INTEGER_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.list_expression_prime()
                pass
            elif token in [MiniGoParser.RPAREN]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expression_prime" ):
                return visitor.visitList_expression_prime(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)



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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)




    def expression5(self):

        localctx = MiniGoParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expression5)
        try:
            self.state = 312
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.match(MiniGoParser.NOT)
                self.state = 308
                self.expression5()
                pass
            elif token in [MiniGoParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
                self.match(MiniGoParser.SUB)
                self.state = 310
                self.expression5()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LPAREN, MiniGoParser.LBRACK, MiniGoParser.ID, MiniGoParser.INTEGER_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)



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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_call" ):
                return visitor.visitMethod_call(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTemp_expression6" ):
                return visitor.visitTemp_expression6(self)
            else:
                return visitor.visitChildren(self)



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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_statement" ):
                return visitor.visitList_statement(self)
            else:
                return visitor.visitChildren(self)




    def list_statement(self):

        localctx = MiniGoParser.List_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_list_statement)
        try:
            self.state = 373
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 371
                self.list_statement_prime()
                pass
            elif token in [MiniGoParser.EOF]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_statement_prime" ):
                return visitor.visitList_statement_prime(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared_statement" ):
                return visitor.visitDeclared_statement(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables_declared" ):
                return visitor.visitVariables_declared(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables_declared_without_semi_for_loop" ):
                return visitor.visitVariables_declared_without_semi_for_loop(self)
            else:
                return visitor.visitChildren(self)




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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstants_declared" ):
                return visitor.visitConstants_declared(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declared" ):
                return visitor.visitFunction_declared(self)
            else:
                return visitor.visitChildren(self)




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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_function_parameter" ):
                return visitor.visitList_function_parameter(self)
            else:
                return visitor.visitChildren(self)




    def list_function_parameter(self):

        localctx = MiniGoParser.List_function_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_list_function_parameter)
        try:
            self.state = 440
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 438
                self.list_function_parameter_prime()
                pass
            elif token in [MiniGoParser.RPAREN]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_function_parameter_prime" ):
                return visitor.visitList_function_parameter_prime(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_function_parameter_element" ):
                return visitor.visitList_function_parameter_element(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.COMMA:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_body_container" ):
                return visitor.visitFunction_body_container(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declared" ):
                return visitor.visitMethod_declared(self)
            else:
                return visitor.visitChildren(self)




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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReceiver_container" ):
                return visitor.visitReceiver_container(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_declared" ):
                return visitor.visitStruct_declared(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_declared_body" ):
                return visitor.visitStruct_declared_body(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_declared_body_element" ):
                return visitor.visitStruct_declared_body_element(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_declared" ):
                return visitor.visitInterface_declared(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_declared_body" ):
                return visitor.visitInterface_declared_body(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_declared_element" ):
                return visitor.visitInterface_declared_element(self)
            else:
                return visitor.visitChildren(self)




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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_parameter_container" ):
                return visitor.visitInterface_parameter_container(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_interface_parameter" ):
                return visitor.visitList_interface_parameter(self)
            else:
                return visitor.visitChildren(self)




    def list_interface_parameter(self):

        localctx = MiniGoParser.List_interface_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_list_interface_parameter)
        try:
            self.state = 528
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 526
                self.list_interface_parameter_prime()
                pass
            elif token in [MiniGoParser.RPAREN]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_interface_parameter_prime" ):
                return visitor.visitList_interface_parameter_prime(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_interface_parameter_element" ):
                return visitor.visitList_interface_parameter_element(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.COMMA:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_operator" ):
                return visitor.visitAssignment_operator(self)
            else:
                return visitor.visitChildren(self)




    def assignment_operator(self):

        localctx = MiniGoParser.Assignment_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_assignment_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 552
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN_STATE) | (1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs_assignment_statement" ):
                return visitor.visitLhs_assignment_statement(self)
            else:
                return visitor.visitChildren(self)



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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement_without_semi_for_loop" ):
                return visitor.visitAssignment_statement_without_semi_for_loop(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==MiniGoParser.ELSE:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if_clause" ):
                return visitor.visitElse_if_clause(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if_clause_content" ):
                return visitor.visitElse_if_clause_content(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_clause" ):
                return visitor.visitElse_clause(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_for_loop" ):
                return visitor.visitBasic_for_loop(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitialization_for_loop" ):
                return visitor.visitInitialization_for_loop(self)
            else:
                return visitor.visitChildren(self)




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
            if token in [MiniGoParser.VAR]:
                self.state = 617
                self.variables_declared_without_semi_for_loop()
                pass
            elif token in [MiniGoParser.ID]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_for_loop" ):
                return visitor.visitArray_for_loop(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INTEGER_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
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
         




