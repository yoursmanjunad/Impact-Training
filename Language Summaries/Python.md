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
- IN python we have no need to define a data type before we declare a variable. Even though we dont declare the type of data, interpreter automatically recognize the type of data and allocates the size accordingly. 
- If we try to run `0 = X` it prints `Syntax Error`
- Variables are case sensitive. The right way to declare a variable is `a = 10` format in where the name comes to the left known as **reference variable** and 10 which is typically a value, can comes to the right which is generally called as **Object**
- `=` does refer to the value when we call the **name** of a variable.
- When we try to assign multiple variable's values in one go we should do this 
```commandline
a,b,c = 1,2,3
```
- Which prints`1,2,3` instead if you try this
```commandline
a,b,c = 1,2 - or
a,b = 1,2,3
```
- prints error as `valueError` Like if you need more arguments from the calling of a function, we get error as here. 
### Throwaway variable in Python
- We mostly don't have this feature in other languages, in python to declare a throwaway, i.e temporary variable we use `_` variable in which we can store the values for temporary. 
```commandline
a,b,_ = 1,2,3
# prints 1,2 
```
- It doesn't stores the value, just to fit into the situation it doesn't have any features. But if we try to run, 
```commandline
a,b,_ = 1,2,3,4
```
- prints `valueError` as same discussed before we have less number of arguments as compared with right side.
### Same reference 
```commandline
a, b, c = 1
```
- three variables refer (points) to the same object called `1`. It's address is the same but the referencing variables are different. Instead of creating multiple duplicate values (objects) python helps us to refer to the same one. 
- If any variable's value has changed later, then it's referencing points does also changes. 
- This is same for mutable and immutable types in Python. 
### Indentation
- In python, basically to denote a block, we use `{}`braces but here in py, we use `:` to indicate a block.
```commandline
if a > b:
    print("Hello")
```
- the space below the line decides the block which it belongs to. If there is no space, then it comes into the main function or general line of code insstead which it belongs to a block. 
```commandline
Still, 
if a>b : print("Hello")
```
- is acceptable. But, having multiple lines in this manner, prints `Syntax Error`.
- When an empty block is defined, it prints `indentation Error`. 
- To come across defining a block empty, we can use `pass` keyword so that, it neglects the empty block. 
```commandline
def we_use_this_later():
    pass
```
**Use `spaces` for indentation instead of `tab` which is equal to `4` spaces, `PEP8` the style guide for python suggests this**
- In python `\t` tab indicates 8 spaces and `tab` button indicates 4 spaces. 
### Data types
- In python, `Not`, `and`, `or` keywords are used to represent booleans. 
```commandline
x or y # if X then x else Y
x and y# if X fails then X else Y
not X # if X is True then False else True
```
- If boolean values are used in Arithmetic, then it will be treated as `0` and `1`
```commandline
True + False = 1 (1+0)
True * True = 1 (1*1)
```
- `<`,`<=`,`>`,`>=` operators raise `Type Error` if we use `Complex Numbers` as **Operands**
##### Tuple: 
- It is an ordered list, in which we store elements orderly 
- Tuple is `Immutable`
- We can access the elements in the index values, but when you try this 
```commandline
tupple_Ex = (1,2,3,4,5)
tupple_Ex[2] = 33 #Prints `Type Error`
```
##### List:
- When it comes to list, we can use it using indexing and mutable.
```commandline
list = [1,2,3,4]
print[2] #allowed
```
- `Ellipsis` **...** is mostly used in `numpy` which used to include all elements in the Array. 
- Using `<`,`<=`,`>`,`>=` for `Null` returns **Type Error**
- To test a type of a value, use `type(variable_name)`
### Differences between `Type` and `isinstance` keyword

