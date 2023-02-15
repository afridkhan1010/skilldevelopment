num=input('enter the number')
last2=num[-2:]
print(last2)
if (int(last2)>25):
    print(num[:-2])
    print((num[:-2])+'50')
elif (int(last2)<25):
    print((num[:-2])+'00')