#program to find the list of words that are longer than n from a given list of words

words=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow','1234']
num=(int(input("Enter the n value ")))
#loops for all the elements in list
for x in words:
    #checks if the the elements length is more the n value
    if len(x) > num:
        print(x)