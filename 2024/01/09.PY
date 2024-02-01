MAXSIZE = 10
Queue = [None for i in (range(MAXSIZE))]
Front = 0
Rear = -1
operation = 0
Continue = True

def IsFull():
    if Front == (Rear % MAXSIZE) - 1:
        return True
    else: 
        return False
    

def IsEmpty():
    if Rear == Front:
        return True
    else:
        return False


def Enqueue(item):
    global Front
    if IsFull() == True:
        print("The queue is full.")
    else:
        
        if Front < MAXSIZE-1:
            Front = Front + 1                
        elif Front == MAXSIZE-1:
            Front = 0 
        Queue[Front] = item
        print(Front)
   
        

def dequeue():
    global Rear
    if IsEmpty() == True:
        item = print("The queue is empty.")
    else:

        if Rear < MAXSIZE - 1:
            Rear = Rear + 1
        elif Rear == MAXSIZE - 1:
            Rear = -1

        item = Queue[Rear]
        Queue[Rear] = None
    return item


for i in range(6):
    Enqueue("hello")
    print(Queue)


for i in range(6):
    dequeue()
    print(Queue)

for i in range(6):
    Enqueue("hello")
    print(Queue)




while Continue == True:
    operation = int(input("Please input the operation you want to execute:\n1. Dequeue\n2. Enqueue\n3. End\n"))

    if operation == 1 :
        print(dequeue())
    elif operation == 2:
        item = int(input("Please input the integer to add to the queue :\n"))
        Enqueue(item)
    elif operation == 3: 
        Continue = False
        print("Thank you for using 'Queue'.")
    else:
        print("error")