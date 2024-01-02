# given an array of posituve integers, your task is to find the leaders in the array.
# An element is leader if it is greater than all the elements to its right side
# 6  7  4  3  5  2
# o/p 2  5  7
list = [6, 7, 4, 3, 5, 2]
anslist = []
for i in range(len(list) - 1, -1, -1): # This helps to iterate over data structure from the end
    if list[i] < list[i - 1]:
        anslist.append(list[i])
print(anslist)
# #Leetcode problem --
# import array as arr
# nums = arr.array('i',[-2,1,-3,4,-1,2,1,-5,4])
# ansNums = []
# for i in range(0,len(nums)):
#     sum = 0
#     for j in range(i+1,len(nums)):
#         sum+=nums[i]+nums[j]
#     ansNums.append(sum)
# print(ansNums)

# s = "abcabcbb"
# def func(s):
#     newStr = ""
#     for i in range(0,len(s)):
#         if newStr.a
