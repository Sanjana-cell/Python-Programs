""" program to add 'ing' at the end of a given string (length should be at
least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the
given string is less than 3, leave it unchanged"""

def addSubString(string):
    """
    checks if string length more the or equal to 3 then adds ing at the end of string if ing already present the adds ly at the end
     of the string and returns the string. if string is less than 3 string returned unchanged
    :param string: string
    :return: retrun the updated string with ing or ly
    """
    if len(string) >= 3:
        if string[len(string)-3:len(string)] != "ing": #checks if end of the string contains ing
            string += "ing"
        else:
            string += "ly"
    return string
userInput=(input("Enter a string "))
print(addSubString(userInput))