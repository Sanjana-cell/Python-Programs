#Program to sum all the items in a list.

def sumOfList(list):
    """
    returns the sum of all the elements in list
    :param list: list
    :return: retruns the sum of elements
    """
    length=len(list)
    sum=myList[0]
    for i in range(1,length):
        sum=sum+myList[i]
    return sum

size=(int(input("Enter the size "))) #stores the size of list
myList=[] #created empty lists

#for loop to add element in list , loops until it reaches the size
for i in range(size):
    try:
        myList.append(int(input("Enter the integer value in list ")))
    except:
        print("Enter only integer values")
        continue

print(myList)
print("Sum elements in the list=",sumOfList(myList)) #function call and prints the sum of elements