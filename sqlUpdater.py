# Author: Rob Mullins 
# Co-Author: Hunter McCraw
# Purpose: Tool aspect of project
# ---------------------------------

import sqlite3 as sql
import os.path

# This class maintains all commands to run sql for the dataSort file
class sqlCommands:

    # Upon instantiating the class the init will setup the connection
    # and cursor for all following sql commands.

    def __init__(self,dataBase):
        self.dataBase = dataBase
        self.connection = sql.connect(self.dataBase)
        self.crsr = self.connection.cursor()
        print("Finished sql Setup: connected to " + self.dataBase)

    # This method will use the class vars to create a table determined by the
    # dataSort file. Modular enough to create any table in the DB that is required

    def createSqlOrderTable(self,tableName):
        try:
            createTable = """ CREATE TABLE """ + tableName +"""(
                key INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id DOUBLE,
                is_buy_order BOOLEAN,
                time VARCHAR(25),
                location_id DOUBLE,
                min_volume INTEGER,
                price DOUBLE,
                range VARCHAR(15),
                system_id DOUBLE,
                type_id DOUBLE,
                volume_remains DOUBLE,
                volume_total DOUBLE
            );"""
            
            print("Created Table " + tableName)
            self.crsr.execute(createTable)
        except:
            print("Table Exists Continue")
    
    # This method is used in dataSort to insert pulled esi data
    # into the created DB. Again uses class vars to run commands

    def sqlLoadData(self,values,tableName):
        try:
            loadData = ''' INSERT INTO ''' + tableName + '''(order_id, is_buy_order, time, location_id, min_volume,
                            price, range, system_id, type_id, volume_remains, volume_total)
                            VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
            self.crsr.execute(loadData,values)
            self.connection.commit()
        except Exception as e:
            print(str(e))
    
    # This method reads every row of SQL DB
    # Note: 'key' column in DB is only determinant for uniqueness
    def sqlReadData(self,rowIndex,tableName):
        
        try:
            readData = ''' SELECT * FROM ''' + tableName + ''' WHERE key IS ''' + str(rowIndex)
            self.crsr.execute(readData)
            rowData = self.crsr.fetchall()
            return rowData
        except:
            print("Something went wrong")

    # This method is used to close the sql connection
    
    def sqlCloseConnection(self):
        try:
            self.connection.close()
            print("Connection closed")
        except:
            print("Could not close connection")




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
