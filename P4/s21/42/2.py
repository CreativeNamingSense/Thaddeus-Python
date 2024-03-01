arrayData = [10,5,6,7,1,12,13,15,21,8]

def linearSearch(searchElement):
    found = False  
    for index in range (len(arrayData)):
        if arrayData[index] == searchElement:
            found = True
    return found        

def bubbleSort():
    temp = 0  #initializing temp as an integer value
    for X in range(0, 10):
        for Y in range(0, 9):
            if arrayData[Y] < arrayData[Y+1]:
                temp = arrayData[Y]
                arrayData[Y] = arrayData[Y+1]
                arrayData[Y+1] = temp
            

searchElement = int(input("PLease input the search element: "))
found = linearSearch(searchElement)

if found == True:
    print("The value is found.")
elif found == False:
    print("The value is not present in the array.")
    
    