import os
from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request, jsonify

from emoreply_generator import find_perks_response, read_corpus, build_model, train_model

source_text = os.getcwd() + "/Perks.txt"

app = Flask(__name__)
CORS(app)

print("building the model....")
untrained_model = build_model(source_text)
print("creating the training corpus")
train_corpus = list(read_corpus(source_text))
print("training the model.....")
trained_model = train_model(untrained_model, train_corpus)
print("the model is ready!")

@app.route('/responses', methods=['POST'])
@cross_origin(allow_headers=['Content-Type'])
def generate_emoreply():
    input = request.get_json()['input']
    emoreply = find_perks_response(trained_model, input, train_corpus)
    return jsonify(emoreply), 200
