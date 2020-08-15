#Program to calculate quadratic equation
import math

a=(int(input("Enter the a value")))
b=(int(input("Enter the b value")))
c=(int(input("Enter the c value")))

delta_1=b*b
delta_2=4*a*c
result=delta_2-delta_1
root_1=(-b + math.sqrt(result))/(2*a) #calculates root 1
root_2=(b + math.sqrt(result))/(2*a) #caluculates root 2
print("Root 1=",root_1)
print("Root 2=",root_2)