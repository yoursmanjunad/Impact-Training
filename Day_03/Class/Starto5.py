'''
Program to print
1 * 2 * 3 * 4 * 5
6 * 7 * 8 * 9 * 10
11 * 12 * 13 * 14 * 15
16 * 17 * 18 * 19 * 20
21 * 22 * 23 * 24 * 25
'''
num = 25
for i in range(1, num+1):
    if(i%5==0):
        print(i)
    else:
        print(i,"*", end=" ")