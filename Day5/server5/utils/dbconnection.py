
import mysql.connector

def get_dbconnection():
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='Iotfeb26',
        user='sunbeam',
        password='sunbeam'
    )

    return connection