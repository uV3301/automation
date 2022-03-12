# This file is used for calling functions
from Algorithmic_Trading.constants import username,password,screenerlink
from Algorithmic_Trading.Name_and_pricefound import execution_of_orders



instance = execution_of_orders() # I have created a object named instance

instance.login(username,password) #finally login
instance.open_screener()
instance.runscan()
list_stock_urls_chartink,list_of_stock_names,j = instance.list_of_stocks()#Till here we have clicked run scan button and have list of all stocks scanned by screener
print(j)
print(list_stock_urls_chartink)
print(list_of_stock_names)
list_supertrend =instance.supertrend_finder(list_stock_urls_chartink,j)
print(list_supertrend)

