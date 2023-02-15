class Emmployees:
    def __init__(self,f_name,l_name,age, salary):
        self.name=f_name+" "+l_name

        # self.name=f_name+" "+l_name
        self.age=age
        self.salary=salary

    def compare(self,other):
        if self.age>=other.age:

            return True
        else:
            return False

    def show(self):
        print("show method called")
        return self.name
    @staticmethod
    def salary(salary_range):

        if E1.salary>salary_range:
            print(f"E1 salary is greater than{salary_range} and the salary is {E1.salary}")
        if E2.salary>salary_range:
            print(f"E2 salary is greater than {salary_range} and the salary is{E2.salary}")
        if E3.salary>salary_range:
            print(f"E3 salary is greater than {salary_range} and the salary is{E3.salary}")
        if E3.salary>salary_range:
            print(f"E3 salary is greater than {salary_range} and the salary is{E3.salary}")
    @staticmethod
    def display_names(names_with):
        if E1.name.startswith(names_with):
            print(f"the employee name starts with char '{names_with}' is {E1.name}")
        if E2.name.startswith(names_with):
            print(f"the employee name starts with char '{names_with}' is {E2.name}")
        if E3.name.startswith(names_with):
            print(f"the employee name starts with char '{names_with}' is {E3.name}")
        if E4.name.startswith(names_with):
            print(f"the employee name starts with char '{names_with}' is {E4.name}")
E1=Emmployees('Afrid','khan',25,25000)
E2=Emmployees('Tazneen','khan',22,15000)
E3=Emmployees("Affan","zaidi",24,17000)
E4=Emmployees("shri","kanta",24,19000)

if E1.compare(E2):
    print(f"Empleyee {E1.name} age is greater than {E2.name}")

print(E1.show())
print(E4.show())

Emmployees.salary(int(input("enter the salary range to display employees: ")))
Emmployees.display_names(input("enter the character to display the names with: ").upper())