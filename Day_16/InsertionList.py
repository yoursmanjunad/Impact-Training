#Insertion Sort Algorithm
import array as arr
nums = arr.array('i',[5,4,3,1,2])
def insertionSort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[i]<nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                break
insertionSort(nums)
print(nums)