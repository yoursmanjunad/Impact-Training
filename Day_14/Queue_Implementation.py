Q = []
Cap = 5
Rear = 0
Front = 0
def enqueEle(num):
    global Q
    global Rear
    if Rear == Cap:
        print("\nQueue is Full!")
        return
    Q.append(num)
    Rear+=1
def dequeue():
    global Rear
    global Front
    if Rear == Front:
        if (Rear==Cap):
            Front = 0
            Rear = 0
    print("\nQueue is Empty")
    print(f"\n{Q[Front]} is dequeued")
    Front+=1
def printQueue():
    if Front == Rear:
        print("\nQueue is Empty")
        return
    for i in range(Front,len(Q),1):
        print(Q[i], end=" ")
    Q.pop()
    # print(Q[Front:Rear+1])

if __name__=="__main__":
    enqueEle(10)
    enqueEle(20)
    enqueEle(30)
    enqueEle(40)
    enqueEle(50)
    printQueue()
    dequeue()
    enqueEle(60)
