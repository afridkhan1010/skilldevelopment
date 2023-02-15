arr=[11,43,12,9,5,33,59]
smallest=arr[0]
for i in range(1,len(arr)):
    if arr[i]<smallest:
        smallest=arr[i]
print(smallest)

small=min(arr[0],arr[1])
sec_small=min(arr[0],arr[1])

for i in range(2,len(arr)):
    if arr[i]<small:
        sec_small=small
        small=arr[i]
    elif arr[i]<sec_small:
        sec_small=arr[i]
print(sec_small)