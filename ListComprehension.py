from functools import reduce

l1= [2,4,6,8,10,12]

list=[]

listComp= [x*4 for x in l1]

for x in l1:
    a= x*3
    list.append(a)

print("list comprehended: ", listComp)
print("List before updation: ", l1)
print("List after updation: ", list)

sum= reduce(lambda a,b: a+b, l1)
sumUp= reduce(lambda a,b: a+b, list)

print(sum)
print(sumUp)