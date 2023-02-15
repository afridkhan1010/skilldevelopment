num=int(input("enter the number"))
def onezero(num):
    binary=format(num,'b')
    temp=1
    temp=format(temp,'b')
    count1=0
    count0=0
    print(binary)
    

    for i in len(binary):
        temp=binary & temp
        if temp==1:
            count1+=1
        if temp==0:
            count0+=1
        binary>>1

    print(count1)
    print(count0)
onezero(num)
