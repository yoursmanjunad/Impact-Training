# import array as arr
# nums1 = arr.array('i',[1,2,3,4,5,6,7])
# k = 3
# till = len(nums1) - k
# nums2 = arr.array('i')
# for val in range(till,0):
#     nums2.append(nums1[val])
# print(nums2)
nums = [2,2,1]
for i in nums:
    for j in nums:
        if nums[i]==nums[j+1]:
            continue
    print()