MaxSize = 6
Queue = [None for i in range(1,MaxSize)]
FPoint = 1
RPoint = 1


def IsEmpty():
    if FPoint == -1:
        return True
    else:
        return False
    
def IsFull():
    if FPoint == (RPoint % MaxSize):
        return True
    else:
        return False
    

print(IsEmpty())
print(IsFull())