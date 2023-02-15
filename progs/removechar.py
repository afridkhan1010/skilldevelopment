char=input("enter the charachter string: ")
rm_char=input("enter the character to be removed: ")
if rm_char in char:
    char=char.replace(rm_char,'')
    print(char)