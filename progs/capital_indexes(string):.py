def capital_indexes(string):
    CAP_LIST=[]
    for i in range(len(string)):
        if string[i]>="A" and string[i]<="Z":
            CAP_LIST.append(i)
    return CAP_LIST
    
    

string="HeLlOo"
x=capital_indexes(string)
print(x)
