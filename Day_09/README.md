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

# Circular Linked List

- There's noting big difference between Doubly and Circular. Only one single change is that `Last node will be poining to the first node instead of NULL`
-

- We can iterate over a list or an array in Negative values.
- Prepare a list from range 0 to 100, in first half for even values and for second half odd.
