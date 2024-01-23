# Non Linear Data Structures
- These Non Linear D.S used for hierarchial representation of data. 
### Trees
- Tree can be defied as an `acycylic`, `Undirected`and `Connected Graph`
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
- **Internal Nodes** -- These are the nodes which are excepted leaf nodes. 
- **Degree** --- A degree os a node is the number of children. Since lead node doesn't have children, its degree is 0. The degree of a node can be any whole number from 0 to N.
- ![Tree Terminology](https://th.bing.com/th/id/OIP.n3NJzfzNPkz52o-WwAo1VQAAAA?rs=1&pid=ImgDetMain)
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
![Traversing Tree](https://global-uploads.webflow.com/5d0dc87aac109e1ffdbe379c/60e18e09daeb6db6f4995305_-Vsv_RLYEukjbDMgKxKJpxTnA246o-X1OjUPkl5HvnSiR-dFU4w5qKNaUtw-rq8wD4vMTGxFKtjvKCt7Uthmidpl_ajqRpVqgAH57N1HTpQ5MGBE4HCvE0dq7gTeM4-JtFLkQShX.png)
### Bredth First Search
- We traverse in Tree using `BFS` in Level Order.
### Types of Binary Tree:
  - **Full Binary Tree** - If a Tree having every node has 0 or 2 nodes children. If having 1 child, it's not a full binary tree
  - `The number of Leaf nodes = number of internal nodes+1`
![FBT](https://image2.slideserve.com/4451147/full-binary-tree-l.jpg)
  - **Degenerate Tree** - Every internal node has one child, such trees are performed as Linked List.
![](https://www.win.tue.nl/~kbuchin/teaching/JBP030/notebooks/bst-height5.png)
  - **Skewed Binary Tree** - Same as Degenerated Tree in which either dominated by Left nodes or the Right nodes.
![SBT](https://www.gatevidyalay.com/wp-content/uploads/2018/07/Skewed-Binary-Tree-Example.png)
### Types of Binary Trees based on Completion of Levels
1. **Complete Binary Tree** - If all the levels are completely filled except possibly last level and the last level has all keys as left as possible. 
As complete binary tree is same like Full Binary tree but there are two major differences, are 
  - Every level except he last level must be completely filled
  - All the leaf elements must lean towards the left
  - The last leaf element might not have a right sibling, i.e a complete binary tree doesn't have to be full binary tree.
  - `The number of intternal nodes = n/2 n--> Total nnumber of Nodes`
  - Last level of a complete binary tree can have `1 to 2^h is the height of the tree`
  ![Complete Binary Tree](https://media.geeksforgeeks.org/wp-content/uploads/binary_tree-1.png)
2. **Perfect Binary Tree** - A binary tree is a perfect binary tree in which all the internal nodes have two children and all leaf nodes are at the same level. 
   - In this, every internal nodes has exactly two child nodes and all the leaf nodes are at the same level. 
   - In a perfect binary tree, **the number of leaf nodes is the number of internal nodes plus 1.**  
   - The number of leaf nodes = `(n+1)/2` where `n` is the total number of nodes. 
   - The total number of nodes `= s^h+1 -1` where h is the height of the tree. 
![Perfect Binary Tree](https://th.bing.com/th/id/OIP.8DEnOoZD9s4DPrACWRfcDAHaD4?rs=1&pid=ImgDetMain)
3. **Balanced Binary Tree** - A binary tree is balanced if the height os the tree is O(Log n) where `n` is the number of nodes
  - The difference between the height of the left and right subtree for each node is either 0 or 1. 
![Balanced Binarry Tree](https://www.thecrazyprogrammer.com/wp-content/uploads/2021/03/balanced_bst.png)
