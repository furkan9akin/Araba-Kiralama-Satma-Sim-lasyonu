import sqlite3
import pandas as pd

csv_file = "Car_Sales.csv"  # Dosya adını kendi dosyanla değiştir
df = pd.read_csv(csv_file)

conn = sqlite3.connect("Car_Sales.db") # Aynı dosya adını .db uzantılı şekilde yaz

df.to_sql("tablo_adi", conn, if_exists="replace", index=False) #tablo_adi kısmı değiştirilebilir

conn.close()
