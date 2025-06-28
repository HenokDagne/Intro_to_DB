import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv


def create_database():
    load_dotenv()
    host = os.getenv('HOST')
    user = os.getenv('USER')
    password = os.getenv('PASSWORD')
    # Only check for host, user, and password (not database)
    if not host or not user or not password:
        print("EnvironmentError: Missing database connection parameters")
        return
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")
    except Error as err:
        print(f"Error while connecting to MySQL: {err}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()




