#### start
```
flask run --host=0.0.0.0 --port=8083
 ```  

#### run
```
python3.7 -m venv myvenv
source myvenv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

http://3.86.17.19:8083/api/segment



{
    "type": "inaSpeechSegmenter", 
    "path": "data/",
    "file": "test.wav"
}


{
    "type": "pyAudioAnalysis", 
    "path": "data/",
    "file": "test.wav"
}



#### threading

https://realpython.com/intro-to-python-threading/


#### MULTITHREADING - PRODUCER AND CONSUMER WITH QUEU
https://www.bogotobogo.com/python/Multithread/python_multithreading_Synchronization_Producer_Consumer_using_Queue.php

eyed3
pydub
scipy
sklearn
hmmlearn
matplotlib
tqdm
plotly

pyAudioAnalysis

tensorflow
inaSpeechSegmenter

