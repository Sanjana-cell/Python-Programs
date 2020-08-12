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

size=(int(input("Enter the size ")))
myList=[]
for i in range(size):
    try:
        myList.append(int(input("Enter the integer value in list ")))
    except:
        print("Enter only integer values")
        continue

print(myList)
print("Sum elements in the list=",sumOfList(myList))