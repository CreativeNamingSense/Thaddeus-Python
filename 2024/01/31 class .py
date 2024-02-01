class Student:
    def __init__(self, Name, Class, Age, House):
        self.StudentName = Name
        self.StudentClass = Class
        self.StudentAge = Age
        self.StudentHouse = House
    def StudentDetails(self):
        print("Student name is : ", self.StudentName)
        print("Student class is : ", self.StudentClass)
        print("Student age is : ", self.StudentAge)
        print("Student house is : ", self.StudentHouse)


FirstStudent = Student("Mike Oxlong", "JC 2 Acting", 16, "Black and Orange")
FirstStudent.StudentDetails()