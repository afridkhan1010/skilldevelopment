# x=int(input("enter the number to find its cube root: "))
# high=x
# low=0
# while low<high:
#     mid=(low+high)/2

#     if mid**3 < x:
#         low=mid
#     else:
#         high=mid
# print(low)

# def cubic_root(x):
#     low = 0
#     high = x
#     while low < high:
#         mid = (low + high) / 2
#         if mid**3 < x:
#             low = mid
#         else:
#             high = mid
#     return low

def cubic_root(x):
    if x == 0:
        return 0
    elif x > 0:
        return x**(1/3)
    else:
        return -(-x)**(1/3)

print(cubic_root(8))