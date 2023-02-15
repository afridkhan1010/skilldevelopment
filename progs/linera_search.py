
pos=-1
def l_search(list,n):
    for i in range(len(list)):
        if list[i]==n:
            globals()['pos']=i
            return True







list=[2,45,65,13,10,1,67,98]
n=int(input("enter the number to be searched in the list: "))

if l_search(list,n):
    print("the search is found at position",pos)
    
else:
    print("the number is not in the list")