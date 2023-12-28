'''
Python Program to print 

*
**
***
****
*****
****
***
**
*

- Rhombus5
'''
num = int(input("Enter the number of rows:"))
for i in range(1, num+1):
    print("*"*i)
for i in reversed(range(1, num)):
    print("*"*i)