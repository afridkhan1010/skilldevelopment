n1=int(input('enter 1st num: '))
n2=int(input("enter the second num: "))
if n1>n2:
    minimum=n2
else:
    minimum=n1

for i in range(1,minimum+1):
    if(n1%i==0) and (n2%i==0):
        hcf=i

print(hcf)