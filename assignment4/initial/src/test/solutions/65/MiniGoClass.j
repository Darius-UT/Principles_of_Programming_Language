.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

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
	return
.limit stack 0
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	iconst_3
	anewarray [[F
	dup
	iconst_0
	iconst_2
	anewarray [F
	dup
	iconst_0
	iconst_4
	newarray float
	dup
	iconst_0
	fconst_0
	fastore
	dup
	iconst_1
	fconst_0
	fastore
	dup
	iconst_2
	fconst_0
	fastore
	dup
	iconst_3
	fconst_0
	fastore
	aastore
	dup
	iconst_1
	iconst_4
	newarray float
	dup
	iconst_0
	fconst_0
	fastore
	dup
	iconst_1
	fconst_0
	fastore
	dup
	iconst_2
	fconst_0
	fastore
	dup
	iconst_3
	fconst_0
	fastore
	aastore
	aastore
	dup
	iconst_1
	iconst_2
	anewarray [F
	dup
	iconst_0
	iconst_4
	newarray float
	dup
	iconst_0
	fconst_0
	fastore
	dup
	iconst_1
	fconst_0
	fastore
	dup
	iconst_2
	fconst_0
	fastore
	dup
	iconst_3
	fconst_0
	fastore
	aastore
	dup
	iconst_1
	iconst_4
	newarray float
	dup
	iconst_0
	fconst_0
	fastore
	dup
	iconst_1
	fconst_0
	fastore
	dup
	iconst_2
	fconst_0
	fastore
	dup
	iconst_3
	fconst_0
	fastore
	aastore
	aastore
	dup
	iconst_2
	iconst_2
	anewarray [F
	dup
	iconst_0
	iconst_4
	newarray float
	dup
	iconst_0
	fconst_0
	fastore
	dup
	iconst_1
	fconst_0
	fastore
	dup
	iconst_2
	fconst_0
	fastore
	dup
	iconst_3
	fconst_0
	fastore
	aastore
	dup
	iconst_1
	iconst_4
	newarray float
	dup
	iconst_0
	fconst_0
	fastore
	dup
	iconst_1
	fconst_0
	fastore
	dup
	iconst_2
	fconst_0
	fastore
	dup
	iconst_3
	fconst_0
	fastore
	aastore
	aastore
.var 1 is a [[[F from Label0 to Label1
	astore_1
	aload_1
	iconst_0
	aaload
	iconst_1
	aaload
	iconst_0
	ldc 124.4
	fastore
	aload_1
	iconst_0
	aaload
	iconst_1
	aaload
	iconst_0
	faload
	invokestatic io/putFloat(F)V
	return
Label1:
.limit stack 10
.limit locals 2
.end method
