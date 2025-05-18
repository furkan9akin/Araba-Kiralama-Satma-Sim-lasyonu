import sqlite3

DATABASE = "Car_Sales.db"


class DB_Manager:
    def __init__(self, database):
        self.database = database

    def executemany(self, sql, data):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.executemany(sql, data)
            conn.commit()

    def __select_data(self, sql, data=tuple()):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute(sql, data)
            return cur.fetchall()

    # def proje_ekle(self, data):
    #     sql = "INSERT INTO projects (project_id, project_name) VALUES (?, ?)"
    #     self.executemany(sql, data)

    def araba_sec(self):
        sql = 'SELECT Company, "Price ($)", Color FROM tablo_adi'
        return self.__select_data(sql)
    
    def tek_par(self, x, y):
        if x=="Company":

            sql = 'SELECT Company, "Price ($)", Color FROM tablo_adi WHERE Company=?'
            return self.__select_data(sql, (y,))
        
        if x=="Price":

            sql = 'SELECT Company, "Price ($)", Color FROM tablo_adi WHERE "Price ($)"<?'
            return self.__select_data(sql, (y,))
        
        if x=="Color":

            sql = 'SELECT Company, "Price ($)", Color FROM tablo_adi WHERE Color=?'
            return self.__select_data(sql, (y,))


# Örnek Kullanım
db_manager = DB_Manager(DATABASE)
sonuc = db_manager.tek_par("Company","Toyota")
for row in sonuc:
    print(row)
    