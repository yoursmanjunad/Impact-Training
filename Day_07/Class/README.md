## Memory Allocation (C, Cpp, Other...)
- Base Address + Index Value * Size_of(DATA_TYPE) **Formaula for storing data into the array**
- ### Why Indexing all starts from ZERO?
- Pointers is a Special variable that stores particular address of a variable
- **Pointer doesn't belong to any data type, it is a void type**
```commandline
int a = 10;
int *ptr
ptr = &a
printf("value %d",a)
printf("Address %d",&a)
prints the address of a's adress for ptr.
printf(" %d",*ptr) * = dereferencing 
```
- [ ] Malloc , calloc functions ()
- If **5000** is a address where we stored the value, the pointer address can be **5002**
- [ ] **Why won't we use address while taking the input for the array?**
- [ ] How an array name is sufficient to represent the array itself as a base address?
- if &* ==> nullify, then there is no symbol. 
- [ ] How do you represent array in a pointer notation
- **Name of the array is sufficient for base address**
- 
```
#include <stdio.h>
int main()
{
    // int a = 0;
    // char name[20];
    // scanf("%s", name); // for string we don't use & operator
    // scanf("%d", &a);   // for integer we use & operator
    // printf("Name = %s", name);
    int *ptr;
    int a[3] = {1, 2, 3};
    ptr = &a[0];
    printf("Address of a[0] = %u and value of a[0] is %d \n", &a[0], a[0]);
    printf("Address of a[1] = %u and value of a[1] is %d \n", &a[1], a[1]);
    printf("Address of a[2] = %u and value of a[2] is %d \n", &a[2], a[2]);
    printf("Address of a[0] = %u and value of a[0] is %d \n", &ptr, ptr);
    ptr += 1;
    printf("na[1] value using ptr = %d\n", *(ptr + 1));
    // using thumb rules
    printf("na[1] value using ptr = %d\n", *(a + 0)); // *(a + 0) = a[0] = *(&a[0])
    printf("na[1] value using ptr = %d\n", *(a + 1));
    printf("na[1] value using ptr = %d\n", *(a + 2));
    return 0;
}
//Pplaying with Pointers
```
* [Malloc](https://www.freecodecamp.org/news/malloc-in-c-dynamic-memory-allocation-in-c-explained/)
## Types of Pointers 
1. **Null Pointer**
```commandline
int *ptr = NULL;
int a[3] = {1,2,3};
 ```
2. **Dangling Pointer** - It points to the de-referencede memory, even after deleting the memory, it still points to that memory. A
3. **Void Pointer**
4. **Wild Pointer** - if The pointer made generic, it is a wild pointer
- [ ] add code for these pointers, explaination, examples, usage, internal working, etc. 
**How to avoid dangling pointer?** - By assigning NULL to the pointer after deleting the memory. By using static also, we can avoid dangling pointer. Static can be removed when the program itself dies.
- - Assigning values for array - ```arr[0] = 10``` ; etc... Using Pointer notation, we can do it as ---
```
*(ptr+0)=10
*(ptr+1)=20
```
- [ ] Know about MMU (Memory Management Unit)
### Question - 1
- [ ] WAP ```demo_04.c```and ```demo_05.c``` using Looping statements 
### Question - 2
- [ ] WAP of merging two strings alternatively using pointers 
### Question - 3
- [ ] Given 2 strings s1 and s2, modify string s1 such  that all the common characters of s1 and s2 is to  be removed aand the uncommon of s1 and s2 is to be concatenated. 

- Registor Memory Class - Will be part of our CPU instead of main memory location

## Pointers: 
- Pointer is a variable that holds the address. It is similar to an unsigned integer. 
- These pointers helps us to reference to the data indirectly. This is more compact and efficient than direct reference. 
- Commonly used in processing for arrays and often essential for passing information out of a procedure. 
### Pointer Decleration
```commandline
int *iptr;
char *cp1, *cp2;
double *addr;
struct taxcode *taxptr;
union machine_word *statptr;
```
- Actually, pointers doesn't have their own data type, it's void type. But, the datatype beofre while declaring it, indicates that pointer variable is storing integer variable's address. 
- '''*'' before ```iptr``` indicates it is storing an integer's address in it. 
- It is possible to have an address of pointer that has the address of a pointer. 
``` int **ptrptr;```
- **We can assign the address of a variable to the pointer variable using unary and & operator**
``` 
iptr = &x /* Assigns the addres of x to iptr variable*/
iptr = &ar[4] /* assigns the addressof element 4 of array ar to iptr*/
```
- A pointer can be assigned a value from another pointer, possibly with an integer offset to the address. 

```commandline
iptr1 = iptr2+3;/*assigns to iptr1 an address of the integer 3 integers on from the address of iptr2
```
- It is possible to assign asbolute address to a pointer
```commandline
iptr = 0x37f0;
```
- When assigning the value of one pointer to another, the pointers should be declared as pointing to the same datatype. Some compilers will accept an assignment of pointers to iincompatible types. But the most require a cast to be used.
- A cast is usually necessarry to assign an absoulute value to a pointer. 
```commandline
chaptr = (char*)iptr;
iptr = (int *) 0x37f0;
```
### Indirect reference using Pointers, the unary Operator * operator. 
```commandline
iptr = &x;
y = *iptr;
*iptr = y;
```
- if ```iptr``` holds the address of ```X``` then ```*iptr``` will refer to ```X``` itself and ```*iptr``` can be used wherever ```x``` could be used. 
- Where a pointer to a pointer has been declared, then double indication can be used. ``**iptrptr``
- **A pointer should always be given a suitable address before it is used!**
### Void Pointers
- It is possible to define a pointer void.
- It means, the pointer is of undefined type. Any address value can be assigned to this type of pointter but it cannot be said what type of variable it points to. 
- ** A pointer cannot be used with the * operator ** 
```
void *ptr;
ptr = &x //this is ok
x = *ptr // is not ok 
```
- To deference the pointer value directly its type must be changed with a cast. 
```
x = *( int *) ptr;

- Declaring the pointer on the same line as data variable does NOT imply that the pointer has the address of the variable;
```
int i, *ptr1; // ptr1 does not point at i!!
however, int j, *ptr2 = &j; points to the j as it has been initialised to do so. 
```
**A constant pointer means, once the pointer haas been initialized, it cannot change the address of referencing, the value may change, but it won't stop referencing to the same address**
- Because a constant pointer assumes that wherever it is pointing is a constant. Whether it really is a constant or not the pointer cannot be used to change the value of whatever is being pointed at. 
```commandline
*ptr1 = 123; //this is illegal
ptr1 = &y;  // this is ok 
```
### Adding integers to, and subtracting Integers from Pointers. 
- When an integer ```n``` is added to a pointer, the pointer will move on in memory ```n
data items of the type that pointer points to. 
```
int *iptr, ar[10]; 
iptr = &ar[4]; // iptr has address of ar[4]
iptr++; // iptr now points to ar[5]
iptr = &ar[6]-3; // iptr now points to ar[3]
```
### Subtracting pointers from pointers . 
- If two numbers of the same type are subtracted, then the result is the number of data items between the two addresses. 
```commandline
int *p1, *p2, ar[10], n;
p1 = &ar[3]
p2 = &ar[5]
n = p2-p1; // n = 2
```
** subtracting pointers from another type could lead to ```compiler error```**
- We can also use pointers to increment by one as 
```commandline
*iptr++;
*iptr--);
--(*iptr);
++(*iptr);
```
### Array names Used as Pointers
- An Array name when not followed by [] has the value of the address of the start of the array. 
```commandline
int *ip, ar[10];
ip = ar; //these two statements are
ip = &ar[10]; //equal
```
- The name of an array is a CONSTANT pointer, however, so it can be used on the left hand side of an assignment. 
```commandline
ar = ip; //this will give a compiler error
```
### Pointers used as Arrays
- As observerd before, ``` ip = ar ``` stores the address of the array first index, same way, we can use ip[4] to store 5th element into the arrays.
```commandline
ip[0] is equivalent to *ip and equivalent to ar[0]
ip[4] is equivalent to *(ip+4) and equivalent to ar[4]
```
##### Imp
## A POINTER SHOULD ALWAYS BE GIVEN A SUITABLE ADDRESS BEFORE IT IS USED 
- The Size of the pointer is ```4 bytes``` of any type, according to ANSI. And it may also depends on the platform like, on Cloud, super machine, etc. 
