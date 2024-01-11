#include <stdio.h>
int main()
{
    int *ptr;
    *ptr = 10;
    printf("%d", *ptr); // it generates run time error
    return 0;
}