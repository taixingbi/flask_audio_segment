from inaSpeechSegmenter import Segmenter

class inaSpeechSegmenter_cnn:
    def __init__(self):
        print("\ncnn_segs init...")
        self.seg = Segmenter()

    def segs(self, path, file):
        print("\nsegs...")

        segmentation = self.seg(path + file)
        print(segmentation)

        segs=[]
        for seg in segmentation:
            if seg[0]== 'male' or seg[0]== 'female':
                segs.append( [seg[1],  seg[2]])
        print(segs)

        return segs


path = 'data/'
file= 'test.wav'

inaSpeechSegmenter_cnn().segs(path, file)