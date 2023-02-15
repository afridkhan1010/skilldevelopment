inp="hello"
count=len(inp)
op=' '
while count>0:
    op+=inp[count-1]
    count=count-1
print(op)
