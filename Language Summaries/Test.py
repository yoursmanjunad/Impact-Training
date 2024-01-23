# # x = [5,10,15,20]
# # print(x[:-1])
# # # print([(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y])
# # ls= [[1,2,3], [4,5,6], [7,8,9]]
# # ls[1].pop()
# # print(ls)
# ml = [1,2,[3,4,[5,6]],7]
# print(ml[2][2][1])
# import random
#
# ml = [1,2,3,4,5]
# random.shuffle(ml)
# print(ml)
ml = [x for x in range(10) if x%2==0]
print(ml)