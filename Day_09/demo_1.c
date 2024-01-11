#include <stdio.h>
#include <stdlib.h>
typedef struct node
{
    int data;
    struct node *next;
    struct node *prev;
} node;

void dispFList(head);
void dispBList(head);

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
    n3.next = NULL;
    // Now created a relation between all nodes with next and prev address
    node *temp = head;
    printf("Null");
    while (temp != NULL)
    {
        printf("-<- %d ->", temp->data);
        temp = temp->next;
    }
    printf("Null");
    // Adding new Node between two nodes.
    node *temp_add = &n3;
    n2.next = &n4;
    n4.next = temp_add;
    n3.prev = &n4;
    n4.data = 40;
    temp = head;
    printf("\nAfter adding new node in between\n");
    printf("Null");
    while (temp != NULL)
    {
        printf("-<- %d ->", temp->data);
        temp = temp->next;
    }
    printf("Null\n");
    // Deleting a Node
    n2.next = &n3;
    n3.prev = &n2;
    temp = head;
    dispFList(head);
    printf("Backward list!\n");
    dispBList(head);
    return 0;
}

void dispFList(node *head)
{
    printf("Null");
    while (head != NULL)
    {
        printf("-<- %d ->", head->data);
        head = head->next;
    }
    printf("Null\n");
}
void dispBList(node *head)
{
    printf("Null");
    while (head->next != NULL)
    {
        head = head->next;
    }
    do
    {
        printf("-<- %d ->", head->data);
        head = head->prev;
    } while (head != NULL);

    printf("Null\n");
}
