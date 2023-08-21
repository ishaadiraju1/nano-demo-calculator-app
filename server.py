from flask import Flask, request, jsonify

app = Flask(__name__)

class Result:
    def __init__(self, value):
        self.value = value

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    numbers = request.json
    response = Result(numbers['first'] + numbers['second'])
    return jsonify(response.value)

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    numbers = request.json
    response = Result(numbers['first'] - numbers['second'])
    return jsonify(response.value)

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')

