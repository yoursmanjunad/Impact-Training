def testFun(l):
    print(l)
    l.append(5)
    print("List within Functions",l)
    return
list = [1,2,3,4]
testFun(list)
print("List outside the functions", list)
def printstr(str1="Moye Moye", val1=23):
    print(str1, val1, "2")
    return
def printstr(str1, val1):
    print(str1, val1, "1")
    return

# def printstr(str1="Moye Moye", val1=23):
#     print(str1, val1, "2(")
#     return
printstr("Bhupendra Jogi", 1) #When you  call a function with a pre-defined sstring as argument it will be passed to the function as parameter to the function
#If you have not given any value, it prints the string which given in the parameters for the function
# Why it is happening?? Assignment! 01/01/2024

#It takes the recent function to execute, from the input
#Even changing the position of argument, that works in python of the same datatype

# variable length arguments
# You may need to process a function for more arguments than you specified while defining the function, it is called aas vaeiable length arguments

def printStr(arg1, *vars):
    print("vars length - ", len(vars))
    print("arg1: ", arg1)
    for i in vars:
        print(i, end=" ")
    return

printStr(1,2,3,4,5)

#
# random={"red","black","blue"}
# print(random)