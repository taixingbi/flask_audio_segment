from flask import Flask, request, render_template
from flask import jsonify

from pyAudioAnalysis_svm import pyAudioAnalysis_svm
from inaSpeechSegmenter_cnn import inaSpeechSegmenter_cnn


app = Flask(__name__)

@app.route('/api/<id>', methods=['GET'])
def index(id):
    print(id)
    data = jsonify(
        id= id,
        segments= [[0.2, 0.9]],
    )

    return data

@app.route('/api/segment', methods=['POST'])
def index_post():
    content= request.json
    print(content)

    # pyAudioAnalysis_svm(path, file)

    data = jsonify(
        api= "pyAudioAnalysis", # inaSpeechSegmenter
        segments= [[0.2, 0.9]],
    )
    return data

# {
# 	"type": "inaSpeechSegmenter", #pyAudioAnalysis
#     "path": "data/",
#     "file": "test.wav"
# }