from flask import Flask, send_file
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET','POST']) 
def index(): 
    log_endpoint("Index")
    return "Index World!"

@app.route('/home', methods=['GET','POST'])
def home():
    log_endpoint("Home")
    return "Home Page"

@app.route('/endpoint/<string:name>', methods=['GET'])
def log_endpoint(name):
    x = datetime.datetime.now()
    print(f"{x} - {name}")
    with open('endpoint_url.txt', mode='a', encoding='utf-8') as file:
        file.write(f"{x} - {name}\n")
    return "Endpoint Logged"

@app.route('/display', methods=['GET'])
def display():
    return send_file('endpoint_url.txt')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000 )