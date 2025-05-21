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
	ldc "a"
.var 1 is local Ljava/lang/String; from Label0 to Label1
	astore_1
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
	ldc ""
.var 2 is local2 Ljava/lang/String; from Label0 to Label1
	astore_2
	aload_2
	invokestatic io/putStringLn(Ljava/lang/String;)V
	return
Label1:
.limit stack 2
.limit locals 3
.end method
