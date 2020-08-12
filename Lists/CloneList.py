#program to clone or copy a list

size=(int(input("Enter the size "))) #stores the size of list
originalList=[] #creates empty lists
copyList=[] #cretes empty lists

#for loop to add element in list , loops until it reaches the size
for i in range(size):
    originalList.append(input("Enter the value in list "))

print("Original List",originalList)
copyList=originalList #assigns the original list to copy list
print("Copy List",copyList)

