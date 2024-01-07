# C Language

- It was developed by `Denies Ritchie`
- C language is termed as a **High level assembly language** because,

1. The control constructs and structured data types found in high level languages.
2. Bit Manipulation, use of register variables only found in Assembly language.

```
#include<stdio.h>
int gloablnum;
int main(){
    int localNum = 0;
    printf("Hello, %d",localnum);
    return 0;
}
```

### Structure of C

#### Comments:

- These are lines written in normaly daily language on purpose for understanding what the program is all about and what we can expect from this program, etc.

#### Pre- Processor Controls

- It is the first part of the compiler to run.
- Always starts with `#`

#### Global Data Definitions

- These defines the external variables that are widely available for use in the main programs and program functions.

#### Function Definitions

- These will contain both data definitions and code instructions to be executed while the program runs.
- Every C program contains one function named `main`.
- When a C program executed the operating system calls the `main()` to begin the program's execution. And it can be defined only once.
- We can end C program in three ways

  - **exit ()**-> It is part of `stdlib.h` library and can be used to terminate the program. It takes an integer argument that represents the exit status.

  ```
  #include<stdio.h>
  #include<stdlib.h>
  int main(){
    printf("Program is ending.. );
    exit(0);
  }
  ```

  - **return**- It is most frequently used method to close a program. Generally ussed to terminate a function and return a value to the calling function.
  - **\_Exit()** function also part of `stdlib.h` library, but it doesn't perform any cleanup operations like calling functions registered with `atexit()`. It's more abrupt teermination.

  ```
  #include<stdlib.>
  int main(){
    printf("Program);
    _Exit(0);
  }
  ```

  - **Return from main**: When the `main` function reaches its closing brace, the program implicitly terminates. If the return type of main is void, it is equivalent to returning 0.
  - **Abort** - This function is defined iin `stdlib.h` used to terminatte the program abruptly. It generates a core dump and often used to handle critical errors.

  ```
  #include <stdlib.h>

  int main() {
    printf("Program is ending.\n");
    abort(); // Abnormal termination
  }
  ```

- Ending a program abruptly typically refers to terminating the program unexpectedly and forcefully, without completing its normal execution flow.
- This can happen due to various reasons, such as encountering a critical error or an unrecoverable condition.
- When the program is terminated abruptly, it may not have the opportunity to clean up resources, close files, or perform other essential tasks before exiting.

**This can cost...**

- `Resource Leaks` (such as allocated memory, open files, or networrk connections.)
- Can also lead to resource leaks and potentially `degrade the system's performance over time.`
- `Risk of data loss` or corruption. For example if a program is writing to a file or a database, the data left may be incomplete or in `inconsistent state.`
- It can also lead to the unpredictable behavior of the program, which makes hard to diagnose the cause of the termination.

Still, we use in industry because...

- **Debugging**
  During software development, abrupt termination can be a helpful debugging tool. When a critical condition is encountered, forcing an abrupt exit and generating a core dump allows developers to analyze the program's state at the time of failure.
  - This information aids in identifying and fixing the root cause of the problem.
- **Fail-Fast Principle**
  The "fail-fast" principle suggests that a program should terminate as soon as an error is detected to prevent cascading failures or the propagation of incorrect data. In scenarios where immediate termination is preferred over attempting to recover from an error, functions like abort() can be employed.
- **Security Measures**
  In some security-sensitive applications, an abrupt termination might be a part of the security strategy. If a program detects potential security breaches or unauthorized access, terminating immediately can be a way to limit exposure and prevent further compromise

**Clean Up Process**

- Here we've used the term called Clean Up process, it means that the activities and steps taken by a program to release and deallocate resources, close open files and generally perform any necessary housekeeping tasks before the program terminates.
- This process ensures that program runs efficiently, avoids resourcce leaks and maintains system integrity.
- In order to deallocate our memory, we can use `free()` method.
  For example,

```
#include <stdlib.h>

int main() {
    // Allocate memory
    int *array = (int *)malloc(10 * sizeof(int));

    // Use the allocated memory

    // Clean up: Deallocate memory
    free(array);

    return 0;
}
```

This is just a basic example for freeing up space, we can actually work on many other stuff like closing the files, signaling etc which can be explained later.

### Declaring Data Variables

- Unlike Python, in C we have to declare a vaibale with it's datatype before they are used.
- Internally, we are just doing
  - Giving a memory space a name.
  - Suitable number of bytes are allocated
  - The compiler knows how to treat the data.
- There are several data types in C as
  - `int`
  - `float`
  - `short int` 16
  - `short` 32
  - `long int` 32
  - `long` about 32
  - `double` about 64
  - `long float` about 64
  - `long double` >64
  - `char` 8 bits
