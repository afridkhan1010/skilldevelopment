def anagram(str1,str2):
    if len(str1)!=len(str2):
        return False
    if(sorted(str1.lower())==sorted(str2.lower())):
        return True
    else:
        return False
str1=input("enter string1: ")
str2=input("enter the secod string")

if(anagram(str1,str2)):
    print("strings are anagram")
else:
    print("not anagram")