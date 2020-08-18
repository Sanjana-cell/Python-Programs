#Program to Calculate the total Price of each items from csv file
import pandas as pd

class Stock:
    csvFilePath=""
    def __init__(self,path):
        self.csvFilePath=path

    def readCSV(self):
        """
        reads csv file and converts contents into data frome
        :return: returns data frame
        """
        #converts csv file content to dataFrame
        stockDetails=pd.read_csv(self.csvFilePath)
        print(stockDetails)
        return stockDetails

    def calucation(self,stockItems):
        """
        calculates the total price of each item
        :param stockItems: data frame
        :return: updates data frame with new colunm total price
        """
        # calculates total Price of each item
        result=stockItems['Price_Per_Kg']*stockItems['Weight']
        #adds new colunm total price
        stockItems['TotalPrice']=result
        print(stockItems)
        return stockItems

    def createNewCSVFile(self,stockData):
        """
        creates new csv file with data frame contents
        :param stockData: data frame
        """
        try:
            #create new csv file from updated dataFrame
            stockData.to_csv('C:/Users/user/PycharmProjects/pythonPrograms/venv/CSV_Files/New_Stock_Details.csv',index=False)
            print("CSV file created succesfully")
        except:
            traceback.print_exception(*sys.exc_info())

csvPath='C:/Users/user/PycharmProjects/pythonPrograms/venv/CSV_Files/Stock.csv'
stock = Stock(csvPath) #object instantiated

stockTable=stock.readCSV() #function call to read csv file and convert into data frame

data=stock.calucation(stockTable) #function call to caluclates total price of the items

stock.createNewCSVFile(data) #function call to create new csv file from updated data frame