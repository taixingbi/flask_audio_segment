from pyAudioAnalysis import audioBasicIO, audioSegmentation

def pyAudioAnalysis_svm(path, file):
    Fs, x= audioBasicIO.read_audio_file( path + file)

    segs = audioSegmentation.silence_removal(x, Fs, 0.020, 0.020, smooth_window = 1.0, weight = 0.3, plot = False)
    print(segs)
    return segs

path = 'data/'
file= 'test.wav'

pyAudioAnalysis_svm(path, file)