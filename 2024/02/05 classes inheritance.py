class Person:
    def __init__(self, FName, LName):
        self.FirstName = FName
        self.LastName = LName
    def PersonDetails(self):
        print("First name: ", self.FirstName)
        print("Last name: ", self.LastName)




P1 = Person("Matthew", "Owen")
P1.PersonDetails()



class Teacher(Person):

    def __init__(self,FName,LName,Sal):
        Person.__init__(self, FName,LName)
        self.Salary = Sal
    def PersonDetails(self):
        Person.PersonDetails(self)
        print("Salary is: ", self.Salary)



T1 = Teacher("Tommy", "Tjoa", 75.000)
T1.PersonDetails()


class Student(Person):
    def __init__(self,FName,LName,Grd):
        Person.__init__(self, FName,LName)
        self.Grade = Grd
    def PersonDetails(self):
        Person.PersonDetails(self)
        print("Grade is: ", self.Grade)


S1 = Student("Thaddeus", "Chalis", 'A')
S2 = Student("Darren", "Putra", 'B')
S1.PersonDetails()
AS = []
AS.append(S1)
AS.append(S2)
print(AS[0].FirstName)