"""ZŁY KOD
class Employee():
    def calculate_payment(self):
        ...

    def report_hours(self):
        ...

    def save(self):

Poniżej dobry kod, jak widać działa to na zasadzie agregacji, gdzie dane
są przechowywane w obiekcie Employee, a metody to osobne klasy. W ten sposób
można w nieskończoność dodawać i odejmować różne funkcjonalności danego
obiektu-np-Employee. Wystarczy wtedy do takiego obiektu jako argument wrzucić
referencję do obiektu employee i przeliczy to danego employee'ra.
"""


class EmployeePaymentCalculator():
    def calculate_payment(self, employee):
        ...


class EmployeeTimeReport():
    def report_hours(self, employee):
        ...


class EmployeeRepository():
    def save(self, employee):
        ...