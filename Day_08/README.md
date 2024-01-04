## Linked-List
- ```Self Referencial Pointer```, because it is a pointer which points to it's own type. Without having a reference name, it would be difficult. That's why to delcare the structure in a structrue (self), we need to name it first. 
- In Linked List, each node has two blocks, one is for storing the value in it and another one is used to store the address of next node.(pointer)
- To get the value or to perform any action in the next node, we should be knowing it's address, so that I can perform any action.
- These nodes in memory are allocated in Dynamically. To know the next node, we store it's address in the current node as pointer, so we can reach there. Else, we can't access.
- If we stop adding new nodes, the last node will be pointing to the ```Null``` where it doesn't point to address of a node.
- [ ] How to design a class using **SOLID** principles
-  