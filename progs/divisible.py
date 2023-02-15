arr=[10,17,6,5,22,12,10,6,5,33]
# num=int(input("enter the number by which you divide"))
# res=[]
# for i in len(arr):
#     # if i%num==0:
#     #     print("true")
        
#     # else:
#     #     print('false')
#     for j in len(arr)-1:
#         print(i,j)
#         if arr[i]==arr[j]:
#             print('repeated',j)
print(max(arr)-min(arr))
large=arr[0]
small=arr[0]
for i in range(len(arr)):
    if large<arr[i]:
        large=arr[i]
    if small>arr[i]:
        small=arr[i]
temp=large-small
print(temp)



    