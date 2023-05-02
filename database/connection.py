import psycopg2  


class Connection():
    
    '''Method to pass teh dates of connections'''
    @staticmethod
    def connection_database():
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="postgres"
        )
        return conn

    @classmethod
    def create_connection(cls):
        try:
            conn = cls.connection_database()
            print("Connection to database created successfully")
            return conn
        except Exception as e:
            print(f"Connection error: {e}")
            return None

    @classmethod
    def close_connection(cls, conn):
        if conn is not None:
            conn.close()
            print("Connection closed")

