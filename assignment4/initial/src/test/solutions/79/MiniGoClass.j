.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a I
.field static c I

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
	iconst_1
	iconst_1
	iadd
	putstatic MiniGoClass/a I
	iconst_5
	getstatic MiniGoClass/a I
	isub
	putstatic MiniGoClass/c I
	return
.limit stack 2
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	getstatic MiniGoClass/a I
	anewarray [I
	dup
	iconst_0
	getstatic MiniGoClass/c I
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_0
	iastore
	dup
	iconst_2
	iconst_0
	iastore
	aastore
	dup
	iconst_1
	getstatic MiniGoClass/c I
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_0
	iastore
	dup
	iconst_2
	iconst_0
	iastore
	aastore
.var 1 is b [[I from Label0 to Label1
	astore_1
	aload_1
	iconst_0
	aaload
	iconst_0
	iaload
	invokestatic io/putInt(I)V
	aload_1
	iconst_0
	aaload
	iconst_0
	bipush 20
	iastore
	aload_1
	iconst_0
	aaload
	iconst_0
	iaload
	invokestatic io/putInt(I)V
	return
Label1:
.limit stack 7
.limit locals 2
.end method
