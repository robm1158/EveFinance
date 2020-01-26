import json
import requests
import csv
import sys


def sortBuys(url):

    response = requests.get(url)

    data = {}

    for index in response.json():
        id = index['order_id']
        data[id] = []
        data[id].append({
            'duration':index['duration'],
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

    file = open("D:\\Code\\EveFinance\\buyOrders.json","w")
    jsonString = json.dump(data,file)
    return("Finished Sorting Buys")

def sortSells(url):
    response = requests.get(url)

    data = {}

    for index in response.json():
        id = index['order_id']
        data[id] = []
        data[id].append({
            'duration':index['duration'],
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

    file = open("D:\\Code\\EveFinance\\sellOrders.json","w")
    jsonString = json.dump(data,file)
    return("Finished Sorting Sells")





buyCheck = sortBuys("https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility&order_type=buy&page=1&type_id=34")
sellCheck = sortSells("https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility&order_type=sell&page=1&type_id=34")
print(buyCheck)
print(sellCheck)