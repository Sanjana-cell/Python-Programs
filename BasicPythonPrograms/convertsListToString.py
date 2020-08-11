def concatenateList(list):
    """
    function to concatenate list elements and returns as string
    :param list: list
    :return: string
    """
    str1=""
    for x in list:
        str1=str1+str(x)
    return str1
list=["how",11,"are",5]
print(concatenateList(list))
