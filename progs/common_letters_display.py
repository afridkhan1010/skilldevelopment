string1=input('Enter strinng 1: ')
string2=input('Enter strinng 2: ')
commmon=''
uncommon=''
for i in string1:
    if i in string2:
        commmon+=i
    else:
        uncommon+=i
print(commmon)
print(uncommon)
