class BinTree:
    def __init__(self, val=0):
        self.data = val
        self.left = None
        self.right =  None
    # def insert(self,val):
    #     if self.data is None:
    #         self.data = val This prints None
    def insert(self, val=0):
        if self.data == 0:
            self.data = val #This prints the data which we've given as argument in thee node creation function call.
        if self.data < val:
            if self.right is None:
                self.right = BinTree(val)
                return
            else:
                if self.right.insert(val):

bt = BinTree()
bt.insert(10)
print(bt.data)