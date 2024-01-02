# rotate the element of the list every h-th element
#output - 3 2 1 4 5 6 7 8 9 1
# 3 2 1 6 5 4 9 8 7 10
k = 3
n = 10

list = [1,2,3,4,5,6,7,8,9,10]
# count = 0
#
# for i in list:
#     if i%3 == 0:
#         for j in range(count,k):
#             list.reverse()
#             count+=1
# print

def fun(num):
    return num*2

l = [1,2,3,4]
l1 = []
for i in l:
    t = fun(i)
    l1.append(t)
print(l1)


#
# end = len(list)
# end-=1
# mid = (0 + end) //2
# for i in range (0,mid):
#     if i//3==0:
#         if i < mid and i<end:
#             t = list[i]
#             list[i] = list[end-1]
#             list[end-1] = t
#             end-=1
# # list.reverse()
# print(list)