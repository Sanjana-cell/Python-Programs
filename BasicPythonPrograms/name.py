
def reverseString(fname,lname):
    firstNameReverse=''.join(reversed(fname))
    lastNameReverse=''.join(reversed(lname))
    fullName=firstNameReverse +" "+lastNameReverse
    return fullName

if __name__ == "__main__":
    firstName = input("Enter the first Name ")
    lastName = input("Enter the Last Name ")
    print("Before reversing")
    print(firstName+" "+lastName)
    print("After reversing")
    print(reverseString(firstName,lastName))