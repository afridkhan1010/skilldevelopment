num=int(input("enter the number:" ))
def armstrong(num):
    temp=num
    n=0
    a=0
    num=list(str(num))
    for i in (num):
        print(i)
        n=int(i)**3
        
        print(n)
        a+=n
        print(a)
        if a==temp:
            print("armstrong number")
        else:
            print("not and armstrong num")
armstrong(num)



