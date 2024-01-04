#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int val;
    struct Node *ptr;
};

int main()
{
    struct Node n1, n2, n3, n4;
    struct Node *temp, *head;

    n1.val = 10;
    n1.ptr = NULL;
    n2.val = 20;
    n2.ptr = NULL;
    n3.val = 30;
    n3.ptr = NULL;
    n4.val = 40;
    n4.ptr = NULL;

    n1.ptr = &n2;
    n2.ptr = &n3;
    n3.ptr = &n4;

    head = &n1;
    temp = head;

    while (temp != NULL)
    {
        printf("%d->", temp->val);
        temp = temp->ptr;
    }
    printf("Null");
    return 0;
}
