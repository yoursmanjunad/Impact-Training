# Given an unsorted arraay of a size of N of non negative integers,
#find a continous sub array which adds to given number sum
#Input format:
# THE first line contains an integer, denoting the size of the array
# the second line contains integers denoting elements of the array
# arr = [1.4.0,0,3,10,5]
# sum = 7
import array as arr
nums = arr.array('i',[1,4,0,0,3,10,5])
sum = 7
count = 0
for i in range(0,len(nums)):
    for j in range(i,len(nums)):
        if nums[i]+nums[j] == sum:
            print(i,j)

