char=input("enter the sentance: ")
rep=input("enter the char to replace with space: ")
op=""
for i in char:
    if i==" ":
        i=rep
    op+=i
print(op)