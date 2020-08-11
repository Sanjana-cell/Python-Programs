import array
size=(int(input("Enter the size of array ")))
arr=[]
x=size
for x in range(size):
    element=(int(input("Enter the value ")))
    arr.append(element)

def removesFirstOcurrencesElement(arr, searchElement):
    """
    remove the first occurrence of a specified element from an array
    :param arr: array
    :param searchElement: number to be searched in array and removed
    """
    count = 0
    for index in range(size):
        if searchElement == arr[index]:
            arr.remove(arr[index])
            break
            
number=(int(input("Enter number to be find the ocurrences ")))
removesFirstOcurrencesElement(arr,number)
print("After removing the element")
newSize=len(arr)
for x in range(newSize):
    print(arr[x])