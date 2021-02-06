class Employee:
    total_employees = 0
    expenses = 0.00

    def __init__(self, first, family, salary, department):
        self.first_name = first
        self.last_name = family
        self.salary = salary
        self.dept = department
        Employee.total_employees += 1
        Employee.expenses += salary

    def average_salary(self):
        value = Employee.expenses / Employee.total_employees
        print("Average of employee salary is", str(value))


class Fulltime(Employee):

    def __init__(self, first, family, salary, department, years):
        self.first_name = first
        self.last_name = family
        self.salary = salary
        self.dept = department
        self.tenure = years
        Employee.total_employees += 1
        Employee.expenses += salary

    def service(self):
        print("This employee has worked here for", self.tenure, " years")
