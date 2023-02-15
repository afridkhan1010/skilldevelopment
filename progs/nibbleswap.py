inp=0x45
temp=bin(inp) <<4
print(temp)
op=(inp>>4)& 0x0f
op=temp|op
print(op)