n=11211
rev=0
temp=0
while n!=0:
    temp=n%10
    rev=rev*10+temp
    print(rev)
    n=n//10
print(rev)