def add_dots(string):
    temp_string=""
    for i in range(len(string)):
        if i==len(string)-1:
            temp_string+=string[i]
        elif string[i]!=".":
            temp_string+=string[i]+"."
    return temp_string
string="test"
op=add_dots(string)

def remove_dots(op):
    rm_dot=''
    for i in range(len(op)):
    
        if op[i]!=".":
            rm_dot+=op[i]
        else:
            rm_dot+=""
    return (rm_dot)
    

print(remove_dots(op))