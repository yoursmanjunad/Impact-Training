import sys
num = 10
print(sys.getsizeof(num)) #Minimum size of int = 28 bytes.
#Maximum size of int depends on the length of the string.
#
#
# string = "Gunturu#Karam#babu#guruji#hanuman"
# newStr = " "
# for i in range(0,len(string)):
#     if string[i] == '#':
#         var = string[i-1]
#         string.replace(var, '')
# print(string)
#remove the charachter previous of hashtag #
# test = input()
# res = []
# for i in test:
#     if i!="#":
#         res.append(i)
#     elif len(res)>0:
#         res.pop()
# print("".join(res))

#reverse the words
# I/O - Happy coding with Manjunath
# # 0  Manjunath with coding Happy
# print(" ".join((input().split())[::-1]))

# l1, l2, l3 = [],[100],[200,300]#list occupy more memory than tuple
#
# print(sys.getsizeof(l1), sys.getsizeof(l2), sys.getsizeof(l3))
# t1, t2, t3 = (),(100), (200,300) # tuple single element considerd as integer, to not to then we include comma next to the single element
# print(sys.getsizeof(t1), sys.getsizeof(t2), sys.getsizeof(t3))
# Dictionary
parul = {}
print(parul,type(parul))
parul = dict()
print(parul,type(parul))
parul = {1: "AA MG", 2:"Star ante rebel ye raa", 3:"Evadraa nuvvu", 4:"Address pettu"}
print(parul,type(parul))
print(*parul.keys())
print(*parul.values())
print(parul.items())
for i,j in parul.items():
    print(i," ==>", j)
# duplicate keys are not allowed in thh python
parul = {1:20, 2:30, 3:40}
print(parul)
parul[2] = 50
print(parul)
parul[4] = 40
print(parul) #even if there is no key and we are agging value to that key, python creates thaat key and assigns the value to it. 