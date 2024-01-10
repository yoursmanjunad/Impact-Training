#libraries = ["Star ante rebel ye ra", "ayte velliiiii","AA MG", 'Enti comedy aa' ]
# f = filter(lambda s:s[0]=='S' or s[0]=='E', libraries)
# print(list(f))


scores = (10,20,30,40,50,60)
generate_scores = list(filter(lambda x:x >20 and x<=60, scores))
print(generate_scores)

strs = ["Nenu", "sarada", "saradagke", "Netthi", "pagal", "denginodni"]
greater_str = list(filter(lambda x:len(x)<=5, strs))
print(greater_str)

length = list[map(len, ['Training', 'Digital', 'Python'])]
print(length)

# base, powers = [2,4,6], [1,3,5]
# res = list(map(pow, base, powers))
# print(res)

def change_case(s):
    return s.swapcase()
m = list(map(change_case, "DigiTal IndiA"))
print(*m, sep=" ")

res = "DigiTal InDiaaa"
for i in res:
    if i.isupper():
        res+=i.lower()
    else:
        res+=i.upper()
print("\n",res)

circle_ares = [1.34, 3,45,5.3425, 4.424]
area = list(map(round,circle_ares, range(1,5)))