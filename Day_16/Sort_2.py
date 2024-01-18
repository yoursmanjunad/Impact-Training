import array as arr
nums = arr.array('i',[4,3,5,6,2,6,7,12,62])
for i in range(len(nums)):
    min_Index = i
    for j in range(i+1,len(nums)):
        if nums[min_Index] > nums[j]:
            min_Index = j
        nums[i], nums[min_Index] = nums[min_Index], nums[i]
print(nums)