# import Flask
from flask import Flask, request

from dbconnection import get_dbconnection as dbconn

# create a server
server = Flask(__name__)

@server.get('/')
def homepage():
    return "Student Management System"

@server.get('/students')
def get_students():
    # retrieve students data from database table
    conn = dbconn()
    query = "select * from studinfo;"
    cursor = conn.cursor()
    cursor.execute(query)
    studs = cursor.fetchall()
    cursor.close()
    conn.close()

    # return students list in a response
    return f"students = {studs}"

@server.post('/student')
def insert_student():
    # retrieve data from form fields
    name = request.form.get('name')
    rollno = request.form.get('rollno')
    marks = request.form.get('marks')
    course = request.form.get('course')

    # create a query to be executed to insert student
    query = f"insert into studinfo values('{name}', {rollno}, {marks}, '{course}');"

    # get query executed
    conn = dbconn()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
    
    # return response to the client
    return f"Student with rollno {rollno} is added successfully"

@server.route('/student', methods=['PUT'])
def upate_student():
    # retrieve data from form fields
    rollno = request.form.get('rollno')
    marks = request.form.get('marks')

    # create a query to be executed to insert student
    query = f"update studinfo set marks = {marks} where rollno = {rollno};"

    # get query executed
    conn = dbconn()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
    
    # return response to the client
    return f"Student with rollno {rollno} is updated successfully"

@server.route('/student', methods=['DELETE'])
def delete_student():
    # retrieve data from form fields
    rollno = request.form.get('rollno')
  
    # create a query to be executed to insert student
    query = f"delete from studinfo where rollno = {rollno};"

    # get query executed
    conn = dbconn()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
    
    # return response to the client
    return f"Student with rollno {rollno} is deleted successfully"

# run a server
server.run(debug=True)