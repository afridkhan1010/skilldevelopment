l1=[3,12,4,57,31,49,98,2,5,6,7]
l2=[2,5,3,54,61,90,87,31]
op=l1+l2

common=[]
uncommon=[]
for i in l1:
    if i in l2:
        common.append(i)
    else:
        uncommon.append(i)
print(common)

for k in common:

    flag=False
    for j in l1:
        if j==k:
            flag=True
    if flag:
        l1.append(k)
print(l1)

for a in common:
    flag=False
    for b in l2:
        if a==b:
            flag =True
    if flag:
        l2.append(a)
print(l2)


a=list(set(l1)|set(l2))
print(a)
print("The present(all) elements in both lists are:")
for i in a:
    print(i)