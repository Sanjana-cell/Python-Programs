#Program to take input from the user and displays that input back in upper and lower cases

userInput=input("Enter a String ")
if userInput.islower(): #checks if string is lower case
    print(userInput.upper()) #prints the user input in upper case if above condition is satsified
else:
    print(userInput.lower()) #prints the user input in lower case if above condition is not satsified