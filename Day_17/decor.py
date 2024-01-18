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