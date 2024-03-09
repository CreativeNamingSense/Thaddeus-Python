class treasureChest:
    #Private question as string
    #private answer as integer
    #Private points as integer
    
    
    def __init__(self, theQuestion, theAnswer, thePoints) -> None:
        self.__question = theQuestion
        self.__answer = theAnswer
        self.__points = thePoints
    
    def getQuestion(self):
        return self.__question
    
    def checkAnswer(self,userAnswer):
        if userAnswer == int(self.__answer):
            return True
        else:
            return False
    
    def getPoints(self, userAttempts):
        if userAttempts == 1:
            return int(self.__points)
        elif userAttempts == 2:
            return (int(self.__points) / 2)
        elif userAttempts == 3 or userAttempts == 4:
            return (int(self.__points) / 4)
        else:
            return 0
    

def readData(arrayTreasure):
    fileName = "TreasureChestData.txt"
    try:
        file = open(fileName, "r")
        fileData = file.readline().strip()
        while fileData != "":
            question = fileData
            answer = file.readline().strip()
            points = file.readline().strip()
            arrayTreasure.append(treasureChest(question, answer, points))
            fileData = file.readline().strip()
        file.close()
    except IOError:
        print("Unable to access file.")
        
        
        
def main():
    arrayTreasure = [] #array[5] of type treasureChest
    flag = False


    readData(arrayTreasure)    
    questionNum = int(input("Please input which question you would like to do (1 to 5): "))
    print()
    try:
        print(f"Your question is: ({arrayTreasure[questionNum - 1].getQuestion()})")
        userAttempts = 0
        while flag == False:   
            userAnswer = int(input("Please input your answer: "))
            if arrayTreasure[questionNum - 1].checkAnswer(userAnswer) == True:
                userAttempts = userAttempts + 1
                pointsAwarded = arrayTreasure[questionNum - 1].getPoints(userAttempts)
                flag = True
            else:
                print("Your answer is incorrect.")
                userAttempts = userAttempts + 1  
        print(f"You got {pointsAwarded} points.")
    except IndexError:
        print("That is not an available number.")

main()