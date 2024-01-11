'''
Take in two numbers and an operator (+, -, *, /) and calculate the value. (Use if conditions)
'''
op = input("Enter your operator: +, -, *, / ")
num1 = int(input("Enter a number "))
num2 = int(input("Enter another number: "))
if op == '+':
    print(num1+num2)
elif op == '-':
    print(num1-num2)
elif op == '*':
    print(num1*num2)
elif op == '/':
    print(num1/num2)
else:
    print("Sorry, we are working on ", op, " operator")