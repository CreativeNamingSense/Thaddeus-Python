class Salary:
    def __init__(self, sal):
        self.MonthlySalary = sal
    def ShowMonth(self):
        return self.MonthlySalary
    def ShowAnnum(self):
        return self.MonthlySalary * 12

S1 = Salary(100)
S1.ShowAnnum()
S1.ShowMonth()

class Employee():
    def __init__(self, name, age, sal):
        self.EmpName = name
        self.EmpAge = age
        self.EmpSalary = sal
    def Show(self):
        print("Name: ", self.EmpName)
        print("Age: ", self.EmpAge)
        print("Monthly Salary: ", self.EmpSalary.ShowMonth())
        print("Yearly Salary: ", self.EmpSalary.ShowAnnum())

E1 = Employee("Jeff", 2, S1)
E1.Show()