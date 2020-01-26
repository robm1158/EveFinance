import sqlite3 as sql
import os.path

class sqlCommands:

    def __init__(self,dataBase):
        self.dataBase = dataBase
        if os.path.isfile(self.dataBase):
            print("Finished sql Setup: connected to " + self.dataBase)
        else:
            self.connection = sql.connect(self.dataBase)
            self.crsr = self.connection.cursor()
            print("Finished sql Setup: connected to " + self.dataBase)

    def createSqlTable(self):
        try:
            createTable = """ CREATE TABLE buys(
                key int IDENTITY (1,1) NOT NULL PRIMARY KEY,
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
            print("Table Existis Continue")

    def sqlLoadData(self,values):
        command = ''' INSERT into buys(order_id, date, location_id, min_volume,
                        price, range, system_id, type_id, volume_remains, volume_total
                        VALUES(?,?,?,?,?,?,?,?,?,?))'''
        self.crsr.execute(command,values)



#------------------------------------------------------------------------


