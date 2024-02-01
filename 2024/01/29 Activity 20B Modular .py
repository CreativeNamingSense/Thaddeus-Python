pi = 3.14

print("Square, Rectangle, Parallelogram, Triangle, Circle")
Shape = str(input("Please input which shape you want to measure: "))
print(Shape.lower())
def Triangle(Height, Base):
    print((Height * Base) / 2)
def Quadilateral(Height, Base):
    print(Height * Base)
def Circle(Radius):
    print(pi * (Radius ** 2))



if (Shape.lower() == "triangle"):
    Height = int(input('Please input the height of the shape: '))
    Base = int(input('Please input the base of the shape: '))
    Triangle(Height,Base)
elif Shape.lower() == "square" or Shape.lower() == "rectangle" or Shape.lower() == "parallelogram":
    Height = int(input('Please input the height of the shape: '))
    Base = int(input('Please input the base of the shape: '))
    Quadilateral(Height, Base)
elif Shape.lower() == "circle":
    Radius = int(input('Please input the radius of the shape: '))
    Circle(Radius)

