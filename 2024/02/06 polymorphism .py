def add(num1 = None, num2= None):
    if num1 == None and num2 == None:
        return num1
    elif num1 == None and num2 != None:
        return num2
    elif num2 == None and num1 != None:
        return num1
    elif num1 != None and num2 != None:
        return num1 + num2
    
print(add())
print(add(None,2))
print(add(3))
print(add(4,5))
