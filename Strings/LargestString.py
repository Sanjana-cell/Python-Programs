#Program that takes a list of words and returns the length of the longest word in list


def printLongestWordLength(myList):
    """
    prints the length of longest word
    :param myList: list
    """
    max = len(myList[0]) #assigns the length of first element from list
    for x in myList:
        #checks if length x is geater the max
        if len(x) >= max:
            max=len(x)
            maxElement=x
    print("Length of longest word in list", maxElement,"=",max)


size = (int(input("Enter the size of list ")))
wordsList = []
#loop to add elements in list
for i in range(size):
    wordsList.append(input("Enter the word "))

printLongestWordLength(wordsList) #function call