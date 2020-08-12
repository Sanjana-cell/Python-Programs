#Program that takes two lists and returns True if they have at least one common members
sampleList1=[]
sampleList2=[]
def intersectionOfLists(list1,list2):
    """
    function returns true if two list have atleast one common members
    :param list1: list 1
    :param list2: list 2
    :return: return true or false
    """
    result=False
    for x in list1:
        for y in list2:
            #checks if x any y are same if it is same then assigns result to true and then loop breaks
            if x == y:
                result=True
                break
    return result

def CreateList(myList):
    size=(int(input("Enter the size of list ")))
    for i in range(size):
        myList.append(input("Enter the value "))
    return myList

sampleList1=list(CreateList(sampleList1))
sampleList2=list(CreateList(sampleList2))
print("Both list have one atleast common member in list ?",intersectionOfLists(sampleList1,sampleList2))