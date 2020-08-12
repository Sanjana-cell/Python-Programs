# Program that accepts a comma separated sequence of words as input and prints the unique words in sorted form

userInput=input("Enter the comma seperated words ")
wordsList=[]
#loop for adding elements from comma seperated userInput
for words in userInput.split(','):
    if words not in wordsList: #checks for unique words in userInput
        wordsList.append(words)

#for sorting the list
for i in range(len(wordsList)):
    for j in range(i,len(wordsList)):
        if wordsList[j] <= wordsList[i]:
            temp=wordsList[i]
            wordsList[i]=wordsList[j]
            wordsList[j]=temp

print(wordsList)