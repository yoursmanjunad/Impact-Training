# Write a program to find the n-th number made of prime digits.
# Input - 10 should print the 10th number from 0 which both digits are prime
# Write Test cases, use multiple functions, try to run using Recursion

# num = int(input("Enter a number: "))
# function to increment the count value as we find two digits are prime.
# def isPrime(num):
#     flag = False
#     for i in range(2, int(num / 2)):
#         if num % i == 0:
#             flag = True
#             break
#     if flag == True:
#         return False
#     return True
# n = input()
# if n.isdigit() == True:
#     print("Contains digits only")
# isPrime(10)
# # print(num//10)
# # print(num%10)
#
# def getDigits(num):
#     for i in range(1,num+1):
#         fig = num%10
#         isPrime(dig)
#         flag+=1
#         num = num//10
# def isPrime(num):
#     flag =False
#     for i in range(2, num//2):
#         if(num% 2)==0:
#             flag = True
#             break
#         return flag
# def getDigits(num):
#     cDigitsPrime = 0
#     countDigits = 0
#     d = num%10
#     countDigits+=1
#     if isPrime(d) == False:
#         cDigitsPrime+=1
n=80
list = [2,3,5,7]
count = 4
for i in range (0,n+1):
    for j in range(0,4):
        if count==n:
            break
        list.append(list[i] * 10 + list[j])
        count+=1
print(list[n-1])