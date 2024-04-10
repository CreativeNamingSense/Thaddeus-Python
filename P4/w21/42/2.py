class Picture:

    def __init__(self, pDescription, pWidth, pHeight, pFrameColour):
        self.__description = pDescription #string private
        self.__width = pWidth #integer private
        self.__height = pHeight #integer private
        self.__frameColour = pFrameColour #string private
        
    def GetDescription(self):
       return self.__description
    def GetHeight(self):
        return int(self.__height)
    def GetWidth(self):
        return int(self.__width)
    def GetColour(self):
        return self.__frameColour
    
    def setDescription (self, pDescription):
        self.__description = pDescription


def ReadData(myPictures, fileName):
    counter = 0
    try:
        file = open(fileName, "r")
        pdescription = file.readline().strip()
        
        while pdescription != "":            
            pwidth = file.readline().strip()
            pheight = file.readline().strip()
            pframeColour = file.readline().strip()
            myPictures[counter] = Picture(pdescription, pwidth, pheight, pframeColour)
            counter = counter + 1
            pdescription = file.readline().strip()
        file.close()    
    except IOError:
        print("The file was not found.")    
    return counter, myPictures


fileName = "Pictures.txt"        
myPictures = [] 

for i in range(100):
    myPictures.append(Picture("",0,0,""))

counter, myPictures = ReadData(myPictures, fileName)

picColour = str(input("Please input the colour of the picture: "))
picHeight = int(input("Please input the height of the picture: "))
picWidth = int(input("Please input the width of the picture: "))

index = 0
for index in range(counter):
    if picColour.lower() == (myPictures[index].GetColour()).lower() and picHeight >= myPictures[index].GetHeight() and picWidth >= myPictures[index].GetWidth():
        print(myPictures[index].GetDescription())
        print(myPictures[index].GetWidth())
        print(myPictures[index].GetHeight())
    index = index + 1   
    
        

    



