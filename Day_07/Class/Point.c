#include <stdio.h>
int main()
{
    int a = 10;
    int *ptr;
    ptr = &a;
    printf("Address of a = %d \n", &a);           // &a is address of a
    printf("Address of ptr = %d \n", &ptr);       // ptr is a variable that stores address of a
    printf("Contents of a = %d \n", ptr);         // ptr = &a
    printf("Value of a using ptr = %d \n", *ptr); // *ptr = *(&a) = a Here * is called dereferencing operator
}