sample={}
num=(int(input("Enter the size of dictionary")))
for i in range(1,num+1):
    sample.update({i:i*i})

print(sample)