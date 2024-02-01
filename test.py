StudentNumber = int(input("Please input the number of students you want to input :\n"))

StudentName = ["a"] * StudentNumber
StudentGrade = [0] * StudentNumber

for i in range(1,StudentNumber):
    StudentName[i]  = str(input("Please input Student's Name :\n"))
    StudentGrade[i] = int(input("Please input student's grade :\n"))

HighestGrade = StudentGrade[1]
LowestGrade = StudentGrade[1]

for i in range(2,10):
    if StudentGrade[i] >= HighestGrade:
        HighestGrade = StudentGrade[i]
    if StudentGrade[i] <= LowestGrade:
        LowestGrade = StudentGrade[i]
    
print("Highest grade : ", HighestGrade,"\nLowest grade : ", LowestGrade)