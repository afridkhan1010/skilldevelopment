string=input("enter the string")
l=string.split()
d={}
for i in l:
    count=0
    for p in l:

        if i == p:
            count+=1
    d[i]=count
print(d)
