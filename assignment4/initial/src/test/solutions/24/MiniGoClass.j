.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static b [[F

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
	iconst_3
	anewarray [F
	dup
	iconst_0
	iconst_2
	newarray float
	dup
	iconst_0
	ldc 1.4
	fastore
	dup
	iconst_1
	bipush 64
	i2f
	fastore
	aastore
	dup
	iconst_1
	iconst_2
	newarray float
	dup
	iconst_0
	ldc 6.0
	fastore
	dup
	iconst_1
	ldc 634.2
	fastore
	aastore
	dup
	iconst_2
	iconst_2
	newarray float
	dup
	iconst_0
	ldc 10.0
	fastore
	dup
	iconst_1
	fconst_1
	fastore
	aastore
	putstatic MiniGoClass/b [[F
	return
.limit stack 7
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	getstatic MiniGoClass/b [[F
	iconst_0
	iconst_2
	newarray float
	dup
	iconst_0
	ldc 30.0
	fastore
	dup
	iconst_1
	iconst_4
	i2f
	fastore
	aastore
	getstatic MiniGoClass/b [[F
	iconst_1
	aaload
	iconst_0
	faload
	invokestatic io/putFloatLn(F)V
	getstatic MiniGoClass/b [[F
	iconst_1
	aaload
	iconst_1
	faload
	invokestatic io/putFloatLn(F)V
	return
Label1:
.limit stack 6
.limit locals 1
.end method
