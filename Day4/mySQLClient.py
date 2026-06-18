
# import mysql connector
import mysql.connector

# create connection with mysql server
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='Iotfeb26',
    user='sunbeam',
    password='sunbeam'
)

def get_students():
    # create a query
    query = "select * from studinfo;"

    # create a cursor to execute query
    cursor = connection.cursor()

    # execute or pass query to the mysql server
    cursor.execute(query)

    # get data / result from cursor
    data = cursor.fetchall()

    # print data
    print(data)

    # close the cursor
    cursor.close()

def insert_student(name, course, marks,rollno):
    #create a query
    query = f"insert into studinfo values('{name}', {rollno}, {marks}, '{course}');"
    
    # create a cursor to execute query
    cursor = connection.cursor()
    
    # Execute passing both the query and the data
    cursor.execute(query)
    
    # commit your changes to database server
    connection.commit()

    # close the cursor
    cursor.close()

def update_student(rollno, marks):
    # create a query
    query = f"update studinfo set marks={marks} where rollno={rollno};"

    # create a cursor to execute query
    cursor = connection.cursor()

    # execute or pass query to the mysql server
    cursor.execute(query)

    # commit your changes to database server
    connection.commit()

    # close the cursor
    cursor.close()

def delete_student(rollno):
        # create a query
        query = f"delete from studinfo where rollno={rollno};"
    
        # create a cursor to execute query
        cursor = connection.cursor()

        # execute or pass query to the mysql server
        cursor.execute(query)
        
        # commit your changes to database server
        connection.commit()

        # close the cursor
        cursor.close()


insert_student("sakshi", "esd", 81.2, 17)
#update_student(51, 75.5)
#delete_student(51)
get_students()

# close the connection
connection.close()