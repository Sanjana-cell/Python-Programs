#Program that takes a list of words and returns the length of the longest one


def printLongestWordLength(myList):
    max = len(myList[0])
    for x in myList:
        if len(x) >= max:
            max=len(x)
            maxElement=x
    print("Length of longest word in list", maxElement,"=",max)


size = (int(input("Enter the size of list ")))
wordsList = []
for i in range(size):
    wordsList.append(input("Enter the word "))

printLongestWordLength(wordsList)