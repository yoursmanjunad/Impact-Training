# Day 14
- List implementation
- class have properties which are governed by methods
- It's about designing the class not about coding. It's design should be more effective that makes your class to implement in better way. `SOLID ` Principles
- Validations are important towards the properties, while designing the class. 
## Stack
- Last In First Out
- In stacks and queues, we have limitation of the size. Just like an array but differs in the way we store,retrive and print the data. 
- To print built in private variables, print dir() in terminal. 
- If we declare new variable, if adds into the same stack of inbuilt variables. 
```commandline
print(dir())
num = 10
print(dir())
n = 1223
def fun():
    n = 1223 #If we comment it, python searches for the same variable within the program out of scope and prinits it's value
    print("Inside the function, we have ", n)
fun()
```
- But if we try to perform some operations based on that, to modify the globla variable we get `OutBound Error`
- It means we can use it, but we cannot `Manipulate it`
- Can we make an array `Mutable?`
- In C we use `Extern`keyword to make it global
- IF we try to define a globla variable in a function scope, it throws `Syntax Error`
- If we want to modify the variable value in a inner function of a outer function variable, it throws `Error`
- Enclosure, Global, Local scope rules
- 