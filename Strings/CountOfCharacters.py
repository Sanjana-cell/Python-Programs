# Program to count the number of characters in String

userInput=(input("Enter the String "))
characterCount={} #creates empty string
for x in userInput:
    if x in characterCount:
        characterCount[x]+=1 #update the value
    else:
        characterCount[x] = 1 #addes the value and key

print("The count of characters in given string =",characterCount)