# num1 = int(input("Please input the first number: "))
# num2 = int(input("Please input the second number: "))

# try:
#     print(f"The value is: {num1/num2}")
# except ZeroDivisionError:
#     print("∞")
# except TypeError:
#     print("Please input an appropriate integer value.")


list = [None for i in range(0,10)]
print(list)
try:
    list[0] = int(input("Enter a value: "))
except IndexError:
    print("out of range.")