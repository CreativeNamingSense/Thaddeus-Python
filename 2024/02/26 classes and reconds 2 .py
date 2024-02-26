import pickle
class Student:
    def __init__(self, firstName,lastName,age,house):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.house = house
    def printStudent(self):
        print(f"First name : {self.firstName}")
        print(f"Last name : {self.lastName}")
        print(f"Age : {self.age}")
        print(f"House : {self.house}")
    def __str__(self) -> str:
        return f"{self.firstName}, {self.lastName}, {self.age}, {self.house}"
        
        
firstStudent = Student("Thaddeus", "Chalis", "17", "Green")
secondStudent = Student("Darren", "Dahana", "18", "Yellow")
allStudents = []
allStudents.append(firstStudent)
allStudents.append(secondStudent)


studentFile = open("StudentFile.txt", "w")
studentFile.write(str(firstStudent))
studentFile.close()

studentFile = open("StudentFile.txt", "wb")
pickle.dump(firstStudent, studentFile)
studentFile.close()

studentFile = open("StudentFile.txt", "rb")
fromFile = pickle.load(studentFile)
print(str(fromFile))
studentFile.close()


