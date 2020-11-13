
from flask import Flask, request, render_template
from flask import jsonify

from svm_pyAudioAnalysis import svm_pyAudioAnalysis
from cnn_inaSpeechSegmenter import cnn_inaSpeechSegmenter

import time

app = Flask(__name__)

# cnn= cnn_inaSpeechSegmenter()

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


@app.route('/api/segment/file', methods=['POST'])
def index_post():
    data= request.json
    print(data)

    model =data['model']
    path =data['path']
    file =data['file']

    segments= []

    st = time.time()

    if model=='cnn':
        try:
            segments= cnn.segmentation(path, file)
        except:
            try:
                segments= svm_pyAudioAnalysis().segmentation(path, file)
            except:
                print(" somethingwrong both seg")

    elif model=='svm': 
        try: 
            segments= svm_pyAudioAnalysis().segmentation(path, file)
        except:
            try: 
                segments= cnn.segmentation(path, file)
            except:
                print(" somethingwrong both seg")

    else:
        segments= 'model is not cnn or svm'

    elapsed = time.time() - st
    print(elapsed)

    data_res = jsonify(
        model= model, # inaSpeechSegmenter
        path= path,
        file= file,
        segments= segments,
        elapsed= elapsed,
    )

    return data_res

app.run(host='0.0.0.0', port='8083', debug=True)





# {
# 	"type": "inaSpeechSegmenter", #pyAudioAnalysis
#     "path": "data/",
#     "file": "test.wav"
# }

