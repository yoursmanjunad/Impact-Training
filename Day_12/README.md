# File Handling
1. `open()` it takes two arguments the name of the file and the mode in which we want to open the file
```commandline
file = open("example.com", r) 
```
- There are other modes like writing, append etc with `w` and `a` keywords 
- For both read and write `r+`
- reading a specific number of characters `file.read`
- to read specific number of characters from a file, `file.read(100)`
- to read a single line from file, `file.reaedine()`
- to read and store it in a list, `file.readlines()`
- `file.write` used to write inside a file. 
- to close a file, use `file.close()`
- if we use `with` keyword, we have no need to use `file.close()` method explicitly. 
- It will automatically closes the file after the completion of the block
# Class
- Unline Java, we can create objecct in Python without using `new ` keyword
- `self` keyword represents current object
- Constructor
- 4 OOPS Concepts ->
    - Inheritance
    - Encapsulation
    - Polymorphism
            - Method Overloading
            - Method Overridng
    - Abstraction
