inp_str=input("enter the string: ")
op=""

if inp_str[0]>='a' and inp_str[0]<='z':

    op+=chr(ord(inp_str[0])-32)+inp_str[1:]
print(op)
opnew=""
#lowercase to uupper case
for i in range(len(op)):
    if op[i]== " ":
        opnew+=op[i]
    if op[i]>='A' and op[i]<='Z':
        opnew+=op[i]
    else:
        opnew+=chr(ord(op[i])-32)

print(opnew)

#uppercase to lower case

lop=''
print(list(opnew))
print(len(opnew))
for i in range(len(opnew)):
    if opnew[i]==" ":
        lop+=" "
    lop+=chr(ord(opnew[i])+32)

print(lop)


##capitalizing 1st and last letter if they are vowels
vowel_word=''
for word in lop.split(" "):
    if len(word)>1:
        if word[0]=='a' or word[0]=='e' or word[0]=='i' or word[0]=='o'or  word[0]=='u':
            vowel_word+=chr(ord(word[0])-32)+word[1:]
print(vowel_word)

