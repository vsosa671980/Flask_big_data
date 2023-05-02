
import psycopg2 
from connection import Connection

class DbTables():

    def create_products_tables(self):
     try:
        conn = Connection.create_connection()
        sql = """CREATE TABLE IF NOT EXISTS products(
                id SERIAL PRIMARY KEY NOT NULL,
                code varchar(255) NOT NULL,
                description varchar (255) not null,
                price float not null);"""
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        print("Table products created successfully")
     except Exception as e:
        print(f"Error -> ${e}")
     finally:
        if conn is not None:
           conn.close()
           print("Connection closed")