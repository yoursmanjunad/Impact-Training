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
    def deleteNode(self):
        self.temp = self.head
        val = int(input("Enter a value to be deleted: "))
        if self.__length == 1:
            if val == self.head.data:
                self.head = None
                return
        if self.head.data == val:
            self.head = self.head.next
            self.__length -= 1
        while(self.temp.data != val):
            self.temp = self.temp.next
        self.temp.next = self.temp.next.next
    def isPalindrome(self):
        upto=self.__length//2




if __name__ == "__main__":
    # n1 = Node(10)
    # n2 = Node(20)
    # n3 = Node(30)
    # n1.next = n2
    # n2.next = n3
    # print(n1, type(n1))
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
    print("Add LinkedList at the Beginning - ")
    # LL.addAtBeginning()
    # LL.printList()
    LL.deleteNode()
    LL.printList()
