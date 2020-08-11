def histogram(list_of_integers):
    """
    function prints the histogram according to the numbers given in list
    :param list_of_integers: list contains integers
    """
    for x in list_of_integers:
        limit=x
        counter=0
        while counter < limit:
            print("+",end=" ")
            counter+=1
        print()

numbers=[1,2,3,4,5,6]
histogram(numbers)