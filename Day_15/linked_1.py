class Check:
    S = [1,2,3]
    def __init__(self):
        Check.List = [4,5,6]
class test(Check):
    def __init__(self):
        self.a = 10
    def priintVals(self):
        print(f"{self.S}")

obj1 = test()