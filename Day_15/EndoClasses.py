class A:
    def __init__(self):
        self.a = 101


class B:
    def __init__(self):
        self.b = 102
        self.__manipulateB()

    def printB(self):
        self.__manipulateB()
        print(self.b)

    def __manipulateB(self):
        self.b = self.b ** 3


objB = B()
# objB.b = 201
# objB.manipulateB()
objB.printB()