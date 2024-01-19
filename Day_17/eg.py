# def fun2(x):
#     return 'Inside Function'
# help(fun2)
# x = 20
# def fun4():
#     def fun5():
#         nonlocal x
#         x = 20
#         return x
#     return fun5()
# print(fun4())
# def fun(n,temp):
#     if (n==0):
#         return temp
#     temp = (temp*10)+(n%10)
#     return fun(n//10,temp)
# fun(1234,0)
# def fun(num):
#     if num<2:
#         return False
#     for i in range(2,int(num**0.5)+1):
#         if num%1==0:
#             return False
#     return True
# fun(9)
# def isEven(n):
#     if n==0:
#         return True
#     else:
#         return not isEven(n-1)
# isEven(5)
# def fun(x,y):
#     if x==0:
#         return y
#     return fun(x-1,x+y)
# print(fun(4,3))
# def fun(a,b):
#     if(b==0):
#         return a
#     else:
#         return fun(b,a%b)
# print(fun(24,25))
# def f(s):
#     if len(s)<=1:
#         return True
#     else:
#         return s[0]==s[-1] and f(s[1:-1])
# print(f("ADA"))d

# def fun(x,n):
#     if n==0:
#         return 1
#     else:
#         return x*fun(x,n-1)
# print(fun(2,3))
def s(n):
    if (n==0):
        return n
    else: return n+s(n-1)
print(s(8))