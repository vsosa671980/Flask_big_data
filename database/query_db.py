import psycopg2 
from database.connection import Connection

class Querie():
    
    """For Show Products"""
    @staticmethod
    def show_products(self):
        try:
            conn = Connection.create_connection()
            sql = "SELECT * FROM products LIMIT 10;"
            cursor = conn.cursor()
            cursor.execute(sql)
            products = cursor.fetchall()
            for product in products:
                print(product)
        except Exception as e:
            print("e")

    """Insert products into database"""
    @staticmethod
    def insert_product(code, description, price):
        try:
            conn = Connection.create_connection()
            cursor = conn.cursor()
            sql = """INSERT INTO products(code, description, price) 
                    VALUES (%s, %s, %s)"""
            cursor.execute(sql, (code, description, price))
            conn.commit()
            print("Product added successfully")
        except Exception as e:
            print("Failed to add product")
        finally:
            if conn is not None:
                conn.close()
                print("Connection closed")
    
    """Show list of products"""
    @staticmethod      
    def select_product_alls():
        conn = Connection.create_connection()
        sql = """SELECT * FROM products ORDER BY id LIMIT 10"""
        cursor = conn.cursor()
        cursor.execute(sql)
        products = cursor.fetchall()
        print(type(products))
        return products
    """Delete product by id"""
    def delete_products(id):
        conn = Connection.create_connection()
        sql = f"""DELETE from products WHERE id = %s"""
        cursor = conn.cursor()
        cursor.execute(sql,(id,))
        conn.commit()
        
    """Find product by id""" 
    def find_product_by_id(id):
        try:
            conn = Connection.create_connection()
            sql ="SELECT * FROM products WHERE id = %s;"
            cursor = conn.cursor()
            cursor.execute(sql,(id,))
            product = cursor.fetchone()
            print(product)
            return product
        finally:
            conn.close()
        
    """Update Product"""
    def update_product(id,code,description,price):
       try:
           conn = Connection.create_connection()
           sql = """UPDATE products SET 
                  code = %s,
                  description = %s,
                  price = %s
                  WHERE id = %s;"""
           cursor = conn.cursor()
           print(id)
           print(code)
           print(description)
           print(price)
           cursor.execute(sql,(code,description,price,id))
           conn.commit()
       except Exception as e:
           print(f'Error es -> {e}')
    """Find Product by Code"""
    def find_product_by_code(code):
         try:
             conn = Connection.create_connection()
             sql = "SELECT * FROM products WHERE code = %s;"
             cursor = conn.cursor()
             cursor.execute(sql,(code,))
             product =cursor.fetchone()
             return product 
         except Exception as e:
             print(e)        
        


    
