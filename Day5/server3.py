#import Flask
from flask import Flask


#create a server
srv = Flask(__name__)

#crete an empty list
temps = list()

@srv.get('/')
def homepage():
    return "This is a homepage"

@srv.get('/temperatures')
def get_temperatures():
    # temps = [28.0,29.2,32.1,22.8,25.8]

    return f"temps = {temps}"

@srv.post('/temperature/<float:temp>') 
def add_temperature(temp):
    #appened recived temp into a list
    temps.append(temp)

    #send msg to the client
    return f"{temp} added"



#run server contionuously
if __name__ == '__main__':
    srv.run(debug=True)