**Solve this**
```commandline
X = None
if X is None:
    print("I've just declared X as None, not a surprise")
```
#### Conversion
- We can convert one data type to another, using the inbuilt functions as 
- `int()`
- `float()`
- `list()`
- `set()`
- `tuple()`
- `set()`
- If we try to print `int` into `float` it prints `ValueError`
- If we try to change a value of a list or anything it is `Mutable` else `Immutable`
- `byteArray`, `set`, `list` and `dict` are types in which we can modify the value, else we cannot change in others. 
```commandline
print(str[0:5]) #prints the elements from 0to 4th index means 5 elements. 
```
### Collection Types. 
- Types like `int`, `String` holds a single value. But in Collection types it holds multiple values in the same type. 
## List:
- List is more thn array, more likely used in `JavaScript`. 
- In list, we can add hetrogenous elements like `int`, `string`, `float`, etc. 
- The list can be empty and when we print it, it gives us `[ ]` as output. 
- And a list can be included in another list. 
- List is `0-indexed` collection just as `Array` and also allowed for `reverse` using `-1` and so on. 
- To add new element into the list, use `lisst.append("Manjunath")` which adds this to the list. 
- To add a element into list at **particular Index** we use `list.insert(1,"Manjunath")` to insert that at a particular index. 
- To remove the first occurance of a value in the list, we use `list.remove(value)`
- To get a **particular index** value of a lisst, we use `list.index(value)` which returns the index value. 
- To get the length of a list, we use `len(list)`
- To get the count of a particular value's present in the list, we use `list.count(1)` which returns the number of 1s present in the list. 
- To reverse the list, we use `list.reverse()` or use this as `list[::-1]`
- To remove a value in the list we use `list.pop()` method which removes the last value in the list by `default`
- `list*2` gives the output as 
```commandline
list = ['hello', 'world']
print(list*2)
# ['hello','world',hello','world']
```
- `list1 + list2` prints the concatenation of two lists. 
**Tuples**
- 
- Tuples are same as the `list`, but the values int the `tuples` are immutable and it mostly used to store the values which are unchanged such as `IP Adddreses` , `Port` etc.
- We can concatenate multiple tuples and print them directly.
## Dictionary
- It is a key value paired collection, here we use curly braces. 
```commandline
print(dic)
print(dic['names'])
print(dic[''key']])
print(dic['keys'])
```
## Sets
- In sets, we cannot include the duplicate elements. It is mutable.
```commandline
set  a= {'abracadabra'}
print(a) # removes all dupliactes and prints in list format. 
```
#### Logic Operations in Sets: 
- To perform **Intersection** we use `set1.intersection(set2)` or we can use `&` operator. 
- To perform **Union** we use `set1.union(set2)` or we can use `|` operator
- To perform **Difference** we use `set1.difference(set2)` or we can use `-` operator. 
- To perform **Symmetric Difference** between them `set1.symmetric_difference(list2)`
- To perform **subset** we use `set1.issubset(set2)`
- To check an element's existence in set, we use `value in set` returns **True** or **False** and `not in` is like reverse of it. 
- To add an element into the set, we use `set.add(value)`
- To remove an element we use `set.discard(value)` if the value present it removes it else, it doesn't perform anything. 
- But, if we use `set.remove(value)` it removess the value, if it is not present, it returns as error as `key Error`
- To get a unique eements of a list we use
```commandline
list = ["McDownels Murty", "Jalebi", "Lavangam", "Miriyam", Miriyam", "Pedda Reddy"]
print(set(list))
```
- It prints the values of the list which have removed the duplicates. 
- `list(set(list))` returns a list in which the duplicates been removed. 
- Implementing sets in set leads to `TypeError` 
- So, to implement that we use **frozensets**
```commandline
{frozenset({1,3}), frozenset({3,4})} #allowed
```
### Loops
- We cannot use `break` statement else where of `loops`. 
```commandline
for i in range(0,10):
    print("Hello",i)
    if i == 6:
        break
```
- We cannot proceed into further loops if we use `break` at certain iteration. 
- Then to proceed to the next iteration by skipping the current according to the conditionals, then we use `continue`. 
```commandline
for i in range(1,11):
    if i == 6:
        continue
    print("Hello",i)
```
- As discussed before, to come out of loops at certain level, we use `break` and to do the same in functions, e use `return` keyword. 
- To print the index values and elements in the list or array, we can use `enumerate`
```commandline
for index, item in enumerate(['alex','apple','banana','samsung'])
    print(index, '::',item)
```
- `pass` is a null statement, which helps us to not to do anything. 
```commandline
for i in range(1,11):
    if i == 6:
        pass
    print("Hello",i)
```
- To iterate over dictionaries. 
```commandline
for i in d:
    print(key)
  0r 
for i in d.keys:
    print(key)
  or
for value in d:
    print(value)
  or
for key, values in d.items:
    print(key,'::',values)
```
- To iterate over particulaar range, 
```commandline
for i in range[3::5]:
    print("fwef")
```
## Arrays
- In python, to implement `Arrays` we have to import `from Arrays import *`
- **array_Name = array('typecode',[initializers])**
- We can append any value to the array using `arr.append('value')`
- To insert an element at a particular index, we use `arr.insert(0,0)` 
- To concatenate two arrays, we can use `extend`
 method
```commandline
arr1 = array('i',[1,2,3,4])
arr2 = array('i',[5,6,7,8])
arr1.extend(arr2)
```
- To add elements from list to array, use `fromlist()` method. 
```commandline
arr1 = arrray('i',[1,2,3,4])
list = [6,7,8,9]
arr1.fromlist(list)
```
- To remove any element, we can use `arr.remove(value)` and also can use `pop` method to remove last element. 
- We can get the first index value of element, `arr.index()`
- We can reverse it using `arr.reverse()`
- To count number of elements of particular value, `arr.count(value)`
- convert array to string using `arr.tostring()`
- convert array to list using `arr.tolist()`
- Append a string to char array using `arr.fromstring()`
- `print(arr.remove(1))` prints **None**

## Dictionary  
```commandline
# Creating dictionary.
example = {'Name': 'Manjunath', 'RollNo': 54, 'Field':'DevOps'}
example2 = {'Name': 'Hussain', 'RollNo':56, 'Field':'Xerox' }
# print('Name',example['Name'])
example.update(example2)
merged_dict = dict(example,**example2)
print(merged_dict.pop('RollNo'))
print(merged_dict)
my_dict = {'banana': 3, 'apple': 1, 'orange': 2}

# Sort the dictionary by keys and print the result
# sorted_dict_by_keys = dict(sorted(my_dict.items()))
sorted_dict_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Sorted Dictionary by Keys:",sorted_dict_by_va
```
- 