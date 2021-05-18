import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='dorsia',
                                         user='root',
                                         password='')

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print()
        print("Achieved connection to the database")
        print("Connected to MySQL Server version ", db_Info)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        connection.close()