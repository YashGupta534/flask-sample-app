from flask import Flask, send_file, render_template
from flask_cors import CORS, cross_origin
import datetime
import logging
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET','POST']) 
@cross_origin()
def index(): 
    log_endpoint("Index - With CORS")
    return render_template('index.html',message="Welcome to Index Page")

@app.route('/info', methods=['GET','POST'])
def info():
    log_endpoint("Info")
    return render_template('info.html',message="Welcome to Info Page")

@app.route('/endpoint/<string:name>', methods=['GET'])
def log_endpoint(name):
    x = datetime.datetime.now()
    # print(f"{x} - {name}")
    with open('endpoint_url.txt', mode='a', encoding='utf-8') as file:
        file.write(f"{x} - {name}\n")
        file.flush()
    return render_template("endpoint.html", message ="Endpoint Logged")

@app.route('/display/<string:name>', methods=['GET'])
def display(name):
    file = open(name, mode='r', encoding='utf-8')
    file_content_str = file.read()
    file_content = file_content_str.split('\n')
    file.close()
    return render_template('display.html',file_content = file_content )

if __name__ == "__main__":
    app.run()
    # app.run(host='0.0.0.0',port=5000)
    # app.run(host='0.0.0.0', port=5000, debug=True )