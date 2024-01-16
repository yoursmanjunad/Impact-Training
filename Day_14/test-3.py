# import test_1 as T
# T.func1()
# # If we call the function without using referene `T` it throws Name Error
# list = ["McDownels Murty", "Jalebi", "Lavangam", "Miriyam", "Miriyam", "Pedda Reddy"]
# #used = set(list)
# print(set(list))
# from array import *
# arr = array('i',[1,2,3,4,5])
# arr2 = array('i',[9,7,5,6])
# # arr.extend(arr2)
# # print(arr)
# list = [99,87,78,84]
# arr.fromlist(list)
# print(arr)
# print(arr.pop())
# print(arr.remove(1))
# print(arr.count(2))
# print(arr.index(4))
listd = [1,2,3,4,5,6,7,8,9,10]
evens = list(filter(lambda n : n%2==0,listd))
print(evens)
# cook your dish here
num1 , num2 = map(int, input().split())
print(num1*num2)