- The `char`, `int`, `short`, and `long` types can be preceded by the qualifiers `signed ` or `unsigned`.
- The default is **signed**.
- `char` type is suitable for storing a character, but compiler also let to be used to store numbers.
- The number of bytes to be stored depends on **compiler**.
- **Long float** is identical to **double**
- have an **L** or **l** suffix, the number is a signed long integer. Ex: `42L` `99L`
- have a `U` or `u` suffix, the number is an unsigned integer. `42U`.
- have both `U` and an `L` suffix the number is an `unsigned long integer`.
- Contains a decimal point or scientific 'e' notation, the number is of type `double`. Ex: `7.3`, `42e-1`, `12.34E+4`
- contain a decimal point or scientific **'e' notation** and an F or f suffix the number
  is of type float eg. ` 7.3F``,  `42e-1f`
- contain a decimal point or scientific **'e' notation** and an L or l suffix the number is of type **long float** eg. `7.3L, 42e-1l`

### Character Constants

- `\n` - newline
- `\r` - The carriage return character (\r) is used to move the cursor or pointer to the beginning of the current line.
- `\f` - The form feed character is a non-printable control character that historically had a specific role in controlling the pagination or formatting of documents, particularly in the context of printed output.
- `\t` - tab
- `\b` - backspace
- `\a` - The \a escape sequence in C programming represents an audible alert or alarm character. When this character is encountered in a string or character constant and is printed or displayed, it triggers a system-specific audible alert or beep sound. This alert is intended to draw attention to a particular event or condition in the program.
- `\0` - null
- `\\` - backslash
- `\` - prime

#### Character Constants and String Constants

- Characters represented with the \ notation can also be used in strings. Strings are enclosed between " " and have an impiled null character at the end.
- A string constant cannot be spread over more than one line. However, if the compiler finds two string constants with only spaces or new lines in between it will automatically concatinate the strings together.

```
The string constants "Hello the" "re Mum!"
or "Hello the"
"re Mum!"
are both equivalent to the single string constant "Hello there Mum!"
```

**'A' is not same as "A"**

- A single character in '' can be regarded as a means of expressing a numeric value corresponding to the ASCII value of the character.

- 'A' is equivalent to '\101' or '\x41' and also `65`, `0101` and `0x41`
- 'A' + 'B' is equivalent to **65+66** in C
- initialisations can be mixed with other declarations.
- If a variable not initialised, then global variables are initialised by default to **zero**.
- There is no default initialisation for local variables. They will not have starting value of zero.
- A variable my be declared as constant using the keyword `const`
- Once they are declared, they cannot have any value assigned to them or be changed in any other way, by they can be used in expressions.
  `
diam = 2*pi*rad;`

- `const` variables are must be initialised before of any use.

### Assignments and Expressions

- `- ~` operators have high precedence. these are unary negation and one's complement.
- `<<  >> ` left shift and right shift
- `& | ^` bitwise **and** **or** , **exclusive or**
- With the exception of 2 unary operators, all arithmetic operators group from left to right where precedence is equal,the unary operators group from right to left.

```
a/b*c is equivalent to (a/b)*c
-~ is equivalent to -(~a)
```

```
2(a+b) //in Mathematics valid, not in C
2*(a+b) is Valid in C
```

- Shift Operators can only be used in inteer variables (`char`, `int`, `short`, `long`)
- A right shift looses the rightmost bits and fills the leftmost bits with either zeros or ones.
- If the original variable value is negative the leftmost bits are filled with ones otherwise they are filled with seros.
- This copies the sign bit ensuring the sign of the original value is preserved.
- Unsigned integers should always have the left most bits filled with zeros.
- `bitwise operators ` are used for manipulating individual bits in byte and words.
- The `~` is a unary operator requirinng only one operand, the other bit manipulation operators require two operands.
- `~` flips all the bits in an integer.

```
ie. If fred has binary value: 0110001110110010
then ~fred has binary value: 1001110001001101
```

- `&` is an operator compares the bits of two variables or constants and gives a result with a bit set where it is set in both the first and the second operand.

```
If fred has the bits: 0110001110110010
 and joe has the bits: 0101010101010101
then fred & joe gives: 0100000100010000
```

- This is a useful operator for selectively zeroing bits.
- `^` is the bitwise exclusive operator.
- It compares the bits of twwo variables or constants and gives a result with a bit set where it is set in either the first or the second operator, but not both.
- This is a useful operator for selectively flipping bits.

#### C Handling of `char` & `short` Variables

- Whenever C handles any variables with fewer bits than `int` the first thing it does is work out the integer equivalent.
- `The char variable 01100111` is converted to `0000000001100111`
- If the variable is an unsigned char or unsigned short the left bits are
  always filled with zeros.

```
The unsigned char: 11001101
is converted to: 0000000011001101
```

If C has to handle the expression such as a+b+c then the following rules are applied
in order:

1. If any of the variables are char or short they will be converted to int.
2. If any of the variables are of type long then all char, short and int
   variables will be converted to long.
   This is done by adding either 0s or 1s to the left depending on the sign of the
   variable.
3. If any of the variables are unsigned then all signed variables are
   converted to unsigned.
   This does not involve any extra or changed bits, just a change in how the
   variable is designated.
4. If any variable is of type float all integer types are changed to the signed
   float type.
5. If any variable is of type double, all integer and float variables are
   changed to the signed double type.
6. Similarly if a long double type exists and is used in the expression then all
   other variables are changed to long double.
   NB. Many C compilers always convert all float numbers to double no matter
   what else is in the expression.

### Mixed variable Type Assignments

1. If a "smaller" variable type is assigned to a "larger" type then the conversion is the same as for mixed types in an expression.
2. If a "larger" integer type is assigned to a "smaller" type the surplus bits on the left are lost.
3. If a signed value is assigned to an unsigned variable or vice-versa the bit pattern is transferred without change.
4. If a double type is assigned to a float type some of the precision (ie.number of decimal places) is lost.Similarly if a long double is assigned to a double or float type.
5. If a real number is assigned to an integer type the fraction part is lost.
   NB. It is not rounded.
   eg. 6.9 will be truncated to 6 if assigned to an integer
