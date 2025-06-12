<div  align="center">

<img  src="https://hcmut.edu.vn/img/nhanDienThuongHieu/bk_name_en.png"  alt="HCMUT logo"  width="700">

</div>

<div  align="center">

<a  href="">

<img  src="https://static.vecteezy.com/system/resources/previews/048/332/163/non_2x/python-3d-icon-transparent-background-free-png.png"  alt="Golang logo"  width="140"  height="140">

</a>

<a  href="">

<img  src="https://static-00.iconduck.com/assets.00/file-type-antlr-icon-1024x1023-79rcs87c.png"  width="140"  height="140">

</a>

<h1  align="center">Principles of Programming Language</h1>

</div>

## Introduction

- Semester: 242
- Student: Nguyễn Lê Hoàng Phúc
- ID: 2212629
- Lecturer: Master Trần Ngọc Bảo Duy
- Minigo Specification Desiger & Inital source code Provider: PhD Nguyễn Hứa Phùng

![Ê Ê](https://media3.giphy.com/media/0jjALjfIMKeuGjyI22/200w.gif?cid=6c09b952e24dp2bli4t4dgbz3hyi0j615qctqhi6jyn50dex&ep=v1_gifs_search&rid=200w.gif&ct=g)

## About this assignment

These four assignments of Principles of Programming Language subject aim to introduce and guide students to create a simple Compiler based on specification of a new programming language - [Minigo](specifications/MiniGo_Specification.pdf). The primary model of Minigo is "Golang" which is an extremely strong and useful language developed by Google.

The project focuses on the fundamental programming language implementation, through five primary stages:

1. Lexical Analysis ([Assignment 1](assignment1/initial)):
    - Use: Regular Expression (ANTLR);
    - Self-implementing files: MiniGo.g4, LexerSuite.py.
2. Syntax Analysis ([Assignment 1](assignment1/initial)):
    - Use: Context Free Grammar (ANTLR);
    - Self-implementing files: MiniGo.g4, LexerSuite.py.
3. Abstract syntax tree Generation ([Assignment 2](assignment2/initial)):
    - Use: Python;
    - Self-implementing files: ASTGeneration.py, ASTGenSuite.py.
4. Semantic Analysis ([Assignment 3](assignment3/initial)):
    - Use: Python;
    - Self-implementing files: StaticCheck.py, CheckSuite.py.
5. Intermediate code Generation ([Assignment 4](assignment4/initial)):
    - Use: Python;
    - Self-implementing files: CodeGenerator.py, Emitter.py (partial), CodeGenSuite.py.


## Result in class

This result was calculated based on the total number of correct testcases (compared to Author PhD Nguyễn Hứa Phùng):

- Assigment 1: Lexer(100/100) + Parser (100/100).

- Assigment 2: 95/100.

- Assignment 3: 118/125.

- Assigment 4: 95/101.