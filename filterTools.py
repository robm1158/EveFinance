# Author: Rob Mullins
# Co-Author: Hunter McCraw
# Purpose: Running filtering functions on imported data
# Version: 1.0
# --------------------------------------

import json
import requests
import csv
import sys
import sqlUpdater


# Sort data from eve ESI. Takes in an sql connection and ESI url.
# Will create a dictionary/json of data with the order id as the Key
# will then pass data in per order into an sql load function to load 
# into a given data base.
# for /market/{region_id}/orders/
# Ex) https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility&order_type=buy&page=1&type_id=34

def sortData(sql,tableName,url):

    response = requests.get(url)
    data = {}
    for index in response.json():
        id = index['order_id']
        values = (index['order_id'],index['is_buy_order'], index['issued'],index['location_id'],index['min_volume'],
                    index['price'],index['range'],index['system_id'],index['type_id'],
                    index['volume_remain'],index['volume_total'])
        sql.sqlLoadData(values, tableName)

    return("Finished Sorting Buys")

def rowLookUp(sql,rowData,filterTable):
    counter = 0
    sql.crsr.execute("SELECT * FROM "+filterTable)
    archives = sql.crsr.fetchall()
    
    if len(archives) == 0 :
       # values = (index['order_id'],index['is_buy_order'], index['issued'],index['location_id'],index['min_volume'],
       #             index['price'],index['range'],index['system_id'],index['type_id'],
       #             index['volume_remain'],index['volume_total'])
       # conn.sqlLoadData(values, tableName)

    for index in range(len(archives)):
        data = sql.sqlReadData(index + 1, filterTable)
        #if row (data[0] != rowData[0]) || (data[1] != rowData[1])
        # set values like above
        #sql.sqlLoadData()
        #counter = last index value
        #else:
        #log nothing added
        #counter = index


def filterSqlData(sql,table):
    # create table

    if (table == "buy"):   
        sql.crsr.execute("SELECT * FROM trialBuy")
    else:
        sql.crsr.execute("SELECT * FROM trialSell")

    archives = sql.crsr.fetchall()
    print("Number of entries: " + str(len(archives)))

    # Iterating over length of archives
    # Grabbing values in indexed row, putting in shit
    
    for index in range(len(archives)):
        data = sql.sqlReadData(index, "trialBuy")
        print(data)


#---------------------------------------------------------------------------

sql = sqlUpdater.sqlCommands("/home/e395953/Documents/EveFinance/buySell.db")
sql.createSqlOrderTable("FilteredBuyData")
filterSqlData(sql,"buy")
#sql.createSqlOrderTableTable("trialBuy")
#sql.createSqlOrderTableTable("trialSell")
#sellCheck = sortData(sql,"trialSell","https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility&order_type=sell&page=1&type_id=34")

sql.sqlCloseConnection()
