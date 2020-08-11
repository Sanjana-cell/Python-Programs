size=(int(input("Enter the size of array ")))
arr=[]
x=size
for x in range(size):
    element=(int(input("Enter the value ")))
    arr.append(element)
while x >= 0:
    print(arr[x])
    x-=1