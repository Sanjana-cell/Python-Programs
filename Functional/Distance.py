#Program to calulate Euclidean distance
import math
try:
    x=(int(input("Enter x value ")))
    y=(int(input("Enter y value ")))

    #formula to calculate Euclidean distance
    distane=math.sqrt(x*x + y*y)
    print("Euclidean distance from ",x,"and",y,"=",round(distane,2))
except:
    print("Enter x any y value")
