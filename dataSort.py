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

def sortData(conn,tableName,url):

    response = requests.get(url)

    data = {}

    for index in response.json():
        id = index['order_id']
        print("Inputting: " + str(id))
        data[id] = []
        data[id].append({
            'duration':index['duration'],
            'is_buy_order':index['is_buy_order'],
            'issued':index['issued'],
            'location_id':index['location_id'],
            'min_volume':index['min_volume'],
            'price':index['price'],
            'range':index['range'],
            'system_id':index['system_id'],
            'type_id':index['type_id'],
            'volume_remain':index['volume_remain'],
            'volume_total':index['volume_total']
            })
        
        values = (index['order_id'],index['is_buy_order'], index['issued'],index['location_id'],index['min_volume'],
                    index['price'],index['range'],index['system_id'],index['type_id'],
                    index['volume_remain'],index['volume_total'])
        conn.sqlLoadData(values, tableName)

    file = open("D:\\Code\\EveFinance\\buyOrders.json","w")
    jsonString = json.dump(data,file)
    return("Finished Sorting Buys")

def filterSqlData(sql):
            # create table
    createSqlTable("FilteredData")

    archives = sql.crsr.fetchall()
    print("Number of entries: " + len(archives))

    # Iterating over length of archives
    # Grabbing values in indexed row, putting in shit
    for index in len(archives)
        shit = sql.sqlReadData(index, newTable)

            





#---------------------------------------------------------------------------

sql = sqlUpdater.sqlCommands("D:\\Code\\EveFinance\\testing2.db")
sql.createSqlTable("trialBuy")
buyCheck = sortData(sql,"trialBuy","https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility&order_type=buy&page=1&type_id=34")
sql.createSqlTable("trialSell")
sellCheck = sortData(sql,"trialSell","https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility&order_type=sell&page=1&type_id=34")
print(buyCheck)
print(sellCheck)
sql.sqlCloseConnection()
