#Given array A of positive elements, count the number of small elements on right side of each array
# [5,4,3,2,1] - Input
# 4,3,2 - Output

from array import *

# list = [5,4,3,2,1]
# ansList = []
from array import *
arr = array('i',[5,4,3,2,1])
# ansArr = array('i',)
def func(arr):
 for i in range(len(arr)):
    count = 0
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            count+=1
    arr[i]=count
 return arr
ansArr = func(arr)
print(ansArr)