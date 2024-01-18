#Insertion Sort Algorithm
import array as arr
nums = arr.array('i',[5,4,3,1,2])
def insertionSort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]<nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                print(nums)
            else:
                break
    return nums
#insertionSort(nums)
print(insertionSort(nums))