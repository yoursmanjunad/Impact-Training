#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int val;
    struct Node *ptr;
};

int main()
{
    struct Node n1, n2, n3, n4, n5;
    struct Node *temp, *head;

    n1.val = 10;
    n1.ptr = NULL;
    n2.val = 20;
    n2.ptr = NULL;
    n3.val = 30;
    n3.ptr = NULL;
    n4.val = 40;
    n4.ptr = NULL;
    n5.ptr = NULL;
    n5.val = 143;

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
    // adding node between two nodes
    n2.ptr = &n5;
    n5.ptr = &n3;
    temp = head;
    printf("After adding in between two nodes, the list is --- ");
    while (temp != NULL)
    {
        printf("%d->", temp->val);
        temp = temp->ptr;
    }
    // Adding at the beginning of the list.
    struct Node n6;
    n6.val = 5;
    n6.ptr = &n1;
    head = &n6;
    temp = head;
    printf("After adding new node at the beginning of the list. ");
    while (temp != NULL)
    {
        printf("%d->", temp->val);
        temp = temp->ptr;
    }
    printf("Null");
    // Inserting the values at the end of the list
    struct Node n7;
    n7.val = 90;
    n7.ptr = NULL;
    n5.ptr = &n7;
    temp = head;
    printf("After adding node at the  end\n");
    while (temp != NULL)
    {
        printf("%d->", temp->val);
        temp = temp->ptr;
    }
    printf("Null");
    // Removing at the End
    n5.ptr = NULL;
    temp = head;
    while (temp != NULL)
    {
        printf("%d->", temp->val);
        temp = temp->ptr;
    }
    // Removing at the middle
    n2.ptr = &n4;
    n3.ptr = NULL;
    temp = head;
    printf("After removing node in  between");
    while (temp != NULL)
    {
        printf("%d->", temp->val);
        temp = temp->ptr;
    }
    printf("\nNull");
    // Removing the node at the Beginning.
    head = &n1;
    temp = head;
    while (temp != NULL)
    {
        printf("%d->", temp->val);
        temp = temp->ptr;
    }
    printf("\nNull");
    // Adding the Node's accoding to the Node's value
    // temp = head;
    // printf("Enter a number: ");
    // int value = scanf("%d", value);
    // struct Node newNode;
    // newNode.val = value;
    // newNode.ptr = NULL;
    // if (temp->val < value && temp->ptr->val > value)
    // {
    //     temp->ptr = &newNode;
    //     newNode.ptr = temp->ptr;
    // }
    // // adding a node by value using Ascending value.
    // while (temp != NULL)
    // {
    //     printf("%d->", temp->val);
    //     temp = temp->ptr;
    // }

    return 0;
}
