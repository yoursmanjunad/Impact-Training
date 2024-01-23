# Non Linear Data Structures
- These Non Linear D.S used for hierarchial representation of data. 
### Trees
- Each node has two components - data and a link to its sub category. 
- Quicker and Easier access to the data
- Store hierarchial data, like folder structure, organization structure, XML/HTML Data
- There are many different types of data structure which performs better in various situations. 
- Types of Trees like -> `Binary Trees`, `AVL`, `Red Black Tree`
- Whenever a file or directory is created, a spearate code is generated and stored in the table. That code is directly converted to numerix including the `root` directory. 
- It is called `Inode Information`
- Whenever the new file or sub directory is created, it will be in the increasing order from the `Inode` code. 
- It will be stored in a `Tree` data structure mostly in `Binary Tree`
- That's why in Linux or Unix OS we get results for the search operations faster as compared to Windows. Because, `Windows` uses Linear Data structure for it.
### Tree Terminology
- **Root** --- It is on the first level `Head` node. (In LL terms)
- **Edge** --- Link between nodes called `Edge`
- **Leaf** --- Nodes which doesn't have a child called `Leaf`
- **Sibling** --- childrens of same parent called 'sibling'
- **Ancestor** --- parent,  grand parent or great grand parent of a `node`
- **Depth** --- Measured from Top to Bottom, whereas Top is the `Level 0` and the bottom is where the max depth of the tree.
- **Height** ---
- ![Tree Terminology](C:\Impact Training\Day_19\OIP.jpeg)
### Binary Trees
- It is a tree data structure in which each node can have at most two children. which are referred to as the left child and the right child. 
- Binary trees are used in situations like, data storage and retrival, expression evaluation, network routing and game AI.
- Can also be used to implement various algorithms such as `searching`, `sorting` and `Graph` Algorithms. 
- We can do operations as `Inserting`, `Removing`, `Searching`, `Deletion` of nodes and also `Traversing` of it. 
  - Other important operations like `Height`, `Level ` and `size ` of the entire tree. 
- And also used in `Storing cache in DB`,`Huffman Coding`, `Compilers`, `Excel`, `Priority Queues`, `Syntax Trees` for programming like **GCC** and **AOCL** platform arithmetic operations. 
- Fast Memory Allocation in computers, encoding and Decoding, 
- In trees, we traverse using algorithms like `DFS ` and `BFS`
###  Depth First Search
- Futher this algorithm is classified into three types -
1. PreOrder `( Current - left - right)`
2. InOrder `(left - current - right)`
3. Post Order `(left - right - current)`
![Traversing Tree](C:\Impact Training\Day_19\WhatsApp Image 2024-01-23 at 11.13.52_9628236e.jpg)
### Bredth First Search
- We traverse in Tree using `BFS` in Level Order.
### Types of Binary Tree:
  - **Full Binary Tree** - If a Tree having every node has 0 or 2 nodes children. If having 1 child, it's not a full binary tree
  - **Degenerate Tree** - Every internal node has one child, such trees are performed as Linked List. 
  - **Skewed Binary Tree** - Same as Degenerated Tree in which either dominated by Left nodes or the Right nodes.
### Types of Binary Trees based on Completion 
