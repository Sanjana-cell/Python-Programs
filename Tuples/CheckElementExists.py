#Program to check whether an element exists within a tuple

def checkElementExists(tuples_1,value):
    """
    returns true if element is present in tuples else return false
    :param tuples_1:
    :param value:
    :return:
    """
    found=False
    for x in tuples_1:
        #checks if x is same as value
        if x == value:
            found=True
    return found

demoList=[] #creates empty list

size=(int(input("Enter the size of the tuples ")))

#loop to add items in list
for i in range(size):
    demoList.append(input("Enter the integers value in list "))

tupleEx=tuple(demoList) #coverts list to tuple and then assigns to tupleEx
print(tupleEx)

searchElement=(input("Enter the element to be searched "))
print("IS ",searchElement,"present in tuples ? ",checkElementExists(tupleEx,searchElement)) #function call and prints the results

