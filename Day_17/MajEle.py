# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than n//2 times. You may assume that the majoity element always exists in the array.
list = [3,2,3]
maxList = []
for i in range(0,len(list)-1):
    if list[i] == list[i+1]:
        maxList[i] = list[i]
    print(maxList)
# count1 = 0
# l1 = list(set(list))
# l2 = []
# d1 = {}
# for i in l1:
#     l2.append(list.count(i))
#     d[i] = l2[count1]
#     count1+=13