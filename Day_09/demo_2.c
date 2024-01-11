#include <stdio.h>
#include <stdlib.h>
typedef struct node
{
    int data;
    struct node *next;
    struct node *prev;
} node;

void printList(head);

int main()
{
    node n1, n2, n3, n4;
    node *head = &n1;
    n1.data = 10;
    n1.prev = NULL;
    n1.next = NULL;
    n2.data = 20;
    n2.prev = NULL;
    n2.next = NULL;
    n3.data = 30;
    n3.prev = NULL;
    n3.next = NULL;
    // Added data and assigned values to it. Currently they are pointing to Null, in prev and next,
    // Making relationship between them...
    n1.prev = NULL;
    n1.next = &n2;
    n2.prev = &n1;
    n2.next = &n3;
    n3.prev = &n2;
    n3.next = &n1;
    // Now created a relation between all nodes with next and prev address
    return 0;
}
/* Function to traverse a given Circular linked list and print nodes */
void printList(struct Node *first)
{
    struct Node *temp = first;

    // If linked list is not empty
    if (first != NULL)
    {
        // Keep printing nodes till we reach the first node again
        do
        {
            printf("%d ", temp->data);
            temp = temp->next;
        } while (temp != first);
    }
}
