#Program to take User Input and Replace String Template
import Error
value = 1
class ValueTooSmallError(Exception):
    """Raised when the input value is too small"""
    pass

#Infinte Loop
while value == 1:
    try:
        userInput = input("Enter the String ")
        if len(userInput) < 3:
            raise ValueTooSmallError
        print("Hello", userInput, "How are you??")
        break #Breaks the loop
    except ValueTooSmallError:
        print("Enter more than 3 characters")
