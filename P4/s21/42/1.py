class node:
    def __init__(self,myData,myNextNode):
        #data and nextNode are of type integer
        self.data = myData
        self.nextNode = myNextNode
        
    def getData(self):
        return self.data

    def getNode(self):
        return self.nextNode
        
def addNode(linkedList, currentPointer, myemptyList):
    dataToAdd = int(input("Please input the data to add: "))
    global emptyList
    if myemptyList < 0 or myemptyList > 9:
        return False
    else:
        newNode = node(dataToAdd, -1)
        nextFreeNode = linkedList[myemptyList].nextNode
        linkedList[myemptyList] = newNode
        
        previousPointer = 0
        while currentPointer != -1:
            previousPointer = currentPointer
            currentPointer = linkedList[currentPointer].nextNode
        emptyList = linkedList[nextFreeNode].nextNode
        linkedList[previousPointer].nextNode = myemptyList 
        print(emptyList)       
        return True
        
def outputNodes(linkedList, currentPointer):   
    while currentPointer != -1:
        print(linkedList[currentPointer].data)
        currentPointer = linkedList[currentPointer].nextNode #changing the value of the currentPointer to the next node value
     


linkedList = [node(1,1), node(5,4), node(6,7), node(7,-1), node(2,2), 
              node(0,6), node(0,8), node(56,3), node(0,9), node(0,-1)]

startPointer = 0
emptyList = 5

outputNodes(linkedList, startPointer)

     
if addNode(linkedList, startPointer, emptyList) == True:
    print("The value has been added to the list.")
else:
    print("The list is full.")


outputNodes(linkedList, startPointer)
