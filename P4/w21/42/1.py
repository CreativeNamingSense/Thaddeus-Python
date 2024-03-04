def Unknown(X, Y):  #Recursive function
    
    if X < Y:
        print( X+Y )
        return(Unknown(X+1, Y) * 2)
    else:
        if X == Y:
            return 1
        else:
            print( X+Y )
            return (Unknown(X-1, Y) // 2)


def iterativeUnknown(X, Y):   #iterative function
    
    Total = 1
    while X != Y:
        if X < Y:
            print(X + Y)
            X = X + 1
            Total = Total * 2
        else:
            print(X + Y)
            X = X - 1
            Total = Total // 2
    return Total


print("10 and 15")
print(Unknown(10,15))
print()
print("10 and 10")
print(Unknown(10,10))
print()
print("15 and 10")
print(Unknown(15,10))
print()

print("10 and 15")
print(iterativeUnknown(10,15))
print()
print("10 and 10")
print(iterativeUnknown(10,10))
print()
print("15 and 10")
print(iterativeUnknown(15,10))
print()