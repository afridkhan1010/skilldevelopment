inp="hello"
count=len(inp)
op=' '
while count>0:
    op+=inp[count-1]
    count=count-1
print(op)

ot_str=''
for i in inp:
    ot_str=i+ot_str
    print(ot_str)
