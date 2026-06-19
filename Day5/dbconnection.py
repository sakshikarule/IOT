
import mysql.connector

def get_dbconnection():
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='Iotfeb26',
        user='sunbeam',
        password='sunbeam'
    )

    return connection