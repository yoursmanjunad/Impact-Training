num = int(input("Enter a number: "))
for i in range(0,num):
    for j in range(0,num):
        if i == 0 or i == num-1:
            print("# ", end="")
        else:
            if j == 0 or i == num-1:
                print("# ", end='')
    print()
