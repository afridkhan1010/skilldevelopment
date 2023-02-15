string=input("enter the string: ")
o_lettr=input("enter the character to be find: ")
count=0
for i in string:

    if i==o_lettr:
        print("match found")
        count+=1
print(count)