// Program to implement Linked List in C
#include <stdio.h>
struct node
{
    int val;
    struct node *ptr;
};

int main()
{
    // creating nodes
    struct node n1, n2, n3, n5;
    struct node *temp, *head;
    // assigning values to the nodes
    n1.val = 10;
    n1.ptr = NULL;
    n2.val = 20;
    n2.ptr = NULL;
    n3.val = 30;
    n3.ptr = NULL;
    // make a relationship by creating a link
    n1.ptr = &n2;
    n2.ptr = &n3; // Created a Linked List
    // Trasversing the list
    head = &n1;
    temp = head;
    // printf("%d->", temp->val);
    // temp = &n2; // or can be done using temp = n1.ptr;
    // printf("%d->", temp->val);
    // temp = &n3;
    // printf("%d->Null", temp->val);
    // while (temp != NULL)
    // {
    //     printf("%d->", temp->val);
    //     temp = temp->ptr;
    // }
    // printf("NULL");
    // printf("New node adding");
    struct node n4;
    n4.val = 25;
    n2.ptr = &n4;
    n4.ptr = &n3;
    while (temp != NULL)
    {
        printf("%d->", temp->val);
        temp = temp->ptr;
    }
    printf("NULL");

    // adding n5 at the beginning.  (new node)
    n5.ptr = &n1;
    n5.val = 01;
    // assign BA of earlier list to the new node
    // Now changing the head pointer to the new node, n5.
    head = &n5;
    temp = head;
    n2.ptr = n4.ptr;
    while (temp != NULL)
    {
        printf("%d->", temp->val);
        temp = temp->ptr;
    }
    // de referencing - deleting the node n3.
    printf("NULL");
    // deleting  2 node.

    return 0;
}
// void dispList(struct node *h)
// {
//     printf("\n List is ");
//     while (h)
//     {
//         printf("%d->", h->val);
//         h = h->ptr;
//     }
//     printf("NULL");
// }