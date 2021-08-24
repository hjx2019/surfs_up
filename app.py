from flask import Flask, app

#Create a New Flask App Instance
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'