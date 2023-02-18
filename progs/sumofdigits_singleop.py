n=12345
n1=str(n)
print(n1)
op=0

while len(n1)>1:
    add_op=0
    for i in n1:
        print(int(i))
        add_op=add_op+int(i)
    n1=str(add_op)
print(int(n1))

