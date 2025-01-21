class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        return f"Manager: {self.name}, Salary: {self.salary}, Department: {self.department}"

name_emp = input("Introduceți numele angajatului: ")
salary_emp = float(input("Introduceți salariul angajatului: "))
emp = Employee(name_emp, salary_emp)

name_mgr = input("Introduceți numele managerului: ")
salary_mgr = float(input("Introduceți salariul managerului: "))
department_mgr = input("Introduceți departamentul managerului: ")
mgr = Manager(name_mgr, salary_mgr, department_mgr)

print(emp.get_details())
print(mgr.get_details())
