char=input("enter the character:" )
if char>='A' and char<='Z':
    op=(ord(char)-ord('A'))+1
    print(op)
elif char>='a' and char<='z':
    op=(ord(char)-ord('a'))+1
    print(op)
