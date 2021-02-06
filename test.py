import time, json, requests

class step1_1_segs:
    def __init__(self, model, path, audio_name):
        print("\n-------------------pipeline12_generate_segs-------------------", audio_name )
        self.model= model #cnn/ svm
        self.path= path
        self.audio_name= audio_name

    def api_post(self, data):
        # URL= 'http://3.86.17.19:8083/api/segment'
        URL= 'http://127.0.0.1:8091/api/segment'

        jsonData = json.dumps(data)
        print(jsonData)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(  URL,
                            data= jsonData,
                            headers= headers)

        return r

    def call_api_segment(self):
        data_req= {
            "model": self.model, 
            "path": self.path,
            "file": self.audio_name + '.wav'
        }

        time_try_again= 1
        while time_try_again >= 0:
            r= self.api_post(data_req)
            print(r.status_code)
            if r.status_code == 200:
                return r.json()['segments']

            time_try_again= time_try_again -1

        return []

if __name__=="__main__":
    model= "cnn"
    path= "data/"
    file= "test"

    segs= step1_1_segs(model, path, file).call_api_segment()
    print(segs)
