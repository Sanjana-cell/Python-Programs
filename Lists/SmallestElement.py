#program to get the smallest number from a list

myList=[] #creates empty list
def sorting(list):
    """
    return the sorted list, this function sorts the list in ascending order
    :param list: list
    :return: returns the sorted list
    """
    size=len(list)
    for i in range(size):
        for j in range(i,size):
            if list[j] < list[i]:
                temp=list[i]
                list[i]=list[j]
                list[j]=temp
    return list

size=(int(input("Enter the size "))) #stores the size of list

#for loop to add element in list , loops until it reaches the size
for i in range(size):
    try:
        myList.append(int(input("Enter the integer value in list ")))
    except:
        print("Enter only integer values")
        continue
myList=sorting(myList) #function call to sorting and assigns the returned list to myList
print("Minimum element=",myList[0]) #prints minimim element in list