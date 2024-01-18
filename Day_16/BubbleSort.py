list = [2,3,5,2,5,2,7,3,74,55,41,53]
for i in range(len(list)):
    for j in range(i,len(list)):
        if list[i]<list[j]:
            list[i], list[j] = list[j], list[i]
print(list)

