#Given array A of positive elements, count the number of small elemets on right side of each array
# [5,4,3,2,1] - Input
# 4,3,2 - Output

from array import *

list = [5,4,3,2,1]
ansList = []
for i in range(0,5):
    count = 0
    for j in range(i+1,5):
        if list[i]>list[j]:
            count+=1
    ansList.append(count)

print(ansList)