global stackData 
global stackPointer
stackPointer = 0
stackData = [None for i in range(10)]

def outputData():
    print(stackPointer)
    for i in range(10):
        print(stackData[i])

def Push(element):
    global stackPointer
    if stackPointer == 10:
        return False
    else:
        stackData[stackPointer] = element
        stackPointer = stackPointer + 1
        return True

def Pop():
    global stackPointer
    if stackPointer == 0:
        return -1
    else:
        data = stackData[stackPointer - 1]
        stackData[stackPointer - 1] = None
        stackPointer = stackPointer - 1
        return data

    
def main():
    for i in range(11):
        element = int(input("Please input the element to be added: "))
        
        if Push(element) == True:
            print(f"{element} has been added.")
        else:
            print("Stack is full.")        
    outputData()
    
    Pop()
    Pop()
    outputData()
    
    
    
    
main()