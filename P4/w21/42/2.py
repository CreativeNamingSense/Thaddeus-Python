class Picture:

    def __init__(self, pDescription, pWidth, pHeight, pFrameColour):
        self.__description = pDescription #string
        self.__width = pWidth #integer
        self.__height = pHeight #integer
        self.__frameColour = pFrameColour #string
        
    def GetDescription(self):
       return self.__description
    def GetHeight(self):
        return self.__height
    def GetWidth(self):
        return self.__width
    def GetColour(self):
        return self.__frameColour
    
    def setDescription (self, pDescription):
        self.__description = pDescription
        
myPictures = [] 

for i in range(100):
    myPictures.append(Picture("",0,0,""))

print(myPictures)