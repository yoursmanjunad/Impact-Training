# Insertion sort
- Insufficient Memory, easy to implement,when we have continous inflow of numbers and we want to keep them sorted. 
- When time is a concern, we try to avoid the insertion sort. 
- [ ] Given an array nums of size n, return the majority element. The majority element is the element that appears more than n//2 times. You may assume that the majoity element always exists in the array
## Decorators:
```commandline
def printMe():
    print("Majito ki rubi ")
m1 = printMe
print(m1)
m1()
def outer_fun(inner_fun):
    print("Chipi chipi chapa chapa")
    # def inner_fun():
    #     print("Dubi Dubi Daba Daba")
    inner_fun()
outer_fun(m1)
```
- When a function is decorated, it becomes callable. 