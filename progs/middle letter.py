def mid(string):
    op=""
    print(len(string)//2)
    if len(string)%2!=0:
        print("inside string")
        return string[(len(string)//2)]
    else:
        print("inside else part")
        return ""
    
string="abcd"
x=mid(string)
print(x)