# Doubly Linked List

- In previous one, we've just inserted the values into the list by pointing to the next address.
- It doesn't know about the previous node's value and address. So, this drawback be solved in doubly linked list.
- Doubly linked list contains three values,

  - Data,
  - Next node address
  - Previous.

- In singly Linked List, we have a Node pointing to the NULL is known as End.
- But, the in Doubly, we have pointing **Head** to the `Null` as previous.

```
typedef struct Node{
    int val;
    struct node *right;
    struct node *left;
}Node;
//In main function
Node n1,n2,n3;
```

- This is how we create a **Doubly Linked** List in C
- **Typedef** is used to give a new name to the existing data type.
