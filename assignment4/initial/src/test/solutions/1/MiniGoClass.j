.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static global I

.method public static fvoid()V
Label0:
	ldc "GiaiPhongMienNam"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	return
Label1:
.limit stack 1
.limit locals 0
.end method

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
	invokestatic MiniGoClass/fvoid()V
	getstatic MiniGoClass/global I
	i2f
	fconst_2
	fadd
	invokestatic io/putFloatLn(F)V
	ldc "a"
.var 1 is local Ljava/lang/String; from Label0 to Label1
	astore_1
	aload_1
	ldc "b"
	invokevirtual java/lang/String/compareTo(Ljava/lang/String;)I
	ifle Label2
	iconst_0
	goto Label3
Label2:
	iconst_1
Label3:
	invokestatic io/putBoolLn(Z)V
	new java/lang/StringBuilder
	dup
	invokespecial java/lang/StringBuilder/<init>()V
	aload_1
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	ldc "c"
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
	astore_1
	aload_1
	invokestatic io/putStringLn(Ljava/lang/String;)V
	return
Label1:
.limit stack 7
.limit locals 2
.end method
