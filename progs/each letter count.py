string=input("Enter the string: ")
letters={}

for i in string:
    
    count_i=0
    for letter in string:
        if i==letter:
            count_i+=1
            letters[i]=count_i
print(letters)