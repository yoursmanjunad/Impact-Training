### Write a program to read sum and product of digits in a given number
num = int(input("Enter a number: "))
# for i in range(0,num):
#     if(num == 0):
#         print(" Addition = 0", "Product = 0")
#     while(num == 0):
#         add = add + num%10
#         add = add/10

add = 0
while(num==0):
    add = add + num %10
    num = num / 10

print(add)