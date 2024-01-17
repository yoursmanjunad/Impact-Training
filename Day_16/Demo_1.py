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
    def DelNode(self):
        #Code to delete a node accodring to the position.
    def DelPos(self):
        pos = int(input("Enter the position to be removed: "))
        self.temp = self.head
        i=1
        while(i!=pos-1):
            self.temp = self.temp.next
        self.temp.next = self.temp.next.next

if __name__=="__main__":
    LL = LinkedList()