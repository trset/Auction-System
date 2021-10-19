import mysql.connector
from const import *

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123"
)

if db.is_connected():
    db_Info = db.get_server_info()
    print("Connected to MySQL Server version ", db_Info)

cursor = db.cursor(buffered=True)

cursor.execute("SHOW DATABASES")

for x in cursor:
    if DATABASE_NAME in x:
        break
else:
    cursor.execute(f"CREATE DATABASE {DATABASE_NAME}")

cursor.execute(f"USE {DATABASE_NAME}") 

cursor.execute("SHOW TABLES")
for x in cursor:
    if "Products" in x:
        break
else:
    cursor.execute(f"""
    CREATE TABLE Products (
        id int PRIMARY KEY AUTO_INCREMENT,
        title varchar(255) NOT NULL,
        description varchar(255),
        base_price float NOT NULL,
        current_price float NOT NULL,
        bid_deadline varchar(255) NOT NULL,
        customer_id int,
        is_sold boolean default 0
    )""")


cursor.execute("SHOW TABLES")
for x in cursor:
    if "Customers" in x:
        break
else:
    cursor.execute(f"""
    CREATE TABLE Customers (
        id int PRIMARY KEY AUTO_INCREMENT,
        username varchar(255) NOT NULL UNIQUE,  
        password varchar(255) NOT NULL,  
        spent float default 0.0
    )""")


cursor.execute("ALTER TABLE Products ADD FOREIGN KEY(customer_id) REFERENCES Customers(id)")
