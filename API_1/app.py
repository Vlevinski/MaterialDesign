from flask import Flask, request, jsonify

#try : curl -i -H "Content-Type: application/json" -X POST -d '{"userId":"1", "username": "Name Family"}' http://localhost:5000/foo

app = Flask(__name__)

@app.route('/')
def index():
    return ' Hello World'

@app.route('/foo', methods=['GET','POST'])
def foo():
    data = request.json
    return jsonify(data)

app.run(debug=True)


