class Employee:
    def __init__(self, name, salary, YOE):
        self.name = name
        self.salary = salary
        self.YOE = YOE

    def calculate_salary(self):
        if self.YOE < 5:
            print(f"{self.name}: We will offer {self.salary} rs")

        elif 5 <= self.YOE <= 10:
            self.salary += self.salary * 0.10
            print(f"{self.name}: Your revised salary is {self.salary}")

        else:
            self.salary += self.salary * 0.15
            print(f"{self.name}: Your revised salary is {self.salary}")


# Child Class 1
class RegularEmployee(Employee):
    def __init__(self, name, salary, YOE, working_days):
        super().__init__(name, salary, YOE)
        self.working_days = working_days

    def calculate_salary(self):
        # call parent logic first
       # super().calculate_salary()

        # add bonus
        self.salary += self.working_days * 50
        print(f"{self.name}: Salary with bonus is {self.salary}")


# Child Class 2
class ContractEmployee(Employee):
    def __init__(self, name, salary, YOE, number_of_courses):
        super().__init__(name, salary, YOE)
        self.number_of_courses = number_of_courses

    def calculate_salary(self):
        if self.number_of_courses <= 5:
            print(f"{self.name}: Not eligible for increment")

        else:
            self.salary += self.salary * 0.10
            print(f"{self.name}: Revised salary is {self.salary}")


# Objects
empsal = Employee("Lithu", 150000, 6)
regempsal = RegularEmployee("John", 200000, 0, 350)
contempsal = ContractEmployee("Meena", 120000, 4, 7)

# Polymorphism
totalsal = [empsal, regempsal, contempsal]

for emp in totalsal:
    emp.calculate_salary()
