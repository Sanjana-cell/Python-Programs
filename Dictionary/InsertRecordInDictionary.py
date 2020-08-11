dictonary = {0:43, 1:60}
print("Before update",dictonary)
key=(int(input("Enter the key value ")))
value=(int(input("Enter the value ")))
dictonary.update({key:value})
print("After update",dictonary)