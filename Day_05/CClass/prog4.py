# program to check if product of digits of a number at even and odd places is equal
#2841 - yes

n = 2841
list = [2,8,4,1]
odd =1
even =1
for i in range(0,3):
    if i%2==0:
        even = even * list[i]
    else:
        odd = odd * list[i]

print(odd == even)

