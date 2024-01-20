class Node:
    def __init__(self, num = 0):
        self.data = 0
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.temp = self.head
        self.__length = 0
    def createNode(self,num=0):
        nn = Node(num)
        nn.data = int(input("Enter the value "))
        if self.head==None:
            self.head = nn
            self.__length+=1
        else:
            self.temp = self.head
            while (self.temp.next!=None):
                self.temp = self.temp.next
            self.temp.next = nn
            self.__length += 1
    def printList(self):
        self.temp = self.head
        while self.temp!=None:
            print(self.temp.data, end=" -->")
            self.temp = self.temp.next
        print("None")
LL = LinkedList()
nodes = int(input("Enter the number of nodes: "))
while nodes!=0:
    LL.createNode()
    nodes-=1
print("You've created the List: ")
LL.printList()