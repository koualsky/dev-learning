class Salary:

    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (12 * self.pay) + self.bonus


class Employee:

    def __init__(self, name, salary_obj):
        self.name = name
        self.salary = salary_obj

    def total_salary(self):
        return self.salary.annual_salary()


salary = Salary(100, 7)
employee = Employee('Rita', salary)
print(employee.total_salary())