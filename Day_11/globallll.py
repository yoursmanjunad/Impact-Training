x = 100
def variable():
    global x
    x = 200
    print(x)
variable()
print(x)