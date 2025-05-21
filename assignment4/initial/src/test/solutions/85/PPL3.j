.source PPL3.java
.class public PPL3
.super java/lang/Object
.implements Course
.field public number I

.method public <init>()V
.var 0 is this LPPL3; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iconst_0
	putfield PPL3/number I
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public <init>(I)V
.var 0 is this LPPL3; from Label0 to Label1
.var 1 is number I from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iload_1
	putfield PPL3/number I
	return
Label1:
.limit stack 2
.limit locals 2
.end method

.method public study()V
Label0:
.var 0 is this LPPL3; from Label0 to Label1
	iconst_5
	invokestatic io/putInt(I)V
	return
Label1:
.limit stack 1
.limit locals 1
.end method
