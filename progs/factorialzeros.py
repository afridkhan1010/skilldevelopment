n=int(input("enter the number:"))
for i in range(1,n):
    temp=n*i
    n=temp
print(temp)
newnum=str(temp)
n=-1
count=0
for j in range(len(newnum)):
    
    
    
    if int(newnum[n])==0:
        count+=1
        n=n-1

    
print(count)
