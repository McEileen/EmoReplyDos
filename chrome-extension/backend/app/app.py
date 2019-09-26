from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request, jsonify

app = Flask(__name__)
CORS(app)

@app.route('/responses', methods=['POST'])
@cross_origin(allow_headers=['Content-Type'])
def generate_emoreply():
    input = request.get_json()['input']
    emoreply = "I got this input: " + input
    return jsonify({'response': emoreply}), 200
