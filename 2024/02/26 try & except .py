num1 = int(input("Please input the first number: "))
num2 = int(input("Please input the second number: "))

try:
    print(f"The value is: {num1/num2}")
except ZeroDivisionError:
    print("∞")
except TypeError:
    print("Please input an appropriate integer value.")