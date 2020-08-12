#Program to iteration over sets

setEx=set()
size=(int(input("Enter the size of the size ")))
#loop to insert items in set
for i in range(size):
    setEx.add(int(input("Enter the unique elements in set ")))

print("Printing the set elements")
#loop to iterate over set
for x in setEx:
    print(x,end=' ')