'''
Program to print the sum  of a given number is a several combination from 1 to 4
'''
count = 0
num = int(input("Enter the number:"))
for i in range(1, num+1):
    for j in range(i,num+2):
        for k in range(j, num+1):
            for l in range(k,num+1):
                if(i+j+k+l==num):
                    print(i,j,k,l)
                    count+=1
print(count, "combinations are possible")