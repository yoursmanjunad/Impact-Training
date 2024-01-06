#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *next;
    struct Node *prev;
};
// WE SHOULD BE POINTING TO  THE NULL AFTER CREATING THE NEW NODE DIRECCTLY
typedef struct Node Node;
void dispFList(Node *head);
int main()
{
    printf("Doubly Linked List");

    Node *temp = NULL;
    Node *head = NULL;
    Node *newNode;

    int choice = 1;

    while (choice)
    {
        newNode = (Node *)malloc(sizeof(Node));

        if (newNode == NULL)
        {
            printf("Memory allocation failed.\n");
            return 1;
        }

        printf("\n Enter the new Node value: ");
        scanf("%d", &(newNode->data));

        if (head == NULL)
        {
            head = newNode;
            temp = head;
        }
        else
        {
            temp->next = newNode;
            newNode->prev = temp;
            temp = temp->next;
        }

        printf("\n Do you want to create a new node? (0/1): ");
        scanf("%d", &choice);
    }
    printf("You've Created this List -- ");
    dispFList(head);
    return 0;
}

void dispFList(Node *head)
{
    printf("Null");
    while (head != NULL)
    {
        printf("-<- %d ->", head->data);
        head = head->next;
    }
    printf("Null\n");
}