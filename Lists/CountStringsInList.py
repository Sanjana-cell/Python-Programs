"""
program to count the number of strings where the string length is 2 or
more and the first and last character are same from a given list of strings
"""
#lists contains strings and integers
wordsList=['abc', 'xyz', 'aba', '1221']
count=0

#loops for all elements in the list
for x in wordsList:

    #checks if each element length is more than 2 and first and last character is same
    if len(x) >= 2 and x[0] == x[-1]:
        count+=1

print(count)
