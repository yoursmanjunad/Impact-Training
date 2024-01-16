class Node:
    def __init__(self,num=0):
        self.data = num
        self.next = None
    def printVal(self):
        return self.data
class StackLinked:
    def __init__(self):
        self.head = None
        self.temp = None
        self.__length = 0
    def stackPush(self, num=0):
        nn = Node(num)
        nn.data = int(input("Enter the data: "))
        self.temp = self.head
        self.temp = self.head
        if self.head == None:
            self.head = nn
            self.__length +=1
        while (self.temp.next != None):
            self.temp = self.temp.next
        self.temp.next = nn
    def popStack(self):
        if self.head == None:
            return "Stack Overflow"
        else:
            self.temp = self.head
            while(self.temp.next!=None):
                self.temp = self.temp.next
            self.temp.next = None
    def printStack(self):
        self.temp = self.head
        while (self.temp!=None):
            print(self.temp.data)
            self.temp = self.temp.next
if __name__ == "__main__":
    LLS = StackLinked()
    LLS.stackPush()
    LLS.stackPush()
    LLS.stackPush()
    LLS.popStack()
    LLS.printStack()

