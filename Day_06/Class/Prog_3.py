#Program 3
#Reverse the given string along words in the line
# This is a C Program
# margorP C si sihT.
# sihT si C margorP.

def func(str1):
    newStr = ""
    strlength = len(str1)
    for i in range(1, len(str1) + 1):
        if str1[-i]=='.':
            continue
        newStr += str1[-i]
        # newStr[strlength-1] = newStr[0]
    return newStr

str1= input("Enter a String: ")
if len(str1)==0:
    print("Please Retry by giving some text""")
print(func(str1))