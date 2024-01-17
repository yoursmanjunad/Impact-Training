class Node:
    def __init__(self,num=0):
        self.data = num
        self.next = None
    def printVal(self):
        return self.data
class LinkedList():
    def __init__(self):
        self.head = None
        self.temp =None
        self.__length = 0
    def appendNode(self,num=0):
        nn = Node(num)
        nn.data = int(input("Enter a value:"))
        if self.head == None:
            self.head = nn
            self.__length +=1
        else:
            self.temp = self.head
            while(self.temp.next!=None):
                self.temp = self.temp.next
            self.temp.next = nn
            self.__length+=1
    def printList(self):
        self.temp = self.head
        while(self.temp!=None):
            print(self.temp.data, end=" ->")
            self.temp = self.temp.next
        print("None")
    #Printed the list.
    # def LengthOfList(self):
    #     self.temp = self.head
    #     length = 0
    #     while(self.temp!=None):
    #         length+=1
    #         self.temp = self.temp.next
    #     return length
    def addAtBeginning(self,num=0):
        nn = Node(num)
        nn.data = int(input("Enter a value:"))
        if self.head == None:
            self.head = nn
        else:
            nn.next = self.head
            self.head = nn
    def getLength(self):
        return self.__length
    def AddAtEnd(self,num = 0):
        nn = Node(num)
        nn.data = int(input("Enter a  value: "))
        if self.head == None:
            print("No list Presents")
            self.addAtBeginning()
        else:
            self.temp = self.head
            while(self.temp.next!=None):
                while (self.temp.next != None):
                    self.temp = self.temp.next
                    self.temp.next = nn
                    self.__length += 1

    # #Adding the Node in the mid
    # def deleteNode(self):
    #     self.temp = self.head
    #     val = int(input("Enter a value to be deleted: "))
    #     if self.__length == 1:
    #         if val == self.head.data:
    #             self.head = None
    #             return
    #     if self.head.data == val:
    #         self.head = self.head.next
    #         self.__length -= 1
    #     while(self.temp.data != val):
    #         self.temp = self.temp.next
    #     self.temp.next = self.temp.next.next
    def delKeyNode(self):
        val = int(input("Enter a value to be deleted: "))
        if self.head == None:
            return "List is Empty"
        if self.head.next == None:
            if val == self.head.data:
                self.head.next = None
                return
            else:
                return "Not Found"
        # Checking ig only one element is present in the lisst and if it is the val and may not
        if self.head.data == val:
            self.head = self.head.next
        self.temp = self.head
        slower = self.temp.next
        faster = self.temp.next.next
        while slower.next!=None:
            if slower.data == val:
                self.temp.next = faster
            self.temp = self.temp.next
            slower = slower.next
            faster = faster.next
        return
    # Not able to remove the last element if it is == val.


    def DelPos(self):
        pos = int(input("Enter the position to be removed: "))
        if pos == 1:
            self.head = self.head.next
            return
        #If the position is 1, it jusst points the head just points to the next of it.
        self.temp = self.head
        i = 2
        faster = self.head
        while (i != pos - 1):
            self.temp = self.temp.next
            faster = faster.next
            i+=1
        self.temp.next = faster
        return
    # Reverse LinkedList - II
    #Remove duplicates from the sorted linked list.
    def remDupli(self):
        self.temp = self.head
        while(self.temp!=None and self.temp.next!=None):
            if self.temp.data == self.temp.next.data:
                self.temp.next = self.temp.next.next
            self.temp = self.temp.next
        return
    def remDupII(self):
        slow = self.head
        fast = slow.next
        superFast = fast.next
        while(superFast!=None):
            if fast.data == superFast.data:
                while(superFast.next.data!=fast.data):
                    superFast = superFast.next
                slow.next = superFast.next
        slow = self.temp
        fast = slow.next
        superFast = superFast.next
        return
    # Removing duplicate elements from the list - Leetcode 82

if __name__ == "__main__":
    # n1 = Node(10)
    # n2 = Node(20)
    # n3 = Node(30)
    # n1.next = n2
    # n2.next = n3
    # print(n1, type(n1)
    # print(n1.printVal())
    # print(n2.printVal())
    # print(n3.printVal())
    # print(n1.printAll())
    LL = LinkedList()
    size = int(input("Enter the Number of Nodes:"))
    while(size!=0):
        LL.appendNode()
        size-=1
    LL.printList()
    #LL.remDupli()    # LL.remDupII()
    # LL.printList()
    LL.DelPos()
    LL.printList()
