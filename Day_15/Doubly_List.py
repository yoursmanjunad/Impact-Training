class Node:
    def __init__(self,num=0):
        self.data = num
        self.next = None
        self.prev = None
        self.__length=0
    def printVal(self):
        return self.data
class DLinked:
    def __init__(self):
        self.head = None
        self.temp = None
        self.__length = 0
    def insertData(self,num=0):
        nn = Node(num)
        nn.data = int(input("Enter a Value to the Node: "))
        if self.head == None:
            self.head = nn
            self.temp = self.head
            self.__length+=1
        else:
            while(self.temp.next!=None):
                self.temp = self.temp.next
            self.temp.next = nn
            nn.prev = self.temp
            self.__length += 1
    def printList(self):
        self.temp = self.head
        while(self.temp!=None):
            print(self.temp.data, end=" <->")
            self.temp = self.temp.next
        print("None")
    #Printed List
    def printRev(self):
        print("Backward Printing")
        self.temp = self.head
        while(self.temp.next!=None):
            self.temp = self.temp.next
        while(self.temp!=None):
            print(self.temp.data)
            self.temp = self.temp.prev
    # Done with Reverse printing
    def addBeginnig(self,num=0):
        nn = Node(num)
        nn.data = int(input("Enter the value to be inserted at beginning"))
        if self.head == None:
            print("List is empty, created one!")
            self.head = nn
            self.temp = self.head
        else:
            self.head.prev = nn
            nn.next = self.head
            self.head = nn
    # Add node at the beginning
    def deleteNode(self):
        if self.head == None:
            return "List is Empty"
        else:
            val = int(input("Enter a value"))
            self.temp = self.head
            while(self.temp.next.data != val):
                self.temp = self.temp.next
            if __name__ == '__main__':
                self.temp.next= self.temp.next.next

if __name__=="__main__":
    DLL = DLinked()
    DLL.insertData()
    DLL.insertData()
    DLL.insertData()
    DLL.insertData()
    DLL.printList()
    DLL.addBeginnig()
    DLL.printList()
    DLL.deleteNode()
    DLL.printList()
