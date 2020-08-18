#Program to Calculate the total Price of each items from data.json
import json

class Inventory :
    filePath=""
    def __init__(self,file):
        self.filePath=file

    def openFile(self):
        """
        opens the json file and converts the json object into dictionary
        :return: returns the dictionary
        """
        try:
            f = open(self.filePath)
            data = dict(json.load(f))
            print("Opened file successfully")
        except:
            traceback.print_exception(*sys.exc_info())
        return data

    def calculation(self,data):
        """
        calculates the total price of each items
        :param data: dictionary
        :return: returns updated dictionary with total price key value
        """
        for sub in data.values():
            for key, ele in sub.items():
                result=ele['price_per_kg']*ele['weight']
                print("Total price of ",key , result)
                ele['totalPrice']=result
        newData=json.dumps(data)
        print(newData)
        print("Calulated the total price of each items")
        return newData

    def createNewFile(self,newDetails):
        """
        creats new json file from the dictionary
        :param newDetails: dictionary
        """
        try:
            with open("C:/Users/user/PycharmProjects/pythonPrograms/venv/JsonFiles/UpdatedInventoryDetail.json", "w") \
                    as outfile:
                outfile.write(newDetails)
                print("Created new file")
        except:
            traceback.print_exception(*sys.exc_info())

path='C:/Users/user/PycharmProjects/pythonPrograms/venv/JsonFiles/data.json'
stock = Inventory(path) #object instantiated
try:
    data=stock.openFile() #function call to open json file
    newData=stock.calculation(data=data) #function call to calculate total price of each items
except:
    traceback.print_exception(*sys.exc_info())

stock.createNewFile(newDetails=newData) #functiona call to create new json file
