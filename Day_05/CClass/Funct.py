# Functions provides better modularity for your application and a high degree of code reusing.
# Based on the object python stores the value in the variable
#Internal working of function / python , why python allows us to use function without defining. Compare with C/Java
# does it occupy space when you declare a function. how memory management works for function?


def pName(str1,  num1, num2):
    print(str1)
    print(num1, num2)
    return "returning from the func"
# try running function with and without return in calling print function inside calling the function
#str1 = "Po ra puka..."
print(type(pName("Po ra puka...", [3,4,5],5)))

#prime number func
def isPrime(num):
    for i in range(2,int(num/2)):
        flag = False
        if num <= 1:
            return False
        if num % i != 0:
            flag = True
            break
    if flag == True:
        return False
    return True
n = int(input())
if isPrime(n) == False:
    print("It is not a Prime")
else:
    print("It is a Prime")
