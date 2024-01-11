#include <stdio.h>
#include <stdlib.h> //to ue malloc function
int main()
{
    int *ptr = NULL;
    ptr = (int *)malloc(3 * sizeof(int)); // This makes DMA (Dynamic Memory Allocation)
    printf("\n address of ptr = %u", &ptr);
    printf("\n ptr is pointing to %u\n", ptr);
    *(ptr + 0) = 10;
    *(ptr + 1) = 20;
    *(ptr + 2) = 30;
    printf("\n ptr is pointing to %u with the value %d\n", ptr, *(ptr + 0));
    printf("\n ptr is pointing to %u with the value %d\n", ptr, *(ptr + 1));
    printf("\n ptr is pointing to %u with the value %d\n", ptr, *(ptr + 2));
    // This allocates the memory with for the same var repeatedly,
    ptr[0] = 101;
    ptr[1] = 201;
    ptr[3] = 301;

    printf("\n ptr is pointing to %u with the value %d\n", ptr, ptr[0]);
    printf("\n ptr is pointing to %u with the value %d\n", ptr, ptr[1]);
    printf("\n ptr is pointing to %u with the value %d\n", ptr, ptr[2]);
    printf("Newwwwww");
    // This allocates the memory with 4 bytes
    *ptr = 10;
    *ptr = 30;
    *ptr = 20111;
    printf("\n ptr is pointing to %u with the value %d\n", &ptr[0], *ptr);
    printf("\n ptr is pointing to %u with the value %d\n", &ptr[1], *ptr);
    printf("\n ptr is pointing to %u with the value %d\n", &ptr[2], *ptr);
    return 0;
}