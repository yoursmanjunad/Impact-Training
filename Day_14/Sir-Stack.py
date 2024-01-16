class StackClass:


    def __init__(self):
        self.S = []
        self.Cap = 20
        self.Top = 0
        self.Bottom = 0

    def pushStk(self, num):

        if self.Top == self.Cap:
            print("Stack is Full")
            return
        self.S.append(num)
        self.Top += 1

    def popStk(self):
        if self.Top == self.Bottom:
            print("Stack is Empty")
            return
        ret = self.S[self.Top-1]
        self.Top -= 1
        return ret

    def printList(self):
        if self.Top == self.Bottom:
            print("Stack is Empty")
            return
        for i in range(self.Top - 1, -1, -1):
            print(self.S[i])
print(__name__)
if __name__ == "__main__":
    S = StackClass()
    # print(S)
    # S.pushStk(10)
    # S.pushStk(20)
    # S.printList()
    # print(f"{S.popStk()} Element is popped out")
    # S.printList()
    str = input("Enter a string: ")
    for i in range(0, len(str)):
        S.pushStk(str[i])
    S.printList()