# Arrays in Py
- To use arrays in Python, we need to import ```from array import *```
- This helps us to use array in our program. 
```
arrayIdentifierName = array(typecode,[Initializers])
```
- ```array.append(10)``` This method helps us to add new value into the array at the end. 
- ```array.insert(0,120)``` This method helps to add value at a particular index that is first argument
- ```array.extend(array name)``` Helps to add two arrays, also applicable for ```lists ``` aswell
- ```my_arr.fromlist(c)``` To add elements from the list to Array
- ```my_ar.fromlist(list[2:4])``` helps to slice the list and add to Array
-  ```my-arr.pop()``` To remove the last index value
- ```my_arr.reverse()```
- ```my_arr.count()```
- ```my_arr.tostring()```
- ```all()``` To chheck all the elements in the array
- ```any(nums)```
# List Comprehensions
- This is like a Enhanced Loop like in Java
# Lambda Function
- This is a inline function that contains a single expression. The value fo expression is what the function returns when invoked.
```commandline
def greeting():
    return "hello world"
print(greeting())
```
```commandline
greet_me = lambda: "Hello"
print(greet_me)
```
# Zip
# List