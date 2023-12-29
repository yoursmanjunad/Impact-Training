'''
Patterns File
We include multiple patterns question and output
1.
*****
*****
*****
*****
*****

2.
*****
****
***
**
*

3.
*
* *
* * *
* * * *
* * * * *

4.
*
*  *
*  *  *
*  *  *  *
*  *  *  *  *
*  *  *  *  *
*  *  *  *
*  *  *
*  *
*

5.
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5

6.
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5

7.
1
1 * 2
1 * 2 * 3
1 * 2 * 3 * 4
1 * 2 * 3 * 4 * 5
'''
# num = int(input("Enter a number: "))
def pattern1(num):
    for row in range(1,num+1):
        for col in range(1,num+1):
            print("* ",end=" ")
        print()
#pattern1(num)

def pattern2(num):
    for row in range(1,num+1):
        for col in range(row, num+1):
            print("* ", end=" ")
        print()
# pattern2(num)

def pattern3(num):
    for col in range(1, num + 1):
        print(col * "* ")

# pattern3(5)

def pattern4(num):
    for i in range(1, num + 1):
        print("*  " * i)
    for i in reversed(range(1, num+1)):
        print("*  " * i)
# pattern4(5)

def pattern5(num):
    for i in range(1, num+1):
        for j in range(1, num+1):
            print(i, end=" ")
        print()
# pattern5(num)

def pattern6(num):
    for i in range(1, num+1):
        for j in range(1, num+1):
            print(i, end=" ")
        print()
#pattern6(num)

def pattern7(num):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            if(i==1 or j == 1):
                print(j, end=" ")
            else:
                print("*",j, end=" ")
        print()
# pattern7(num)
num = 5
def pattern8(num):
    counter = 1
    for i in range(1, num + 1):
        for j in range(i):
            if j % 2 == 0:
                print(counter, end=" ")
            else:
                print("*", counter, end=" ")
            counter += 1
        print()
pattern8(num)

# for c in range(1,10):
#     print(c
