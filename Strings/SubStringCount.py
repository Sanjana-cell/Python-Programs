#Program to count occurrences of a substring in a string
userString = input("Enter a string: ")
subString = input("Sub String: ")
count = 0

for i in range(len(userString) - len(subString) + 1):
    if userString[i:i + len(subString)] == subString:
        count += 1

print(count)
