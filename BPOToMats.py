import csv
import json

data = {}
previousBpo = '0'
fieldnames = ("typeID","BPO","materialTypeID","Mat","quantity")
with open('C:\\Users\\e395953\\Documents\\Eve\\invTypeMaterials.csv','r',encoding='utf-8') as csvfile:
    readCSV = csv.DictReader(csvfile,fieldnames)
    for row in readCSV:
        id = row['typeID']
        if(id != previousBpo):
            data[id]=[]
            data[id].append({
                'BPO':row['BPO'],
                'materialID':row['materialTypeID'],
                'materialName':row['Mat'],
                'quantity':row['quantity']
            })
            previousBpo = row['typeID']
        else:

            data[id].append({
                'BPO':row['BPO'],
                'materialID':row['materialTypeID'],
                'materialName':row['Mat'],
                'quantity':row['quantity']
                })
            previousBpo = row['typeID']
        
        #print(data)
#print(data)
jsonfile = open("C:\\Users\\e395953\\Documents\\Eve\\testing.json",'w')
json.dump(data,jsonfile)
