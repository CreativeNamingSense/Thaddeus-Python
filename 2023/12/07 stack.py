MAX_SIZE = 100 #MAX_SIZE is a constant
Stack = [None for i in range(MAX_SIZE)]  #Stack is a array of 100 elements with data type integer
Top = -1 #Top is an integer variable
operation = 0  #operations is a string variable
Continue = True #Continue is a boolean variable

def IsFull():
    if Top == MAX_SIZE - 1:
        return True
    else:
        return False
    
def IsEmpty():
    if Top == -1:
        return True
    else:
        return False
    
def Push(item):
    if IsFull() == True:
        print("The stack is full. Unable to push new item into stack.")
    else:
        Top = Top + 1
        Stack[Top] = item

def Pop():
    if IsEmpty() == True:
        print("The stack is empty, unable to pop anything.")
    else:
        item = Stack[Top]
        Stack[Top] = None
        Top = Top - 1
    return item

def Peek(): 
    if IsEmpty() == True:
        print("The stack is empty, unable to Peek at anything.")
    else:
        item = Stack[Top]
    return item

while Continue == True:
    operation = int(input("Please input the operation you want to execute:\n1. Pop\n2. Push\n3. Peek\n4. End\n"))

    if operation == 1 :
        print(Pop())
    elif operation == 2:
        item = int(input("Please input the integer to add to the stack :\n"))
        Push(item)
    elif operation == 3:
        print(Peek())
    elif operation == 4: 
        Continue = False
    else:
        print("error")