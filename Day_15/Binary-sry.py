# This is just a dry run for the algorithm - Binary Search
import array as arr
nums = arr.array('i',[4,3,7,4,8,0,3,6,2,84])
target = int(input("Enter a number that you want to search! : "))
# sorted(nums)
# def binarySearch(nums, target):
#     half = len(nums)//2
#     if nums[half] == target:
#         return half
#     else:
#         if target>nums[half]:
#             for i in range(half,len(nums)):
#                 if nums[i] == target:
#                     return i
#         else:
#             for i in range(0,half):
#                 if nums[i] == target:
#                     return i
#     return -1
# print(binarySearch(nums,target))
# implementaation for Unsorted Array Binary Search!
def NotSortedSearch(nums, target):
    half = len(nums)//2
    if nums[half] == target:
        return half
    else:
        for i in range(half,len(nums)):
             if nums[i] == target:
                 return i
        for i in range(0,half):
            if nums[i] == target:
                return i
    return -1
print(NotSortedSearch(nums,target))
# Implementation using Recursion


