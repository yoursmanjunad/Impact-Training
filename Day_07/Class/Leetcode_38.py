str1 = "33"
strAns = ""

for i in range(0, len(str1)):
    count = 0
    for j in range(i + 1, len(str1)):
        if str1[i] == str1[j]:
            count += 1
print(count)
