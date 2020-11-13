#### start
```
python app.py
 ```  

#### ubuntu install flask
https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-20-04
```
sudo apt update
sudo apt install python3-pip python3-venv
sudo apt install ffmpeg
```

#### run
```
python3 -m venv myvenv
source myvenv/bin/activate
pip install --upgrade pip
pip install wheel
pip install -r requirements.txt
```

http://34.203.38.59:8083/api/segment

{
    "model": "svm", 
    "path": "data/",
    "file": "test.wav"
}


{
    "model": "cnn", 
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


# test
svm  2.92  [[0.06, 1.28]]
cnn  2.9  [['speech', 0, 2900]]
2.9 2.92

# test1
svm  3.6  [[0.36, 3.58]]
cnn  3.58  [['notSpeech', 0, 400], ['speech', 400, 3580]]
3.6 3.6
