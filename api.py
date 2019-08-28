from flask import Flask, jsonify, request
import json

import preprocess
import predict

app = Flask(__name__)

@app.route('/ner', methods=['POST'])
def getName():
  input = json.loads(request.data)['text']
  tkn_txt = preprocess.tokenize_text(input)
  while("" in tkn_txt) : 
    tkn_txt.remove("") 
  X = [preprocess.extract_features(preprocess.pos_tagger([tkn_txt])[0])]

  pred = predict.predict_label(X)
  inputArray = input.split(' ')
  respObj = {"data": [{'word': w, 'isName': p} for w,p in zip(inputArray, pred[0])]}
  
  return jsonify(respObj)