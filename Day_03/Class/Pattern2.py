num = int(input("Enter a Number: "))
def pattern(num):
    for i in range(1,num+1):
        for j in range(1, i+1):
            if (i==1 or j == 1):
                print(j, end=" ")
            else:
                print("*", j, end=" ")
        print()


pattern(num)