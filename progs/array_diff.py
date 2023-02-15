arr=[23,27,56,90,34,27,11,65,48]
op_arr=[]
for i in range(0,(len(arr)//2)+1):
    op= arr[i]-arr[(len(arr)-1)-i]
    
    if i > (len(arr)/2)-1:
        op=arr[i]
        
    op_arr.append(op)

print(op_arr)