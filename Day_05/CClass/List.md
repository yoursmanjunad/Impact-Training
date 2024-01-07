## Lists

**1. Function Objects:**

- When you define a function in Python, a function object is created. This object contains metadata about the function, including its bytecode (the compiled version of the function's code), default argument values, and other related information.
  This function object is stored in memory, and its memory is managed by Python's memory manager

**2. Local Variables and Call Stack:**

- When a function is called, a new frame is created on the call stack. This frame contains space for local variables, parameters, and bookkeeping information.
  Local variables within the function are allocated memory within this frame. The frame acts as a container for everything related to the function call.
  When the function completes its execution, its frame is popped off the call stack, and the memory for local variables is released.

**3. Reference Counting:**

- Python uses a reference counting mechanism as a part of its memory management. Each object in memory has a reference count, and this count is incremented when a reference to the object is created and decremented when a reference goes out of scope or is explicitly deleted.
  Memory for an object is deallocated when its reference count drops to zero, indicating that there are no more references to that object.

**4. Garbage Collection:**

- In addition to reference counting, Python employs a garbage collector that helps identify and collect circular references or objects that are not reachable.
  The garbage collector periodically runs in the background to clean up memory that may not be freed by reference counting alone.

**5.Closures and Function Objects:**

Python supports closures, where a nested function can capture and remember the values of variables from the enclosing lexical scope, even after the outer function has finished execution.
The memory for these captured variables is managed by the runtime, and the garbage collector handles their cleanup when they are no longer needed.

**6. Memory for Function Arguments:**

Immutable objects (like integers, strings, and tuples) are passed by value. When a function receives an immutable object as an argument, it gets a reference to the object.
Mutable objects (like lists and dictionaries) are passed by reference. The function receives a reference to the same object in memory, allowing modifications to affect the original object.

- to delete del list [index_val]
- Length, repeatition, concatenation, membership, iteration, offset starts, negative indexing, slicing section
- `cmp[list1,list2]` - Compare two lists
- `len(list)` - length of a list
- `max(list)` - maximum element in the list
- `min(list)` - minimum element in the list.
- `list(seg)` - converts a tuple into a list
- `list.append()` - adding new element into list at the end. If we pass more lists as arguments it throws **Type error**
- `list.extend()` - concatenates two lists with an existing one. If we pass more lists as arguments it throws **Type error**
- `list.count()` - This method need exactly one argument, else it throws **Type Error**
- `list.index()` - returns the index of a particular element
- `list.insert(index,obj)` - It enables us to insert the element object at particular index value, if the index is not present in the list, then it adds the element at the end of the list. if we try to access that element with the index which we've given in the argument, it throws the `index error`.
- `list.pop[obj=list[-1]]` - To remove at particular **index** element
- `list.remove(obj)` - It removes the particular **element** of the list.
- `list.reverse()` - just reverses the list
- `list.sort(func())` - sorts the list in ascending order
- `(l2,sum(l2))` - returns the sum of a list
- `list.clear` - Removes all the elements in the list, just like `del [a:]`. If we clear a list and print it, compiler throws **None** in the terminal.

### Sort vs Sorted method

```
print(id(l2))
var = sorted(l2)
print(var)
```

###### we get none if we store the sorted list to another var. It happens because sort method is used for **in place sorting** , but for making new sorted list, we use sorted(l2) and assigns the sorted list to the variable which we;ve assigned it

# constant iterators

- Continuous Iterator is a simple iterator class that starts from a given value (start) and increments continuously. It overrides the necessary operators (\*, ++, ==, !=) to make it usable in range-based loops.

- Remember that using continuous iterators without an explicit end condition can lead to infinite loops, so be cautious when implementing and using them.
