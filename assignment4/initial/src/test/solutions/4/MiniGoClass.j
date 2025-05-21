.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static global I

.method public static fint()I
Label0:
	iconst_1
	ireturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
	invokestatic MiniGoClass/fint()I
	putstatic MiniGoClass/global I
	return
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	iconst_2
.var 1 is local I from Label0 to Label1
	istore_1
	return
Label1:
.limit stack 1
.limit locals 2
.end method
