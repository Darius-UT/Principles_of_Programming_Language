.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static createArray()[I
Label0:
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 10
	iastore
	dup
	iconst_1
	bipush 20
	iastore
	dup
	iconst_2
	bipush 30
	iastore
	areturn
Label1:
.limit stack 4
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
	return
.limit stack 0
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	invokestatic MiniGoClass/createArray()[I
.var 1 is a [I from Label0 to Label1
	astore_1
	aload_1
	iconst_0
	iaload
	invokestatic io/putInt(I)V
	aload_1
	iconst_1
	iaload
	invokestatic io/putInt(I)V
	aload_1
	iconst_2
	iaload
	invokestatic io/putInt(I)V
	return
Label1:
.limit stack 2
.limit locals 2
.end method
