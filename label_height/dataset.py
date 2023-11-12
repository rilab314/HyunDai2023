
class Dataset:
    def __init__(self, cfg):
        # list all frames in the dataset
        pass

    def num_frame(self):
        # return number of frames
        pass

    def get_frame(self, index):
        # return image, pcd, label
        pass

    def update_label(self, label):
        # update label file with estimated heights
        pass

