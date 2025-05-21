.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static b I

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
	bipush 124
	putstatic MiniGoClass/b I
	return
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_0
	iastore
.var 1 is a [I from Label0 to Label1
	astore_1
	aload_1
	iconst_0
	bipush 100
	iastore
	aload_1
	iconst_1
	aload_1
	iconst_1
	iaload
	aload_1
	iconst_0
	iaload
	aload_1
	iconst_0
	iaload
	iadd
	iadd
	iastore
	aload_1
	iconst_1
	iaload
	invokestatic io/putInt(I)V
	bipush 42
	putstatic MiniGoClass/b I
	getstatic MiniGoClass/b I
	invokestatic io/putInt(I)V
	return
Label1:
.limit stack 6
.limit locals 2
.end method
