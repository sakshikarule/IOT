#import flask from flask  module
from flask import Flask

#create a server
server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1> This is a homepage <h1>/body></html>"

@server.get('/')
def welcome():
    return "<html><body><h1>  Welcome to IOT is Application <h1>/body></html>"

#run the srever continuosly
server.run(host='0.0.0.0', port=4000, debug=True)


# host='0.0.0.0' - server can be accesed from any machine ina 

