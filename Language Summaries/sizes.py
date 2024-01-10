# import sys
# num = 10
# print(sys.getsizeof(num)) #Minimum size of int = 28 bytes.
# #Maximum size of int depends on the length of the string.
# #
# #
# # string = "Gunturu#Karam#babu#guruji#hanuman"
# # newStr = " "
# # for i in range(0,len(string)):
# #     if string[i] == '#':
# #         var = string[i-1]
# #         string.replace(var, '')
# # print(string)
# #remove the charachter previous of hashtag #
# # test = input()
# # res = []
# # for i in test:
# #     if i!="#":
# #         res.append(i)
# #     elif len(res)>0:
# #         res.pop()
# # print("".join(res))
#
# #reverse the words
# # I/O - Happy coding with Manjunath
# # # 0  Manjunath with coding Happy
# # print(" ".join((input().split())[::-1]))
#
# # l1, l2, l3 = [],[100],[200,300]#list occupy more memory than tuple
# #
# # print(sys.getsizeof(l1), sys.getsizeof(l2), sys.getsizeof(l3))
# # t1, t2, t3 = (),(100), (200,300) # tuple single element considerd as integer, to not to then we include comma next to the single element
# # # print(sys.getsizeof(t1), sys.getsizeof(t2), sys.getsizeof(t3))
# # # Dictionary
# # parul = {}
# # print(parul,type(parul))
# # parul = dict()
# # print(parul,type(parul))
# # parul = {1: "AA MG", 2:"Star ante rebel ye raa", 3:"Evadraa nuvvu", 4:"Address pettu"}
# # print(parul,type(parul))
# # print(*parul.keys())
# # print(*parul.values())
# # print(parul.items())
# # for i,j in parul.items():
# # #     print(i," ==>", j)
# # # # duplicate keys are not allowed in thh python
# # # parul = {1:20, 2:30, 3:40}
# # # print(parul)
# # # parul[2] = 50
# # # print(parul)
# # # parul[4] = 40
# # # print(parul) #even if there is no key and we are agging value to that key, python creates thaat key and assigns the value to it.
# # # print(parul.get(7)) #if we try to get value of a key which not present in the dict, it returns NONE
# # # print(parul.get(7,"Key Not found")) # here,if the value present for the key it returns the value, else of NONE, We print this string
# # # print(parul.setdefault(5,"set default method"))
# # # print(parul) # if the value not fouhnd, it makes changes in the list with the provided string or any value.
# # # # Get vs setdefault()
# # # parul = {}
# # # parul.update({10: "Po ra kota L..."})
# # # parul.update({20: "Thaggedele"})
# # # print(parul)
# # parul = {}
# # count = int(input("Enter students count: "))
# # for i in range(count):
# #     roll_No = int(input("Enter Roll No: "))
# #     name = input("Enter student's name: ")
# #     parul.update({roll_No: name})
# # print(parul)
# #Create Dynamic dictionary, give 3 subjects marks,  dynamically. N = No.of students. Firstt key - roll no,
# # parul = {}
# # marks = {}
# # max_score = topper = 0
# # for i in range (3):
# #     roll_No = int(input("Enter Roll Number: "))
# #     marks = sum(map(int,input().split()))
# #     parul.update({roll_No:marks})
# #     if marks>max_score:
# #          max_score = marks
# #          topper = roll_No
# #
# # print(max_score, topper)
#
# # take an input
# # check wheter it in english or number itself i=have any bubble, then print the number which not having bubble#
# # i/0 -> 123 e
# # o/o -> 2  one two three , we have 'e' in one and three, so print these 2
#
# # num = input("Enter a number: ")
# # ch = input("Enter a character: ")
# # alphaNum = {}
# # dig = {1: 'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
# # for i in dig:
#
#
# # Giving binary string,
# # i/o -> 11000100101000010
# #print(len(max(input().split("1"))))
# # find the occurances of each character in string
# string1 = "Assassination"
# # char_count = {}
# # for char in string1:
# #     char_count[char] = char_count.get(char, 0)+1
# # print(char_count)
# #
# # char_count = {}
# # dig = {}
# # for i in string1:
# #     dig.update(char:string1.count(i))
#
# val = ({i:string1.count(i) for  i in string1})
# print(val)
# list = val.values()
# for i in list:
#     if i!= i+1:
#         print(False)
#         break
#     print(True)
# #sorting dictionaary
# import operator
# d = {1:10, 2:2, 3:33, 4:12}
# print(dict(sorted(d.items(), key=operator.itemgetter(0))))
# print(dict(sorted(d.items(), key=operator.itemgetter(1))))# 0 - keys, 1 - values
# print(dict(sorted(d.items(), key=operator.itemgetter(0), reverse=True)))
# print(dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True)))
#
# import heapq
# d = {1:10, 2:2, 3:33, 4:12}
# print(heapq.nlargest(2,d))
# print(heapq.nsmallest(1,d))
# print(max(d))

# try:
#     print(1//value)
# except NameError as e:
#     print("USE CHATGPT TO CODE THIS",e)
# except ZeroDivisionError as e:
#     print("Error ",e)
# finally: #if we get error or not, finally will execute for sure!
#     print("We are having a fantastic offer sir, please delete this program and use anyone's else")

for i in range(0,6):
    print("\t",i,"\t")
#
# # print in format
# 1      5
#   2   4
#     3
#   2   4
# # 1      5
#  1       5
#    2    4
#       3
