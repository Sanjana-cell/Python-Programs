#Program to Print the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
num=(int(input("Enter num value ")))
harmonic=1.00
#loop continues till num+1
for i in range(2,num+1):
    harmonic+=1/i

print("Harmonic",round(harmonic,5))