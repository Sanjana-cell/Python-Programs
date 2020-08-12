
def MaxAndMin(mylist):
    size=len(mylist)
    for i in range(size):
        for j in range(i,size):
            if mylist[j] < mylist[i]:
                temp=mylist[i]
                mylist[i]=mylist[j]
                mylist[j]=temp
    return mylist


setEx=set()
size=(int(input("Enter the size of the size ")))
for i in range(size):
    setEx.add(int(input("Enter the unique elements in set ")))
list_1=list(setEx)
list_1=MaxAndMin(list_1)
setEx=set(list_1)
print(setEx)
print("Maximum element=",list_1[size-1])
print("Minimum element=",list_1[0])