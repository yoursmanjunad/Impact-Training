class Stack:
    def __init__(self):
        self.S = []
        self.Cap = 20
        self.Top = 0
        self.Bottom = 0

    def pushStack(self, num):
        if self.Top == self.Cap:
            print("Stack Overflow")
            return
        self.S.append(num)
        self.Top += 1

    def popStack(self):
        if self.Top == self.Bottom:
            print("Stack underflow")
            return
        print(f"{self.S[self.Top - 1]} is popped out")
        # To return the value of the removed -- ret =  print(f"{self.S[self.Top - 1]} is popped out")
        self.Top -= 1

    def printList(self):
        if self.Top == self.Bottom:
            print("Stack underflow")
            return
        for i in range(self.Top - 1, -1, -1):
            print(self.S[i],end="")
    def validParenthesis(self):
        for i in range(0,len(str)):
            if str[i]==')':
                my_stack.popStack()
        if my_stack.Top==my_stack.Bottom:
            return True
        return False

# Create an instance of the Stack class
if __name__ == "__main__":
    my_stack = Stack()
    # Use the instance to call methods
    # my_stack.pushStack(10)
    # my_stack.pushStack(20)
    # my_stack.pushStack(30)
    # my_stack.pushStack(40)
    # my_stack.pushStack(50)
    # my_stack.printList()
    # str = input("Enter a string: ")
    # for i in range(0, len(str)):
    #     my_stack.pushStack(str[i])
    # my_stack.printList()
    str = input("Enter a Parenthesis: ")
    if len(str)%2!=0 and str[0]==')' or str[len(str)-1]=='(':
        print("False")
    else:
        for i in range(0,len(str)):
            if str[i] == '(':
                my_stack.pushStack(str[i])
    my_stack.validParenthesis()


