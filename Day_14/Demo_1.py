# print(dir())
# num = 10
# print(dir())
# n = 1223
# def fun():
#     global n#If we comment it, python searches for the same variable within the program out of scope and prinits it's value
#     print("Inside the function, we have ", n)
#     n = n+23
#     print(n)
# fun()

#
num = 201
def outerFun():
    num = 300
    def innerFunc():
        #num = 500
        print(num)
    innerFunc()
    print(num)
print("Global: ", num)
outerFun()