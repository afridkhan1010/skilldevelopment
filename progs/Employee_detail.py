# employees=[]

# for i in range(5):
#     print("enter the emplyee detail ",i+1 )
#     first_name=input('enter first name: ')
#     last_name=input('enter last name :')
#     age=int(input("enter the age: "))
#     id=int(input("enter the emp_id: "))
#     salary=float(input("enter the salary: "))

#     employee={"first_name":first_name, "lastname":last_name,"age":age,"id":id, "salar":salary}
#     employees.append(employee)

# print(employees)

class Employee_details:

    def __init__(self,first_name, last_name, age,id,salary):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.id=id
        self.salary=salary








employees=[]
n=int(input("enter the number of employees"))
for i in range(n):
    print("enter the employee details: ",i+1)
    first_name=input("Enter first name: ")
    last_name=input("enter the last name: ")
    age=(input("enter the age: "))
    id=int(input("enter the id: "))
    salary=float(input("enter the salary: "))


    employee=Employee_details(first_name,last_name,age,id,salary)
    employees.append(employee)

print(employees)
name_employee=[]
name_with=input("enter the character: ")
for employee in employees:
    # print(employee.__dict__)
    if employee.first_name.lower().startswith(name_with):
        # print(employee.__dict__)
        name_employee.append(employee)
        
for employee in name_employee:
    print(employee.__dict__)