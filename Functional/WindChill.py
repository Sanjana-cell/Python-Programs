#Program  to calculate temperature (the wind chill)
import math
value=1

class ValueTooSmallError(Exception):
    """Raised when the input value is too small"""
    pass

#Infinite Lopp
while value==1:
    try:
        t=(int(input("Enter the temperature value ")))
        v=(int(input("Enter the wind speed")))
        if t < 0 or v < 0:
            raise ValueTooSmallError
        weather=(35.74+0.6215*t+(0.4275*t-35.75))*v #formula to calculate windChill
        print(pow(weather,0.16))
        break
    except ValueTooSmallError:
        print("Enter the positive numbers")