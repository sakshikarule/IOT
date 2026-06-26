from flask import Flask,render_template

app = Flask(__name__)

@app.route('/', methods = ['Get'])
def hompage():
    return render_template("homepage.html")

@app.route('/welcome', methods = ['Get'])
def welcome():
    string = "Home Automation"
    return render_template("welcome.html", mesaage=string)

@app.route('/temperature', methods =['GET'])
def get_temperature():
    temps= [(29.0, "Intrayani"), (28.2, "Nira") (25.8, "Krishna")]
    return render_template("table.html")

@app.route('/temperature',methods = ['POST', 'GET'])
def add_temperature():
    if request.method == 'POST':
    temp = request.form.get('temp')
    loc =  request.form.get('loc')
    print(f"location = {loc}, temperature = {temp}")
    return render_template("form.html")


if __name__ == '__main__':
    app.run(debug=True)