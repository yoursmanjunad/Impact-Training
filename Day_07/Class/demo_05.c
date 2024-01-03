#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *ptr = NULL, *temp = NULL;
    ptr = (int *)malloc(3 * sizeof(int)); // This makes DMA (Dynamic Memory Allocation)
    // Check if memory allocation is successful
    printf("\n address of ptr = %u", &ptr);
    printf("\n ptr is pointing to %u\n", ptr);
    *ptr = 10;
    ptr++;
    *ptr = 20;
    ptr++;
    *ptr = 30;
    temp = ptr; // Store the current value of ptr in temp
    ptr--;      // Move ptr back to the beginning
    printf("\n ptr is pointing to %u with the value %d\n", &ptr[0], *ptr);
    ptr++;
    printf("\n ptr is pointing to %u with the value %d\n", &ptr[1], *ptr);
    ptr++;
    printf("\n ptr is pointing to %u with the value %d\n", &ptr[2], *ptr);
    return 0; // Indicate successful completion
}
