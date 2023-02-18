def double_letters(string):
    count=0
    for i in range (len(string)-1):
        if string[i]==string[i+1]:
            count+=1
    if count>=1:
        return True
    else:
        return False
    
string="hello"
print(double_letters(string))