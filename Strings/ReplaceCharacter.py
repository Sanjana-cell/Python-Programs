"""
Program to get a string from a given string where all occurrences of its
first char have been changed to '$'
"""
userInput=(input("Enter the String "))
print("Length of a string",len(userInput))
length=len(userInput)
stringList=[]
newList=[]
def replaceCharacter(userInput):
    str=""
    for x in userInput:
        if x not in stringList and x != "$":
            stringList.append(x)
        else:
            userInput=userInput.replace(x,"$")
            print("from else",userInput)
    print(str)
    return userInput
print(replaceCharacter(userInput))

