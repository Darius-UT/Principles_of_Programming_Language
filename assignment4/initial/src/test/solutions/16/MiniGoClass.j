.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a F

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
	ldc 3.0
	putstatic MiniGoClass/a F
	return
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	getstatic MiniGoClass/a F
	invokestatic io/putFloatLn(F)V
	ldc 4.0
.var 1 is a F from Label0 to Label1
	fstore_1
	fload_1
	invokestatic io/putFloatLn(F)V
	iconst_2
	i2f
	fstore_1
	fload_1
	invokestatic io/putFloat(F)V
	return
Label1:
.limit stack 1
.limit locals 2
.end method
