'''
A file in which all about the strings been included which discussed in class
'''
str1 = "Hello\nWorld"
str = r"Hello,\nWorld I am chitti memory 1 zetaByte Thala for a reason"
str2= "World"
# print(str1+str2)
# print(str1*5)
# print(str1[4])
# print(str1[2:4])
# print('w' in str1)
# print('W' in str2)
# print('Wo' not in str1)
# print(r"Hello\n World")
# print("The str1 is %s"%(str1)) # PlaceHolder
# print(str1[4:2]) # No Output
# print(str1[2:7])
# print(str1[2:len(str1)]) #len(str1) for getting length of the string
# print(str)
# print("String present in the str is %s, the size is "%(str), len(str)) ## to use this we need to include % s in in string and in method calling aswell
# print("String in str2 is %s "%(str2))
# print(str.upper())
# print(len(str1))
# l1 = str1.split()
# print(l1)
# l2 = str.split()
# print(l2)
# l2= str.split(',')
# print(l2)
# a,b= input()
# print(a,b)
# a,b = "Manjunath", "Shetty"
#print(a,b)
# leng = input() # This is a programming class
#print(leng) #Prints everything
# a,b = input().split()
# print(a and b.upper())
# a,b = input().split()
# print(a,b) #['Manjunath', 'shetty']
#If we give three words for two variables using .split aswell, we cannot store thosse bacause of Value Error!
# str1=str.replace('H', 'M')
# print(1) #We cannot replace in-string but we can just create new string and perform this action while inserting particular  element into the var
#len()
#.upper
#.lower
#.join
#.split
#.find
#.index
#isalnum
#isdigit
#isnumeric
#islower
#isipper

print(len(str1))
print(str1.upper())
print(str1.lower())
print(str1.join(str1))
print(str1.split(','))
print(str1.find('T'))
print(str1.index('c'))
print(str1.isalnum())
print(str1.isdigit())
print(str1.isnumeric())
print(str1.islower())
print(str1.isupper())