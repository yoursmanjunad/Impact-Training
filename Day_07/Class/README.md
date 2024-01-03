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