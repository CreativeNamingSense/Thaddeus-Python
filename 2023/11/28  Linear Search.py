NameArray = ["Ted", "Jason", "Jeff", "Darren", "Steve"]
AgeArray = [20,23,24,50,10]
 
NameSearch = str(input("Please input the name of the person :\n"))
Age = 0
i = 1
while Age == 0:   
    if NameSearch == NameArray[i-1]:
            Age = AgeArray[i-1]
    i = i + 1
 
            
    
if Age > 0:
    print(NameSearch,"'s age is ", Age)
else:
    print(NameSearch, "does not exist.")