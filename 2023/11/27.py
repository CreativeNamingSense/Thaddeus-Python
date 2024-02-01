StudentName = ["a","b","c","d","e","f","g","h","i","j"]
StudentGrade = [1,1,1,1,1,1,1,1,1,1]

for i in range(1,10):
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