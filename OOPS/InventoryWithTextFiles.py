#Program to Calculates the total Price of each items from text files

file1 = open("C:/Users/user/PycharmProjects/pythonPrograms/venv/TextFiles/stock.txt","r")
file_2 = open('C:/Users/user/PycharmProjects/pythonPrograms/venv/TextFiles/newFile.txt','a+')

list1=file1.readlines()
a=[]
itemDictionary=dict()
result=1
#Loop to add each line from file in list as one element
for x in list1:
    a.append(x)

#Loop to iterate list
for z in range(len(a)):
    itemDictionary.clear()
    word = str(a[z]) #Assigns each element to word in string foramt
    result=1
    print(word)

    #Loop to split each word string using space
    for s in word.split(' '):
        temp_2=s.partition(":") #partition s string based ':' delimeter and creats tuple
        if temp_2[2].rstrip("\n").isdigit():
            #Create dictionary with key as temp_2[0] and value as temp_2[2]
            itemDictionary[temp_2[0]]=int(temp_2[2].rstrip("\n"))
        else:
            # Create dictionary with key as temp_2[0] and value as temp_2[2]
            itemDictionary[temp_2[0]] = temp_2[2].rstrip("\n")

        #Loop to split s string and store it in j
        for j in s.split(':'):
            temp = j.rstrip("\n")
            if temp.isdigit() == True:
                result=int(j)*result #calucates the total Price
                if result != int(j):
                    itemDictionary['totalPrice']=result #add result to dictionary

    print(itemDictionary)
    #appends to new file with dictionary contents
    file_2.write(str(itemDictionary))
file1.close()
file_2.close()