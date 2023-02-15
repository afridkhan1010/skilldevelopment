# l=[2,4,5,9,1,54,32,67,81,90]
# m=l
# # ascending order
# for i in range(len(l)-1):
#     for j in range(len(l)-1):
#         if l[j]>=l[j+1]:
#             temp=l[j]
#             l[j]=l[j+1]
#             l[j+1]=temp
            
# print(l)
# # descending order

# for i in range(len(m)-1):
#     for j in range(len(m)-1):
#         if m[j]<m[j+1]:
#             temp=m[j]
#             m[j]=m[j+1]
#             m[j+1]=temp
# print(m)

#--------------------------------------------------------------------------------------

#prime numbers
# n=int(input("enter the number to be checked: "))
# count=0
# for i in range(2,n):
#     if n%i==0:
#         count+=1
# if count>=1:
#     print("not prime")  
# else:
#     print("the number is prime")

# for i in range(2,n):
#     count=0
#     for j in range(2,i):
#         if i%j==0:
#             count+=1
#     if count<=0:
#         print(i)
#------------------------------------------------------------------------------
#first letter uppercase

# string=input("enter the string: ")

# l=string.split()
# op=''
# for i in l:
#     if i[0]>='a' and i[0]<='z':
#         up=chr(ord(i[0])-32)+i[1::]+" "
#         op+=up
    
# print(op)
#-------------------------------------------------------------------------------------
#string letters count occurance

# strinh=input("enter the string: ")
# d={}
# for i in strinh:
#     count=0
#     for j in strinh:
#         if i==j:
#             count+=1
#     d[i]=count

# print(d)
#--------------------------------------------------------------------------------------------
# class Employee_details:
#     def __init__(self,first_name=None,last_name=None,age=None,salary=None):
#         self.name=first_name+" "+last_name
#         self.age=age
#         self.salary=salary
# employees=[]
# for i in range(3):
#     print("enter the employee details: ")
#     first_name=input("enter f_name: ")
#     last_name=input("enter l_name: ")
#     age=input("Enter age: ")
#     salary=float(input("Enter the salary: "))

#     employee=Employee_details(first_name,last_name,age,salary)
#     employees.append(employee)
# salary=[]
# for emp in employees:
#     if emp.salary>=30000:
#         salary.append(emp)
# for emplist in salary:
#     print(emplist.__dict__)

#-------------------------------------------------------------------------------
#vowel to uppercase
# string=input("Enter the string : ")
# vowels="aeiou"
# op=''
# for i in string.lower():
#     if i in vowels:
#         op+=chr(ord(i)-32)
#         continue
#     op+=i
# print(op)

#-------------------------------------------------------------------------------
# duplicate chars

# string=input("enter the string: ")
# d={}

# for i in string:
#     count=0
#     for j in string:
#         if i ==j:
#             count+=1
#         if count>1:
#             d[i]=count
# print(d)

#---------------------------------------------------------------------------------------
#extra spaces

# string="   Hello    world!   "
# # words=string.split()
# # new_s=" ".join(words)
# # print(new_s)
# op=''
# # for i in string:
# for i in range(len(string)-1):
#     if string[i]==" " and (string[i+1]>='a' and string[i+1]<='z'):
#         op+=string[i]
#     if string[i]==" ":
#         continue
#     else:
#         op+=string[i]
# print(op)

#---------------------------------------------------------------------------------------------
#array diff

# arr=[23,27,56,90,34,27,11,65,48]
# op_arr=[]
# for i in range(0,(len(arr)//2)+1):
#     op= arr[i]-arr[(len(arr)-1)-i]
    
#     if i > (len(arr)/2)-1:
#         op=arr[i]
        
#     op_arr.append(op)

# print(op_arr)
#------------------------------------------------

#spell check

# s = "i ate a apple and a umbrella i have"
# new_s = ""
# vowel=['a','e','i','o','u']
# words=s.split()
# for i in range(len(words)):    
#     if words[i] == "a" and i+1 < len(words) and words[i+1][0]in vowel:
#         # replace the "a" with "an"
#         new_s += "an "
#         i += 1
#     else:
#         # keep the original character
#         new_s += words[i]+" "

# print(new_s.strip())