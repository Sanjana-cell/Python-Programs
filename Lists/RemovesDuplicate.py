"""
Program to remove duplicates from a list
"""
def removesDuplicates(list):
    """
    this function add unique element in one more list
    :param list:
    :return: returns unique list
    """
    uniqueList=[]
    #loop for all elements in the list
    for x in list:
        #checks if x not in unique list
        if x not in uniqueList:
            uniqueList.append(x)

    return uniqueList

size=(int(input("Enter the size "))) #stores the size of list
myList=[] #created empty lists

#for loop to add element in list , loops until it reaches the size
for i in range(size):
    myList.append(input("Enter the value in list "))

print("Before Removing duplicate values",myList)
myList=removesDuplicates(myList) #function call
print("After Removing duplicate values",myList)

