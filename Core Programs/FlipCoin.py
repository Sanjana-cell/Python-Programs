#Program to Flip Coin and print percentage of Heads and Tails
import random
value = 1
totalHeads=0
totalTails=0
percentageOfHeads=0
percentageOfTails=0
#Infinte loop
while value == 1:
    limit=(int(input("Enter the no of times to flip the coin ")))
    if limit >= 1: #checks if limit is more than 1
        counter=0
        #loop continues till counter reaches the limit
        for counter in range(limit):
            result=random.randint(0,1) #generates random numbers
            if result < 0.5:
                print("tails")
                totalTails+=1
            else:
                print("heads")
                totalHeads+=1
        break
    else:
        print("Enter positive number from 1")

percentageOfHeads=totalHeads/limit #cal
percentageOfTails=totalTails/limit
print("Percentage of Heads",percentageOfHeads)
print("Percentage of tails",percentageOfTails)
print("Total Heads ",totalHeads)
print("Total Tails ",totalTails)
