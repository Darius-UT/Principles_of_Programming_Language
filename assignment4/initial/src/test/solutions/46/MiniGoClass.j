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
	iconst_2
	anewarray [Ljava/lang/String;
	dup
	iconst_0
	iconst_3
	anewarray java/lang/String
	dup
	iconst_0
	ldc ""
	aastore
	dup
	iconst_1
	ldc ""
	aastore
	dup
	iconst_2
	ldc ""
	aastore
	aastore
	dup
	iconst_1
	iconst_3
	anewarray java/lang/String
	dup
	iconst_0
	ldc ""
	aastore
	dup
	iconst_1
	ldc ""
	aastore
	dup
	iconst_2
	ldc ""
	aastore
	aastore
.var 1 is a [[Ljava/lang/String; from Label0 to Label1
	astore_1
	aload_1
	iconst_0
	aaload
	iconst_0
	ldc "VOTIEN"
	aastore
	new java/lang/StringBuilder
	dup
	invokespecial java/lang/StringBuilder/<init>()V
	aload_1
	iconst_0
	aaload
	iconst_0
	aaload
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	aload_1
	iconst_0
	aaload
	iconst_1
	aaload
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
	return
Label1:
.limit stack 7
.limit locals 2
.end method
