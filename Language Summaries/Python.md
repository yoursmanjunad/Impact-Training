# Python Language - Gudio Van Rossum

- This is a complete notes of language python specifically for `Placements`
- Python is a high level interpreted object oriented programming language.
- It's dynamic nature helps code to be minimal than other languages.
- Python is one of the most loved programming language in recent times and also easy to learn.
- It seems like messaging your computer do this a certain task but with indentation.
- Python gives us the ability to use a lot of modules and packages with our code, which are standard libraries built in with the interpreter.
- Python can be used in many fields as
  - Machine Learning
  - Artificial Intelligence
  - Data visualization
  - Programming Application
  - Web Applications
  - Language and Game Development
  - Data Analysis.

### How does Python Interpreter works?

- The python interpreter is called as `CPython`
- Actually, the translator starts with the source code analysis.
- Here, the Python interpreter receives the source code and initializes some instructions to
  - Check the indentation in the source file.
  - If it checks any error in syntax or incorrect lines, it will stop the program from execution to show the error message.
  - Generally, this phase is called `Lexical Analysis`
- Once the parser of the python interpreter receives the tokens, it starts to manipulate the lexical tokens.
- It generates a big structure called the **AST** Abstract Syntax Tree.
- Interpreter converts this **AST** to byte code which means machine language.
- In python, the byte code can be saved in a file ending with an extension `.pyc` extension.
- The pythn interpreter initializes its runtime engine called **PVM** Python Virtual Machine.
- The interpreter loads the machine language with the library modulus and inputs it into the PVM.
- This converts the byte code into executable code (binaries)
- If any error happens during the PVM process, the executor will terminate the operation immediately to display the error.

- Comments in Python start with the hash character, #, and extend to the end of the physical line.
- A comment may appear at the start of a line or following whitespace or code, but not within a string literal.
- A hash character within a string literal is just a hash character.
- In python we have same operators as in other languages, we have some special like `**` - Power, `//` - floor division (removes the decimals after division.)
- If a variable is not “defined” (assigned a value), trying to use it will give you an error: `Name Error`
- 
