def is_present(list, num):
    """
    function returns true or false if given number is present in given list
    :param list: list
    :param num: number to find in the list
    :return: ture or false
    """
    for x in list:
        if num == x:
            return True
    return False
list_1=[1, 5, 8, 3]
list_2=[5, 8, 3]
print("3 is present in the ",list_1,"list?=",is_present(list_1,3))
print("-1 is present in the ",list_2,"list?=",is_present(list_2,-1))