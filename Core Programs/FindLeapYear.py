#Program to find leap or not

year=(int(input("Enter the year ")))
flag=" "
#checks if input given by user is 4 digit number or not
if year>999 and year<9999:
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                flag="true"
            else:
                flag="false"
        else:
            flag="true"
    else:
        flag="false"
else:
    print("Enter 4 digit number")

if flag == "true":
    print("Leap year")
else:
    print("not a leap year")