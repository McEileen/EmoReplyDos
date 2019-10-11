import os
from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request, Response

from emoreply_generator import (find_perks_response, create_train_corpus,
                                create_ref_corpus, build_model, train_model)

source_text = os.getcwd() + "/Perks.txt"

app = Flask(__name__)
CORS(app)

print("creating the training corpus")
train_corpus = create_train_corpus(source_text)
print("creating the reference corpus")
ref_corpus = create_ref_corpus(source_text)
print("building the model....")
untrained_model = build_model(train_corpus)
print("training the model.....")
trained_model = train_model(untrained_model, train_corpus)
print("the model is ready!")


@app.route('/responses', methods=['POST'])
@cross_origin(allow_headers=['Content-Type'])
def generate_emoreply():
    input = request.get_json()['input']
    reply = find_perks_response(trained_model, input, train_corpus, ref_corpus)
    response = Response(reply, content_type="application/json; charset=utf-8")
    return response
