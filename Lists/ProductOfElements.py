#Program to multiply all the items in a list.

def productOfList(list):
    """
    returns the product of all the elements in list
    :param list: list
    :return: retruns the product of elements
    """
    length=len(list)
    product=myList[0]
    for i in range(1,length):
        product=product*myList[i]
    return product

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
print("Product of elements in the list=",productOfList(myList)) #function call and prints the sum of elements