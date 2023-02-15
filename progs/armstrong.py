n=371
temp=0
num=0
num1=n
power=len(str(n))
while n!=0:
    
    temp=n%10
    temp=temp**power
    n=n//10
    num=temp+num
print(num)

if num == num1:
    print('arm strong')


