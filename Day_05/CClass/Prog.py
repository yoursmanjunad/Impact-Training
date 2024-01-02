## Program  to print the sum and product of the digits for a given number
num = int(input("Enter a number: "))
def cal(n):
    add = 0
    prod = 1
    while (n != 0):
        last = n % 10
        add = add + last
        if (last != 0):
            prod = prod * last
        n = n // 10
    print("Sum and Multiplication of digits in ", n ," is ", add," and ", prod)
if num == 0:
    print("Summation and Product is", 0)
else:
    cal(num)