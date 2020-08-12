#Program to convert first n character to lower case
userInput=input("Enter the String ")
num=(int(input("Enter n value ")))

print(userInput[:num].lower()+userInput[num:]) #converts n charater to lower case and concatenates with other characters