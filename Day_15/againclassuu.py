from StackClass import *

stack = StackClass()
str = input()


def bP(str):
    if len(str) % 2 == 0 and str.startswith('(') and str.endswith(')'):

        for i in str:
            if i == '(':
                stack.pushStk(i)
            if i == ')':
                stack.popStk()

        if stack.Bottom == stack.Top:
            return 'pranthasis is correct'

    return 'Not Correct'


print(bP(str))

# from stackClass import *

# def bP(str1):
#   if len(str1)%2 != 0:
#     return False
#   if str1[0] == ")" or str1[len(str1)-1] == "(":
#     return False
#   for i in str1:
#     if i == "(":
#       s.push(i)
#     elif i==")":
#       s.pop()

#   return True