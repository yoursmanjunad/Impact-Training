class Node:
    def __init__(self,num=0):
        self.data = num
        self.next = None
    # Here we are just created a class and created a method by which we create a node and insert value to it and to point to the next node, we default set it as None
class LinkedList():
    def __init__(self):
        self.head = None
        self.temp = 0
        self.__length = 0
    def appendNode(self, num=0):
        nn = Node(num)
        nn.data = int(input("Enter the data:"))
        if self.head == None:
            self.head = nn
        else:
            self.temp = self.head
            while (self.temp.next!=None):
                self.temp = self.temp.next
            self.temp.next = nn
    def printList(self):
        self.temp = self.head
        while self.temp!=None:
            print(self.temp.data,end="-->")
            self.temp = self.temp.next # For every Iteration we are moving to the next node
        print("None")
    # This Method allows us to append the Node at the Beginning of the List
    def addBeginning(self):
        nn = Node()
        nn.data = int(input("Enter the data you want to append at the beginning of the list: "))
        if self.head == None:
            self.head = nn
            self.__length+=1
        else:
            self.temp = self.head
            self.head = nn
            nn.next = self.temp
            self.__length+=1
            print("You've successfully appended the node at the beginning!")
    # This Method allows us to insert the Node at the Middle of the list using two pointer method!
    def addAtMid(self):
        nn = Node()
        nn.data = int(input("Enter the data you want to append at the Middle of the List: "))
        if self.head == None:
            self.head = nn
            self.__length+=1
        else:
            slow = self.head
            fast = self.head
            while (fast is not None):
                slow = slow.next
                fast = fast.next.next
            self.temp = slow.next
            slow.next = nn
            nn.next = self.temp
        print("You've successfully appended the Node at the Middle of the List")
    #This Method allows us to remove the Node at the Beginning.
    def remBeginning(self):
        if self.head == None:
            return
        else:
            self.head = self.head.next
            print("Successfully Deleted the First Node of the Linked List")
    # This Method allows us to remove the node at the Last
    def remLast(self):
        if self.head == None:
            return
        else:
            self.temp = self.head
            while self.temp.next.next!=None:
                self.temp = self.temp.next
            self.temp.next = None
            print("Successfully Deteted the Node at the Last of the Linked List")
    # This Method allows us to remove the node at middle of the Linked List
    def remMid(self):
        if self.head == None:
            return
        else:
            slow = self.head
            fast = self.head
            while fast is not None:
                slow = slow.next
                fast = fast.next.next
            self.temp = slow
            self.temp = self.temp.next.next
            print("You've successfully removed the Node at the Middle")
    # Removing the Node by value
    def remNodeVal(self):
        value = int(input("Enter the value that to be removed from the List"))
        if self.head.data == value:
            self.head = self.head.next
            return
        else:
            self.temp = self.head
            while self.temp.next.data != value:
                self.temp = self.temp.next
            self.temp.next = self.temp.next.next
    # This Method returns True if it has a Cycle else False
    # def detectCycle(self):
    #     if self.head == None:
    #         return "There's no List Itself"
    #     else:
    #         slow = self.head
    #         fast = self.head
    #         while slow !=fast:
    #             slow == slow.next
    #             fast = fast.next.next
    #             if fast is None:
    #                 return False
    #         return True
    # This method returns if the List is Palindrome or not
    # def isPalindrome(self):
    #     if self.head == None:
    #         return "Not having any List"
    #     else:
    #         val = ''
    #         self.temp = self.head
    #         while self.temp != None:
    #             val.join(self.temp.data)
    #             self.temp = self.temp.next
    #     return val == reversed(val)
    # Remove the Nth Node from the End of the List
    def remKthEnd(self):
        if self.head == None:
            return
        else:
            self.temp = self.head
            k = int(input("Enter the k-th Node to be removed:  "))
            upto = self.__length - k
            while upto == 1:
                self.temp = self.temp.next
                upto-=1
            self.temp.next = self.temp.next.next

# Creating object
LL = LinkedList()
nodes = int(input("Enter how many nodes you have to enter: "))
while nodes!=0:
    LL.appendNode()
    nodes-=1
print("You've created these nodes as")
# LL.printList()
# LL.addBeginning()
# LL.printList()
# LL.addAtMid()
# LL.printList()
# LL.remBeginning()
# LL.printList()
# LL.remMid()
# LL.printList()
# LL.remLast()
# LL.printList()
#LL.remNodeVal()
#LL.printList()
# print(LL.detectCycle())
LL.remKthEnd()
LL.printList()