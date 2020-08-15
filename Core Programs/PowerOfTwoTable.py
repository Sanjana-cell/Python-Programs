#Program to print table of 2^N

exponent=(int(input("Enter the exponent value ")))
BASE=2
result=1
counter=0
print(result,"*",BASE)
#checks if the exponent is in range 0 to 31
if exponent>0 and exponent<31:
    for counter in range(exponent):
        result=result*BASE
        print(result,"*",BASE)
else:
    print("Exponent should be less than 31")