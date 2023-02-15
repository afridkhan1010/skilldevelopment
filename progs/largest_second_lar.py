arr=[11,43,12,9,5,33,59]
largest=arr[0]
for i in range(1,len(arr)):
    if arr[i]>largest:
        largest=arr[i]
print(largest)

lar=max(arr[0],arr[1])
sec_lar=min(arr[0],arr[1])

for i in range(2,len(arr)):
    if arr[i]>lar:
        sec_lar=lar
        lar=arr[i]
    elif arr[i]>sec_lar:
        sec_lar=arr[i]
print(sec_lar)