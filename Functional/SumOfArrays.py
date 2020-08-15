#Program to count the number of triples that sum to exactly 0

size=(int(input("Enter the size")))
arr=[]
temp=1
#To add elements in array
for i in range(size):
    arr.append(int(input("Enter the value")))
#loop to check whether triplets in array sum to zero
for i in range(size-2):
    for j in range(i+1,size-1):
        for k in range(j+1,size):
            if(arr[i]+arr[j]+arr[k]==0):
                temp=arr[i]+arr[j]+arr[k]
                print(arr[i],arr[j],arr[k],"=",temp)
if temp == 1:
    print("No triplets is present")