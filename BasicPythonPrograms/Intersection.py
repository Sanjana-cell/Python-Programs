def difference(color_list_1,color_list_2):
    """
    function to return set containing all the colors from list_1 which are not present in list_2.
    :param color_list_1: list 1
    :param color_list_2: list 2
    :return: returns set
    """
    return  color_list_1.difference(color_list_2)

list_1=set(["White", "Black", "Red"])
list_2=set(["Red","Green"])

print(difference(list_1,list_2))