# # def printMe():
# #     print("Majito ki rubi ")
# # m1 = printMe
# # print(m1)
# # m1()
# def outer_fun(inner_fun):
#     print("Chipi chipi chapa chapa")
#     # def inner_fun():
#     #     print("Dubi Dubi Daba Daba")
#     # inner_fun()
#     def i
#     print("Boom boom boom boom")
# @outer_fun
# def printMe1():
#     print("Bakchodi mtkr lowde")

def outer_func(func):
    print("Entering Outer function")
    def inner_func():
        print("Entering inner func")
        func()
        print("Exiting outer func")
    print("Exiting Outer Function")
    return inner_func()
@outer_func
def print_Me():
    print("Helloooooo")
def calc(v1,v2):
    print("Welcome to the Calculator")
    def add_Fun(num1,num2):
        print("The summation is ", num1+num2)
    add_Fun(v1,v2)
    def sub_fun(num1,num2):
        print("Difference is ", num1-num2)
    sub_fun(v1,v2)
    def multi_fun(num1, num2):
        print("Product is ", num1*num2)
    multi_fun(v1,v2)
    def div_Fun(num1, num2):
        if num2>0:
            print("Division is ",num1//num2)
    div_Fun(v1,v2)
    print("Exiting the calculator")
print(calc(2,3))
# num = 1,2,3
# store = []
# for i in num:
#     store.append(lambda: print(i,end=" "))
# for p in store:
#     p()
# text = 'A', 'B', 'C'
# lst = []
# for t in text:
#     lst.append(lambda t = t: t)
# for l in range(len(lst)):
#     print(lst[l](),end=' ')
# def outer(x,y):
#     print(x,y,end=' ')
#     def inner(p):
#         p()
#     return inner()
# def fun(x=50):
#     print(50)
# outer()
# def fun1(x):
#     return fun1(x+'1')
# print(fun1(fun1('10')))
f5 = 10
# def fun6(f5 = f5):
#     print(f5)
# f5 = 30
# fun6()
# def fun7(f7=dict()):
#     print(f7)
# fun7(1)
# def fun4(a,c,b=5):
#     return a,b,c
# print(fun4(10,20,30))
# def fun(*,x,y):
#     return x,y
# print(fun(10,y=20)[0])