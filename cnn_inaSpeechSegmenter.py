from inaSpeechSegmenter import Segmenter

class cnn_inaSpeechSegmenter:
    def __init__(self):
        print("\ncnn_segs init...")
        self.seg = Segmenter()
        self.e= .05

    def segmentation(self, path, file):
        print("\nsegs...")

        segmentations = self.seg(path + file)
        # print(segmentation)

        segs=[]
        # for seg in segmentation:
        #     if seg[0]== 'male' or seg[0]== 'female':
        #         segs.append( [seg[1],  seg[2]])
        for seg in segmentations:
            class_seg= "speech" if seg[0]=="male" or seg[0]=="female" else "notSpeech"
            segs.append( [class_seg, int(seg[1]*1000), int(seg[2]*1000)] )

        print(segs)

        return segs

if __name__ == "__main__":
    path = 'data/'
    file= 'test1.wav'

    cnn_inaSpeechSegmenter().segmentation(path, file)  # [('noEnergy', 0.0, 0.4), ('male', 0.4, 3.58)]