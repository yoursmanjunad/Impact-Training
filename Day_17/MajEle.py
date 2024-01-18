# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than n//2 times. You may assume that the majoity element always exists in the array.
list = [3,2,3]
maxList = []
for i in range(0,len(list)-1):
    if list[i] == list[i+1]:
        maxList[i] = list[i]
    print(maxList)