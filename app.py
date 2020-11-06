from flask import Flask, request, render_template
from flask import jsonify

from pyAudioAnalysis_svm import pyAudioAnalysis_svm
from inaSpeechSegmenter_cnn import inaSpeechSegmenter_cnn
import time

app = Flask(__name__)


cnn= inaSpeechSegmenter_cnn()

@app.route('/', methods=['GET'])
def index():
    return "version 1.0"

@app.route('/api/<id>', methods=['GET'])
def api(id):
    print(id)
    data = jsonify(
        id= id,
        segments= [[0.2, 0.9]],
    )

    return data

@app.route('/api/segment', methods=['POST'])
def index_post():
    data= request.json
    print(data)

    type =data['type']
    path =data['path']
    file =data['file']

    segments= None

    st = time.time()

    if type=='cnn':
        segments= cnn.segs(path, file)

    elif type=='svm': 
        segments= pyAudioAnalysis_svm(path, file)

    else:
        segments= 'type is not cnn or svm'

    elapsed = time.time() - st
    print(elapsed)

    data_res = jsonify(
        type= type, # inaSpeechSegmenter
        path= path,
        file= file,
        segments= segments,
        elapsed= elapsed,
    )

    return data_res

# {
# 	"type": "inaSpeechSegmenter", #pyAudioAnalysis
#     "path": "data/",
#     "file": "test.wav"
# }