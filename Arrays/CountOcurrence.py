size=(int(input("Enter the size of array ")))
arr=[]
x=size
for x in range(size):
    element=(int(input("Enter the value ")))
    arr.append(element)

def ocurrencesOfElement(array,searchElement):
    """
    return number of ocurrence of an element in array
    :param array: array
    :param searchElement: number to be searched in array
    :return: return the count of element ocurrences
    """
    count = 0
    for x in range(size):
        print(arr[x])
        if searchElement == array[x]:
            count+=1
    return count
number=(int(input("Enter number to be find the ocurrences ")))
print("No of ocurrences of",number,"=",ocurrencesOfElement(arr,number))