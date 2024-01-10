#There is an array of n integers. There are also 2 disjoin sets A and B each containing n integers


#Sample input:
'''
 3 2
 1 5 3
 3 1
 5 7


 i/o - 1 total happiness
'''
#pandagram
happiness = 0
import  array as arr
nums = arr.array('i', [1,5,6])
set1 =  [3,1]
set2 = [5,7]
for i in range(0,len(nums)):
    if nums[i] in set1:
        happiness= happiness+1
    if nums[i] in set2:
        happiness= happiness-1
print(happiness)
#words with duplicate letters
str1 = "hello ardff"
for i in range(0,len(str1)):
    if str1[i].count(str1[i])>=1:
        print("Duplicate found")
        break