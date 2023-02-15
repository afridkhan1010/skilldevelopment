max_ele = int(input("Enter the number of elements\n"))
arr = []
for index in range(max_ele):
    arr.append(int(input()))

num = arr[0]
index = 0
while index < max_ele:
    if num != arr[index]:
        print(num)
        num += 1
    else:
        index += 1
        num   += 1