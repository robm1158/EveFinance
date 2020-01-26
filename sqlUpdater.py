# Author: Rob Mullins 
# Purpose: Tool aspect of project
import sqlite3 as sql
import os.path

class sqlCommands:

    def __init__(self,dataBase):
        self.dataBase = dataBase
        self.connection = sql.connect(self.dataBase)
        self.crsr = self.connection.cursor()
        print("Finished sql Setup: connected to " + self.dataBase)

    def createSqlTable(self):
        try:
            createTable = """ CREATE TABLE buys(
                key INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id DOUBLE,
                date VARCHAR(25),
                location_id DOUBLE,
                min_volume INTEGER,
                price DOUBLE,
                range VARCHAR(15),
                system_id DOUBLE,
                type_id DOUBLE,
                volume_remains DOUBLE,
                volume_total DOUBLE
            );"""
            
            print("Created Table")
            self.crsr.execute(createTable)
        except:
            print("Table Exists, Continue")

    def sqlLoadData(self,values):
        try:
            loadData = ''' INSERT INTO buys(order_id, date, location_id, min_volume,
                            price, range, system_id, type_id, volume_remains, volume_total)
                            VALUES(?,?,?,?,?,?,?,?,?,?) '''
            self.crsr.execute(loadData,values)
            self.connection.commit()
            print(self.crsr.lastrowid)
        except Exception as e:
            print(str(e))




#------------------------------------------------------------------------

# Hunter
# Step 1: Grab Data from Eve Website [SQL] -> Dump to buySell.db
#    Step 1.1:  Check that the data from this row doesn't already exist in the *filtered* DB
# Step 2: Parse data - look for duplicates [Python >> SQL]
#          if ((orderID_new == orderID_old) && (orderTime_new == orderTime_old)
#               discardNew()
# Step 3: 

# Rob
# Step 1: Pull data from existing sql file << buySell.db >>
# Step 2: push row into new sql file (filtered one) << buySellFiltered.db >>
# Step 3: Go to next row check if same as previously inserted (and all other previous rows) 
#   row if not insert into new if is the same get-rid of it
# Step 4 make sure this can run continuously on the cron job. Ie. must be automated so that
#   a new set of data will go through data already filtered.
#
# Later: Optimize: some how keep track of what value you left off on from the last filter and 
#   start there rather than from the begining
#  
