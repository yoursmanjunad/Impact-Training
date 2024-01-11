'''
Take 2 numbers as input and print the largest number.
'''
num1= int(input("Enter a number: "))
num2= int(input("Enter another number: "))
if num1>num2:
    print(num1 ," is greater than ", num2)
elif num1==num2:
    print("Both are same")
else:
    print(num2, ' is greater than ', num1)