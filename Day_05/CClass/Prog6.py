#Find if array is palindrome or not
l1 = [3,1,4,5,2]
l2 = l1.sort()
l3 = tuple(reversed(l1))
l4 = tuple(reversed(l1))
print(l3==l4)
