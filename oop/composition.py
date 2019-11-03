class Salary:

    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (12 * self.pay) + self.bonus


class Employer:

    def __init__(self, name, pay, bonus):
        self.name = name
        self.salary = Salary(pay, bonus)

    def total_salary(self):
        return self.salary.annual_salary()


employer = Employer('Patrick', 100, 5)
print(employer.total_salary())