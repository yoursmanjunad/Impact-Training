## Linked-List
- ```Self Referencial Pointer```, because it is a pointer which points to it's own type. Without having a reference name, it would be difficult. That's why to delcare the structure in a structrue (self), we need to name it first. 
- In Linked List, each node has two blocks, one is for storing the value in it and another one is used to store the address of next node.(pointer)
- To get the value or to perform any action in the next node, we should be knowing it's address, so that I can perform any action.
- These nodes in memory are allocated in Dynamically. To know the next node, we store it's address in the current node as pointer, so we can reach there. Else, we can't access.
- If we stop adding new nodes, the last node will be pointing to the ```Null``` where it doesn't point to address of a node.
- [ ] How to design a class using **SOLID** principles 
- **We need to give a semi-colon at the end of the structure because, to let compiler know that whole struct be treated as a One line. Generally, we close the line with the semi-colon, as the struct could be in multi-line, to avoid confusion for the compiler, we use semi-colon at the end of declaring the structure**
- Head will always be pointing to the ```base address``` of the list. 
- In LinkedList, we can **Add, delete, traverse** in the list. 
## To do
- [x] Create a Linked List in C, Java 
- [x] Insert Values in it
- [x] Insert in between two nodes
- [x] Insert at the beginning
- [x] Insert at the End
- [x] Remove at the End
- [x] Remove between nodes
- [x] Remove at the Beginning
- [ ] Add by value in Ascending order
- [ ] Remove by value input
- [ ] Traverse and print the size
- [ ] Traverse and print the List 
- [ ] Take input and update the list with Node number, and Node value
- [ ] Search in the list, if it is present, return True, else false Node value or -1
- [ ] Search a value, if it is present in  the list, then add a new node into it and print the list, else return false. 
- [ ] Sort the List in a Ascending Order 
- [ ] Sort the List with Node Exchange. 
- Return value of ```printf``` is Integer
- ```printf(%d (printf("Hello"))``` It will return the length of the strings
- Returning the successfully scanned items ```scanf("%d%d%d",&a,&b,&c);``` It prints the successfully scanned elements
```commandline
int a = 3;
float b = 3.0
```
**These both are equal** if b = 3.1 or any other, it is false, but as the .0 is equal to a then it is ```true```.
```commandline
#include <stdio.h>
int main()
{
    int a[5] = {5, 1, 15, 20, 25};
    int i, j, m;
    i = ++a[1];
    j = a[1]++;
    m = a[i++];
    printf("%d,%d,%d", i, j, m);
    return 0;
}
```
**What could be the output of the code?**
###  Tata Ninja Question - 1 

Problem:

A washing machine uses a fuzzy system to determine washing time and water level based on the weight of clothes it senses. Here are the fuzzy rules:

Low water level: Estimated time is 25 minutes for clothes weighing between 0 and 2000 grams (approximately).
Medium water level: Estimated time is 35 minutes for clothes weighing between 2001 and 4000 grams (approximately).
High water level: Estimated time is 45 minutes for clothes weighing above 4000 grams (approximately).
Zero weight: Estimated time is 0 minutes.

### Tata Ninja Question - 2
