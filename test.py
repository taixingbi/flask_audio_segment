from pyAudioAnalysis import audioBasicIO, audioSegmentation

# class svm_pyAudioAnalysis:
#     def __init__(self):
#         print("\npyAudioAnalysis_svm init...")
#         self.e= .03

#     def segmentation(self, path, file):
#         Fs, x= audioBasicIO.read_audio_file( path + file)

#         segmentations = audioSegmentation.silence_removal(x, Fs, 0.020, 0.020, smooth_window = 1.0, weight = 0.3, plot = False)
#         duration= len(x)/Fs 
#         print(duration)
#         # print(segmentation)
            
#         segs=[]
#         for i, seg in enumerate(segmentations):
#             if seg[0] > self.e: #head
#                 segs.append( [ "notSpeech", int(0), int(seg[0]*1000) ] )

#             segs.append( [ "speech", int(seg[0]*1000), int(seg[1]*1000) ] )

#             if i==len(segmentations)-1 and seg[1] < (duration - self.e) :  # tail
#                 segs.append( [ "notSpeech", int(seg[1]*1000), int(duration*1000) ] )
        
#         print(segs)
#         return segs


def test():
    print("test")