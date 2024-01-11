#include <stdio.h>
int main()
{
    int arr[] = {0, 2, 1, 0, 2, 1};
     for (int i = 0; i < sizeof(arr) / sizeof(arr[0]); i++) {
        for (int j = i + 1; j < sizeof(arr) / sizeof(arr[0]); j++) {
            if (arr[i] > arr[j]) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    printf("I think, we sorted it!");
    for (int i = 0; i < sizeof(arr); i++)
    {
        printf("%d", arr[i]);
    }

    return 0;
}