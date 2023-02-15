arr=[2,31,24,56,19,11,24,33,56,78]
op=[]
print(len(arr)//2)
for i in range(len(arr)//2):
    print('inside for',arr[i])
    temp=arr[i]+arr[(len(arr)//2)+i]
    op.append(temp)
    # print(op)
print(op)