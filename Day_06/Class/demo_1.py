l1= [1,2,3,4,5]
l2 = [3,2,5,7,3]
#l2.append("abcd")
# print(id(l1), id(l2))
# print(l2)
# if 40 in l2:
#     print("Present")
# else:
#     print("Absent")
# #copying the elements in the same order, gives the same refernece to the second list.
# #Just like in java, string pool takes the responsibility for the duplication of the same list in to other, and points to the same elements for the second
# #Here, having same values makes the scenario.
# #
# for i in range(len(l2)):
#     print(l2[i])
# l2 = [12,4.4,"abcd"]
# for i in l2:
#     print(i, type(i))
#
# # Deleting the element from the list
# del l2[0]
# print(l2)
# del l1[2:4]
# print(l1)
# del l1
#print(l1) - Throws Name Error
# We cant directly access the address of the object, we can only do it in Assembly Language.
#We have a named reference, we just change the reference to the null when we actually delete the list.
# l1.pop()
# print(l1)
# print(l1.size())
# This gives the attribute error we cause we have no method for the size separately, size and len methoods are the same, size is available in cpp
# capacity - the maximum elements data structure can attain, just for that moment. for cpp
#l2.pop(l1[1]) #it takes the l1[1] value as the index to be removed from the list. Always, pop method uses index value to temove the element from the list
# # del l2[6] # it gives the IndexError, because we are accessing the index which is out of range for the list
# print(id(l2))
# var = l2.sort()
# print(var) # we get none if we store the sorted list to another var. It happens because sort method is used in place sorting, but for making new sorted list, we use sorted(l2) and assigns the sorted list to the variable which we;ve assigned it
# l2.sort(reverse=True)
# print(l2)

num = [1,2,2,3,3,3,4,4,4,4,4]
print(num.count(4))
