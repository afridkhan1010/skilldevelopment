string="idea jio"
temp=string.split(" ")
res=[]
op=''
for i in temp:
   
    if i[0]in ('a','e','i','o','u'):
        temp1=chr(ord(i[0])-32)
        res+=temp1+i[1:]+" " 
       
        if res[-2] in ('a','e','i','o','u'):
            res[-2]=chr(ord(res[-2])-32)
        print(res)
    else:
        res+=i

      



op=op.join(res)


print(op)


    
    

        

