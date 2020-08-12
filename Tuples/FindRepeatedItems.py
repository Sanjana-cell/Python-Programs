#Program find the repeated items of a tuple.

def printsRepeatedItems(demoTuples):
    """
    prints the repeated items in list
    :param demoTuples: tuples
    """
    list_1=[] #empty list to store unique value from tuples
    print("Repeated elements")
    for x in demoTuples:
        #checks if x not in list_1 and ocuurence of x in tuple is more than 2
        if x not in list_1 and demoTuples.count(x) > 1:
            print(x)
            list_1.append(x)

demoList=[] #creates empty list

size=(int(input("Enter the size of the tuples ")))

#loop to add items in list
for i in range(size):
    demoList.append(input("Enter the values "))

tuples_1=tuple(demoList) #coverts list to tuple and then assigns to tuples_1
print(tuples_1)

printsRepeatedItems(tuples_1) #function call