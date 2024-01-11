# from array import *
# my_arr = array('i',[1,2,3,4,5])
# print(my_arr)
# print((type(my_arr[0])))
# my_arr.append(6)
# print(my_arr)
# my_arr.insert(0,44)
# print(my_arr)
# my_extended_arr = array('i',[7,8,9])
# my_arr.extend(my_extended_arr)
# print(my_arr)
# c = [1232,234,23,]
# my_arr.fromlist(c[::-1])
# print(my_arr)
# print((my_arr.pop()))
# my_arr = [14] * 10
# print(my_arr)
# squares = [x**x for x in (1,2,3,4)]
# print(squares)
# str1 = "apple"
# l2 = [x for x in str1 if x in "aeiou"]
# print(l2)
#
# l3 = [1,5,2,3,101,100,88,65]
# l4 = [res for res in l3 if res%2==0 ]
# print(l4)
# # Program to print a list in first half contains even and second half contains odd.
# list = [ans for ans in range(0,100) if ans%2==0]+([ans2 for ans2 in range(0,100) if ans2%2!=0])
# print(list)
# list3 = [1,5,2,3,101,100,88]
# # listChar = ['even' for ans in list3 if ans%2==0]
# # listChar2 = ['odd' for ans in list3 if ans%2!=0]
# # print(listChar+listChar2)
# listChar = ['odd' if x%2!=0 else 'even' for x in list3]
# print(listChar)
# # Odd multiply by 3 Even multiply by 5
# listMulti = [res *3 if res%2!=0 else res*5 for res in list3]
# print(listMulti)
# str1 = "Hello"
# str2 = "WORLD"
# # USing lambda to print qube of a list
# powerMe = lambda x:x**3
# for i in  range (1,11):
#     print(powerMe(i), end=" ")
# #
# # for item in zip[1,2,3], ['Sugar,' 'Spice','everything', 'cost']:
# #     print(item)
# for x,y in zip(l3,l4):
#     print(x,y)
# for x,y in zip(l2,l3):
#     print(x,y,powerMe(x,y))
# l1 = [" foo", 'BAR', "BaZ"]
# l2 = list(map(lambda  s:s.strip().upper(),l1))
# print(l2)
# fi1 = [2, 3, 4]
# fi2 = [3, 2, 1]
#
# fi3 = list(map(lambda x, y: x**y, fi1, fi2))
# print(fi3)
#
list = [1,2,3,4]

list2 = [4,3,2,1]
list3 = [5,6,7,8]
list3.reverse()
print(list.sort())
lsit3 = list2.sorte