string=input("enter the string: ")
count=0
word_count=1
for i in string:
    if i!=" ":
        count+=1
    if i==" ":
        word_count+=1
print(count)
print(word_count)