#include <stdio.h>
#include <stdlib.h>

struct node
{
    int val;
    struct node *ptr;
};
typedef struct node NODE;

void dispList(NODE *);

int main()
{
    NODE *temp = NULL, *head = NULL;
    NODE *newNode;
    int choice = 1;

    while (choice)
    {
        newNode = (NODE *)malloc(sizeof(NODE));
        printf("\n Enter the new node value: ");
        scanf("%d", &(newNode->val));
        newNode->ptr = NULL;

        if (head == NULL)
        {
            // List is empty;
            head = newNode;
            temp = head;
        }
        else
        {
            temp->ptr = newNode;
            temp = temp->ptr;
        }

        printf("\n Do you want to create a new node (0/1): ");
        scanf("%d", &choice);
    }

    int search = 35;
    int count = 1;

    // Searching in the list.
    temp = head; // Reset temp to the beginning of the list
    while (temp != NULL && temp->val != search)
    {
        temp = temp->ptr;
        count += 1;
    }

    if (temp != NULL && temp->val == search)
    {
        printf("Found it in Node - %d", count);
    }
    else
    {
        printf("-1, %d not found in the list", search);
    }

    dispList(head);
    return 0;
}

void dispList(NODE *h)
{
    printf("\n List is ");
    while (h)
    {
        printf("%d->", h->val);
        h = h->ptr;
    }
    printf("NULL\n");
}
