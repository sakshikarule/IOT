
from flask import Flask, request
from utils.executeequery import execute_query, execute_select_query

server = Flask(__name__)

@server.get('/')
def homepage():
    return "IoT Application - Sensors Log"

@server.route('/sensor', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def sensors_log():
    if request.method == 'GET':
        # get records from database table
        query = "select * from sensorslog;"
        extra = execute_select_query(query=query)
        pass
    elif request.method == 'POST':
        # insert record into database table
        location = request.get_json().get('location')
        tempearture = request.get_json().get('temperature')
        humidity = request.get_json().get('humidity')

        query = f"insert into sensorslog(location, temperature, humidity) values('{location}', {tempearture}, {humidity});"
        execute_query(query=query)
        extra = "Record is inserted successfully"
    elif request.method == 'PUT':
        # upate record into database table
        extra = "Record is updated successfully"
    elif request.method == 'DELETE':
        # delete record into database table
        extra = "Record is deleted successfully"
    
    d = {
        'code':200,
        'msg':'OK',
        'extra':extra
    }

    return d

server.run(debug=True)