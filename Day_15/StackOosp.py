class stackClass:

    def _init_(self, limit):
        self.Cap = limit
        self.S = []
        self.Top = 0
        self.Bottom = 0

    def push(self, val=0):
        if self.Top == self.Cap:
            return 'Stack is Full'
        self.S.append(val)
        self.Top += 1
        return f'Successfully Inserted {val}'

    def pop(self):

        if self.Top == self.Bottom:
            return 'Stack is empty'
        ret = self.S[self.Top]
        self.S.pop()

        return ret

    def printStack(self):
        for i in range(self.Top - 1, -1, -1):
            print(S[i])


if _name_ == '_main_':
    sobj = stackClass(3)
    print(sobj.push(6))
    print(sobj.push(3))
    print(sobj.push(3))
    print(sobj.push(6))
    print(sobj.pop())
