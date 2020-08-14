"""
Program: Given N distinct Coupon Numbers, how many random numbers do you
need to generate distinct coupon number? This program simulates this random
process

"""
import random
from Logical import Gambler
class Coupon:
    limit=0

    def __init__(self,limit):
        self.limit=limit


    def getRandom(limit):
        """
        retruns random number from 0 to limit
        :return: returns the random numbers
        """
        return random.randint(0,limit)

    def getCoupon(self):
        """
        function to get new coupon card
        :return: returns no of random numbers generated to get N distinct coupon
        """
        result=0
        couponNumbers = []
        distinct = 0
        noOfRandomNumbers=0
        while distinct < self.limit:
            result=Coupon.getRandom(limit=self.limit)
            noOfRandomNumbers+=1
            if result not in couponNumbers:
                couponNumbers.append(result)
                distinct+=1
        print(couponNumbers)
        return noOfRandomNumbers


class ValueTooSmallError(Exception):
    """Raised when the input value is too small"""
    pass

value=1
while value==1:
    try:
        limit=(int(input("Enter the limit ")))
        if limit <= 0:
            raise ValueTooSmallError #throws the exception
        coupon=Coupon(limit)
        print(coupon.getCoupon(),"Random numbers generated")
        break
    except ValueTooSmallError:
        print("Enter any number ")
