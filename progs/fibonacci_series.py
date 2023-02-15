a=0
b=1

n=int(input('enter the nth term: '))
for i in range(0,n):
    if i<=1:
        c=i
    else:
        c=a+b
        a=b
        b=c
    print(c, end=" ")