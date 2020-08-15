#Program to Compute the prime factorization of N using brute force

class ValueTooSmallError(Exception):
    """Raised when the input value is too small"""
    pass
try:
    number=(int(input("Enter the number ")))
    if number <= 0:
        raise  ValueTooSmallError
    for i in range(2,number):
        while number%i == 0:
            print(i," ")
            number = number / i
    if number > 2:
        print(number)
except:
    print("Enter only postive integers from 1")