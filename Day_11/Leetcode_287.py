nums = [1, 3, 4, 2, 2]
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]==nums[j]:
#             print("Yes, found")

def fun1(nums):
    length = len(nums)
    length = length // 2
    for i in range(0, length):
        for j in range(i + 1, length):
            if nums[i] == nums[j]:
                return nums[i]
    for i in range(length, len(nums)):
        for j in range(length + 1, len(nums)):
            if nums[i] == nums[j]:
                return nums[i]
    return -1
print(fun1(nums))