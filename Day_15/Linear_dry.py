#This is the program to run Linear Search Algorithm
import array as arr
nums = arr.array('i',[443,53,43,6,5,7,3,4])
target = int(input("Enter the element that you want to search: "))
def linearSearch(nums, target):
    i=0
    while(nums[i]!=target):
        i=i+1
    if nums[i]==target:
        return i
    return -1
print(linearSearch(nums,target))