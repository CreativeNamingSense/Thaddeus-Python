Llist = [None for i in range(5)]
Lpointer = [1,2,3,4,-1]
Sp = -1
Hp = 0
item = ""

def IsFull():
    if Hp == -1:
        return True
    else:
        return False
    
def SearchItem(item):
    Flag = False
    Index = len(Llist) - 1
    while Flag == False and Index != -1:
        if Llist[Index] == item:
            Flag = True
        else:
            PrevIndex = Index
            Index = Lpointer[Index]
    return Flag, Index, PrevIndex

def DeleteItem(item,Hp):
    Index = Sp
    while Llist[Index] != item and Index != -1:
        PrevIndex = Index
        Index = Lpointer[Index]

    if Index != -1:
        Llist[Index] = None
        Lpointer[PrevIndex] = Lpointer[Index]
        Lpointer[Index] = Hp
        Hp = Index
    else:
        print("Item is not found.")


while IsFull() == False:
    
    item = int(input("Please input a value."))
    tempsp = Sp
    Sp = Hp
    Llist[Sp] = item

    if Hp < len(Llist)-1:
        Hp = Lpointer[Hp]
    elif Hp == len(Llist)-1:
        Hp = -1
    Lpointer[Sp]= tempsp

print(Llist)
item = int(input("Please input a value to search for: "))

print(SearchItem(item))
print(Lpointer)
item = int(input("Please input a value to delete: "))
DeleteItem(item,Hp)
print(Llist)
print(Lpointer)