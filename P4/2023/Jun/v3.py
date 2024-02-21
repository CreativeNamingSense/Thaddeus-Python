DataArray = [] #Array of 25 integer


if not IOError:
    Data = open("Data.txt", "r")
    for i in Data:
        DataArray.append(int(i))
    Data.close
else:
    print("File is not found.")



def PrintArray(DataArray):
    output = ""
    for i in range(0,len(DataArray)):
        output = output + str((DataArray[i])) + ' '
    print(output)


PrintArray(DataArray)


def linearsearch(DataArray, SearchElement):
    count = 0
    for i in range(DataArray):
        if DataArray[i] == SearchElement:
            count = count + 1
    return count

