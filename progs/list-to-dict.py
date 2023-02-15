n=int(input("enter the number of elements for the dictionary: "))
keys=[]
values=[]
for i in range(0,n):
    l1=input("enter the list1 elements: ")
    keys.append(l1)

for j in range(0,n):
    l2=input("enter the second list elemnets")
    values.append(l2)

print(keys)
print(values)

d=dict(zip(keys,values))
print(d)