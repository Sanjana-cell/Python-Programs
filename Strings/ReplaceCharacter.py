"""
Program to get a string from a given string where all occurrences of its
first char have been changed to '$'
"""
userInput=(input("Enter the String "))
def replaceCharacter(userInput):
    """
    it replaces all occurrences of string first char have been changed to '$
    :param userInput: string
    :return: returns changed string
    """
    firstChar=userInput[0] #assigns first character in string
    newString=userInput[1:len(userInput)] # assigns from character 2 to last character of the string to new string
    for i in range(len(newString)):
        if firstChar == newString[i]:
            newString=newString.replace(newString[i],"$")

    newString=firstChar+newString #concatenates firstChar and new String
    return newString
print(replaceCharacter(userInput))

