#Given 2 strings s1 and s2, modify string s1 such  that all the common characters of s1 and s2 is to  be removed aand the uncommon of s1 and s2 is to be concatenated.
#str1 = aacdb
#str2 = gafd
# ans  = cbgf
str1 = "aacbd"
str2 = "gafd"
strAns = ""
#for printing the commons in two strings
# for i in range(0,len(str1)):
#     if str2.find(str1[i])==True:
#         strAns+=str2[i]
# print(strAns)

# for i in range(0,len(str1)):
#     for j in range(i,len(str2)):
#         if str2.find(str1[i]) == False:
#             strAns += str2[j]
# print(strAns)

for i in str1:
    if(i not in str2):
        print(i, end="")
for i in str2:
    if (i not in str1):
        print(i, end="")
