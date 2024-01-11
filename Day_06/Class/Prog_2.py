#Program 2
# Alternative Merge two strings
# bhima ABCDEFGH
# O/P  bAhBiCmDaEFGH

str1 = input("Enter a string: ")
str2 = input("Enter second string: ")
str1Length = len(str1)
str2Length = len(str2)
newStr = ""
if str1Length<str2Length:
    for i in range(0, len(str1)):
        newStr += str1[i]
        newStr += str2[i]
if str2Length<str1Length:
    for i in range(0, len(str2)):
        newStr += str1[i]
        newStr += str2[i]
if (str1Length>str2Length):
    for i in range(str2Length,str1Length):
        newStr+=str1[i]
if (str2Length>str1Length):
    for i in range(str1Length,str2Length):
        newStr+=str2[i]
print(newStr)

# Sir Soution

if '.' in str1:
    print("Present")
    str2 = str1[:len(str1)-1]
    str2=str2[::-1]
    str2+='.'
    print(str2)
    str2 = str1[:len(str1)-1]
    str3 = str.split()
    print(str3)
    str4 = []
    for i in str3:
        i = i[::-1]
        str4.append(i+" ")
    print(str4)
    str5 = " "
    for i in str4:
        str5+=i
    str5+='.'
    print(str5)