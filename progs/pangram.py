from string import ascii_lowercase as asc

string=input("enter the string: ")

def pangram(s):
    print(set(asc))
    print(set(s.lower()))
    print(set(asc)- set(s.lower()))
    return set(asc)- set(s.lower())==set([])

if pangram(string)==True:
    print("string is pangram")

else:
    print("string is not pangram")