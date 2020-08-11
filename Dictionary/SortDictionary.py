register = {'vinay': 33, 'sanjana': 24, 'akash': 40, 'arav': 30}

def asecendingOrder(list):
    """
    sorts lists in asecending order returns the sorted list
    :param list: list to be stored
    :return: return sorted list
    """
    for x in range(4):
        for j in range(x,4):
            if list[j] <= list[x]:
                temp=list[x]
                list[x]=list[j]
                list[j]=temp
    return list
def descendingOrder(list):
    """
    sorts lists in descending Order returns the sorted list
    :param list: list to be stored
    :return: return sorted list
    """
    for x in range(4):
        for j in range(x,4):
            if list[j] >= list[x]:
                temp=list[x]
                list[x]=list[j]
                list[j]=temp
    return list
list_1 = list(register.items())
print('Ascending order =',dict(asecendingOrder(list_1)))

list_1 = list(register.items())
print('Descending order =', dict(descendingOrder(list_1)))

