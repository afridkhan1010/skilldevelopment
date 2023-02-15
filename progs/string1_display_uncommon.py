string1=input("enter the string")
string2=input("enter the second string:")
op=''
for i in string1:
    if i not in string2:
        op+=i
print(op)
print(set(string1))
print(set(string2))
a=list(set(string1)-set(string2))
print(a)
