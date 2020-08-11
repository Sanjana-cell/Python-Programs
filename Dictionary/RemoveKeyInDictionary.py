sample={}
num=(int(input("Enter the size of dictionary")))
for i in range(1,num+1):
    sample.update({i:i*i})
print("Before removing the key",sample)
key=(int(input("Enter the key to remove")))
if key in sample:
    del sample[key]
print("After removing the key",sample)
