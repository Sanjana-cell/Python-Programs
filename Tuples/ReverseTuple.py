#program to reverse a tuple.

def reverseTuples(myTuple,size):
    """
    returns reversed tuple
    :param myTuple: tuple
    :return: reversed tuple
    """
    newTuple=()
    newTuple=myTuple[::-1]
    return newTuple

tuple_1=tuple()
list_1=[]
size=(int(input("Enter the size of an tuple ")))
for x in range(size):
    list_1.append(input("Enter the element in tuple "))

tuple_1=tuple(list_1)
print("Before reversing the tuples")
print(tuple_1)
tuple_1=reverseTuples(tuple_1,size) #function call
print("After reversing the tuples")
print(tuple_1)
