""" program to add 'ing' at the end of a given string (length should be at
least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the
given string is less than 3, leave it unchanged"""

def addSubString(string):
    if len(string) >= 3:
        if string[len(string)-3:len(string)] != "ing":
            string += "ing"
        else:
            string += "ly"
    return string
userInput=(input("Enter a string "))
print(addSubString(userInput))