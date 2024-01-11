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