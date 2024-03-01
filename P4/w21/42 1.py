def Unknown(X, Y):
    if X < Y:
        print( X+Y )
        return(Unknown(X+1, Y) * 2)
    else:
        if X == Y:
            return 1
        else:
            print( X+Y )
            return (Unknown(X-1, Y) // 2)

print("10 and 15")
print(Unknown(10,15))
print()
print("10 and 10")
print(Unknown(10,10))
print()
print("15 and 10")
print(Unknown(15,10))
print()