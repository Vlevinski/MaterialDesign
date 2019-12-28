from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

app.run(debug=True)
