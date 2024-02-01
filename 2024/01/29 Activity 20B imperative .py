pi = 3.14

print("Square, Rectangle, Parallelogram, Triangle, Circle")
Shape = str(input("Please input which shape you want to measure: "))

if Shape.lower == "triangle":
    Height = int(input('Please input the height of the shape: '))
    Base = int(input('Please input the base of the shape: '))
    print((Height * Base) / 2)
elif Shape.lower() == "square" or Shape.lower() == "rectangle" or Shape.lower() == "parallelogram":
    Height = int(input('Please input the height of the shape: '))
    Base = int(input('Please input the base of the shape: '))
    print(Height * Base)
elif Shape.lower == "circle":
    Radius = int(input('Please input the radius of the shape: '))
    print(pi * (Radius ** 2))

