import sqlite3 as sql

class sqlCommands:

    def __init__(self,dataBase):
        self.dataBase = dataBase
        connection = sql.connect(self.dataBase)
        self.crsr = connection.cursor()
        print("Finished sql Setup: connected to " + self.dataBase)

    def createSqlTable(self):
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
        self.crsr.execute(createTable)
        print("Created Table")

#------------------------------------------------------------------------
sql = sqlCommands("D:\\Code\\EveFinance\\testing.db")
sql.createSqlTable()

