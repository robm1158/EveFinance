import sqlite3 as sql
import os.path

# This class maintains all commands to run sql for the dataSort file
class sqlCommands:

    # Upon instantiating the class the intit will setup the connection
    # and cursor for all following sql commands.

    def __init__(self,dataBase):
        self.dataBase = dataBase
        self.connection = sql.connect(self.dataBase)
        self.crsr = self.connection.cursor()
        print("Finished sql Setup: connected to " + self.dataBase)

    # This method will use the class vars to create a table determined by the
    # dataSort file. Modular enough to create any table in the DB that is required

    def createSqlTable(self,tableName):
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
            print("Table Existis Continue")
    
    # This method is used in dataSort to insert puleld esi data
    # into the created DB. Again uses class vars to run commands

    def sqlLoadData(self,values,tableName):
        try:
            command = ''' INSERT INTO ''' + tableName + '''(order_id, is_buy_order, time, location_id, min_volume,
                            price, range, system_id, type_id, volume_remains, volume_total)
                            VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
            self.crsr.execute(command,values)
            self.connection.commit()
        except Exception as e:
            print(str(e))
    
    # This method is used to close the sql connection
    
    def sqlCloseConnection(self):
        try:
            self.connection.close()
            print("Connection closed")
        except:
            print("Could not close connection")




#------------------------------------------------------------------------


