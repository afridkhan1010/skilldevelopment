limit=int(input("enter the limit of prime numbers:" ))

def prime(limit):
    for i in range(2,limit+1):
        
        temp=0
        for j in range(2,i):
            
            if (i%j==0):
                temp+=1
        if (temp <=0):
            print(i)
        # return i
prime(limit)

