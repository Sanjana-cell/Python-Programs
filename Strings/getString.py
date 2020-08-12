#program to get the last part of a string before a specified character

str1 = 'https://www.w3resource.com/python-exercises'
print(str1)
char=input("Enter any character from above string ")
#loop for printing string before charater
for subString in str1.split(char):
    print(subString)
    break
