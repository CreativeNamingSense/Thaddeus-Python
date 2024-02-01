sortedarray = [1,2,3,4,5,6,7,8,9,10]



'''


import time

def FibSeq(Number):
    if Number < 2:
        return Number
    else:
        return FibSeq(Number - 1) + FibSeq(Number - 2)
    
Number = int(input("Please input the value: "))

st = time.time()
print(FibSeq(Number))
et = time.time()
print(et-st)



'''

#Binary Search


LB = 0
UB = len(sortedarray) - 1

def BinSearch(sortedarray, LB, UB, SE):
    MidPoint = (UB + LB) // 2
    if SE == sortedarray[MidPoint]:
        return MidPoint
    elif UB == LB:
        return -1
    elif SE > sortedarray[MidPoint]:
        LB = MidPoint + 1
        return BinSearch(sortedarray, LB, UB, SE)    
    else:
        UB = MidPoint - 1
        return BinSearch(sortedarray, LB, UB, SE)

SE = int(input("Please input the search element: "))
print(BinSearch(sortedarray, LB, UB, SE))

