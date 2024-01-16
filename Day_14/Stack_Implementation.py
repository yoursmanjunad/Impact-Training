s = []
Cap = 20
Top = 0
Bottom = 0
def pushStack(num):
    global Top
    global s
    if Top == Cap:
        print("Stack Overflow")
        return #Prints if the stack is full and tries to push more elements
    s.append(num)
    Top+=1
def popStack():
    global s
    global Top
    if Top == Bottom:
        print("Stack underflow")
        return
    print(f"{s[Top-1]} is popped out")
    Top-=1

def printList():
    if Top == Bottom:
        print("Stack underflow")
        return
    for i in range(Top-1,-1,-1):
        print(s[i])

if __name__=="__main__":
    pushStack(10)
    pushStack(20)
    pushStack(30)
    pushStack(40)
    pushStack(50)
    pushStack(60)
    printList()
    popStack()
    printList()
    popStack()
    printList()
    popStack()
    popStack()
    popStack()
    popStack()

