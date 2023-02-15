pos=-1
def b_search(list, n):
    l=0
    u=len(list)-1
    
    while l<=u:
        mid=l+u//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False


list=[2,4,9,11,13,23,45,76,99,184]
n=int(input('Enter the number to be searched: '))

if b_search(list,n):
    print("the number is found at position",pos+1)
else:
    print("the number  is not found: ")