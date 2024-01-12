s = []
Cap = 5
Top = 0
Bottom = 0
def pushStack(num):
    if Top == Cap:
        print("Stack Overflow")
        return #Prints if the stack is full and tries to push more elements
    s.append(num)
    Top+=1

