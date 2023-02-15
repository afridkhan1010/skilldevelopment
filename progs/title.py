x="hello me"
# x=x.title()
op=list(x)
temp=[]
if x[0]>='a' and x[0]<='z':
    op=chr(ord(x[0])-32)
    # print(op)
temp+=op
for i in range(len(x)):
    if x[i]==" " and (x[i+1]>="a" and x[i+1]<='z') :
        temp2=chr(ord(x[i+1])-32)
        temp+=temp2
    elif x[i]>='a'and x[i]<='z':
        temp+=x[i]

        # print(temp)

    
        
    
    else:
        temp+=x[i]

    print(temp)
    # temp+=x[i]
    # print(temp)
    
    # print(op)
