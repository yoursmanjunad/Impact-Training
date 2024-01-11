# # indexing is not possible with dictionary and sets
# # we can't use sset for spliting, slicing
# # set doesn't allow duplicates
# parul = set()
# print(parul,type(parul))
# parul = {10, "All Hail the Tiger", 3.14, 44, 44,22312,434,3212412, True, False}
# print(parul)
#
# li = [10,10,10,10]
# print(li)
# li = set(li)
# print(li) #converting list to set to remove the duplicates
# #we can modify the set. Normal sets are mutable but frozen set is immutable
# # import array as arr
# # nums = arr.array('i',[1,1,3,2,3,4,5,6])
# # varem = set(nums)
# # print(varem)
# # varem = list(varem)
# # print(varem)
#
# # s = set()
# # N = int(input())
# # for i in range(N):
# #     s.add(int(input()))
# # print(s)
#
#
# x = {11,12,13,14}
# print(x)
# x.remove(12)
# x.discard(22) # if we try to remove not element in list presence, then it throws a Key Error
# print(x)
#
# pack_set = set()
# pack_set.add("Numpy")
# print(pack_set)
# pack_set.update(["panda", "Matplotlib"]) #using add, we can pass only one argument, but in update, we can pass multiple
# print(pack_set)
#
# x = {11,12,13,1,4,41}
# y = x.copy()
# print(y)
# x.clear()
# print(x) #clear removes all the values in a set and if we print, it results in set()
# # del y # it throws as error, because here we are dereferencing it completely
# # print(y) #where as in clear method, we are just removing values from it instead of deleting it completely.
# x = {11,12,13,14,15,16}
# y = {12,44,523,12,14,15}
# print(x.difference(y))
# print(y.difference(x))
# x.difference_update(y)
# print(x)
# #
# # lib1 = set(["BeautifulSoup","scikit","Terraform"])
# # lib2 = set(["seaborn", "beautifulHussain"])
# # lib3 = lib1 & lib2
# # print(lib3)
# # lib2 = lib1-lib3
# # print(lib2)
#
# x = {1,2,3,4,5}
# y = {1,2,3,9,8}
# # z = {2,3,5,6}
# # print(x.intersection(y))
# # print(y.intersection(z))
# # print(set.intersection(x,y,z))
# # print(x,y,z)
# # print(x.intersection_update(y))
# # print(x,y,z)
# #
# # test1 = {'Numpy', 'Tensorflow'}
# # test2 = {'pandas', 'kubernetes'}
# # test3 = test1 ^ test2
# # print(test3)
# # test = test2-test1
# # print(test)
#
# s = set()
# print(s,type(s))
# fs = frozenset()
# print(fs, type(fs))
#set() <class 'set'>
#frozenset() <class 'frozenset'>
# s.add(3)
# fs.add(4) #it throws the attribute error
# print(fs)
# sentence = {"This ", "is ", " Elon", "Musk"}
# res_words = {word for word in sentence if len(word)<=3}
#print(res_words)
sentence = {"hello", "how" ,"are" ,"you?" ,"halmathi" ,"habibooo"}
res_words = {word.capitalize() if word[0]=='h' else word for word in sentence}
# print(res_words)
# print(res_words.reverse())

