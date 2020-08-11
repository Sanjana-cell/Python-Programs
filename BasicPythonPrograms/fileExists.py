import os.path
def ifFileExists(fileName):
    """
    function to to check whether a file exists.
    :param fileName: name of the file with extension
    :return: return true if file exists or false
    """
    return os.path.isfile(fileName)

name=input("Enter file name with extension ")
print(ifFileExists(name))