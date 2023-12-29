'''
A file in which all about the strings been included which discussed in class
'''
# str1 = "Hello\nWorld"
# str = r"Hello,\nWorld I am chitti memory 1 zetaByte Thala for a reason"
# str2= "World"
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
# #isipper
#
# sen = "Manjunath"
# print(len(sen))
# print(sen.upper())
# print(sen.lower())
# print(sen.islower())
# print(sen.isupper())
# print(sen.find('M'))
# print(sen.isalnum())
# print(sen.isdigit())
# print(sen.isnumeric())
# print(sen.join(sen))

# mag1 = "python is a programming language"
# mag2 = mag1.find("is")
# mag3 = mag1.find("java")
# mag4 = mag1.find("p",5)
# mag5 =mag1.find("i", 6,25)
# print(len(mag1))
# print(mag2,mag3,mag4,mag5)

mag1 = "python is a programming language"
# mag2 = mag1.index("is")
# mag4 = mag1.index("p",5)
# mag5 =mag1.index("i", 6,25)
# mag3 = mag1.index("java")
# str1= "Manju"
# str2="Manju123"
# str3="12345"
# str4="manju2033"
# str5="python 234"
#
#
# print(len(mag1))
# print(str1.isalnum())
# print(str2.isalnum())
# print(str3.isalnum())
# print(str4.isalnum())
# print(str5.isalnum())

#isdigit - no decimal values are allowed in it.
# str1="12344"
# str2="python123"
# str3="IIIV"
# str4="/U00B23"
# str5="Python 34"
# # print(str1.isdigit())
# # print(str2.isdigit())
# # print(str3.isdigit())
# # print(str4.isdigit())
# # print(str5.isdigit())
# print(str1.isnumeric())
# print(str2.isnumeric())
# print(str3.isnumeric())
# print(str4.isnumeric())
# print(str5.isnumeric())

mag2 = mag1[3:0:-2]
print(mag2)