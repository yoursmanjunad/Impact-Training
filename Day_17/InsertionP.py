import array as arr
nums = arr.array('i',[5,4,3,1,2])
# def insertSort(nums):
#     for i in range(1,len(nums)):
#         key = nums[i]
#         j = i-1
#         while j>=0 and key<nums[j]:
#             nums[j+1] = nums[j]
#             j-=1
#         nums[j+1] = key
#     print(nums)
# insertSort(nums)
def maxDif(nums):
    maxDif = 0
    for i in range(0,len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] - nums[j] > maxDif:
                maxDif = nums[i] - nums[j]
    return maxDif
print(maxDif(nums))
