import cv2
import numpy as np
import base64

class Rect:
    def __init__(self, x=0, y=0, w=0, h=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

class CV2Img:
    def __init__(self, source=None):
        self._source = source
        self._roi = None

        self._update_source_info()

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self.source = value
        self._update_source_info()

    @property
    def shape(self):
        return self.source.shape

    def _update_source_info(self):
        self.rows, self.cols, _ = self.source.shape
        self._roi = Rect(0, 0, self.rows, self.cols)

        self.mean, self.stddev = cv2.meanStdDev(self.source)

    def load_file(self, file_path):
        # The 1 means return 3-channel color image (without alpha channel)
        self.source = cv2.imread(file_path, 1)

    def load_binary(self, binary):
        buf = np.fromstring(binary, dtype='uint8')

        # The 1 means return 3-channel color image (without alpha channel)
        self.source = cv2.imdecode(buf, cv2.IMREAD_UNCHANGED)

    def load_base64(self, encoded_string):
        self.load_binary(base64.b64decode(encoded_string))

    def is_same_color(self):
        return np.sum(self.stddev[0:4]) <= 1e-5

    def is_black(self):
        return (np.sum(self.mean[0:4]) <= 1e-5) and self.is_same_color()

    def gray(self):
        new_img = CV2Img()
        new_img.source = cv2.cvtColor(self.source, cv2.COLOR_RGB2GRAY)

        return new_img

    def invert(self):
        return CV2Img(cv2.bitwise_not(self.source))

    def crop(self, roi):
        new_img = CV2Img()
        new_img.source = self.source[roi.y:roi.y+roi.h, roi.x:roi.x+roi.w]

        return new_img

    def resize(self, factor):
        h, w, _ = self.source.shape
        new_size = (h/factor, w/factor)
        new_img = CV2Img()
        new_img.source = cv2.resize(self.source, new_size, interpolation=cv2.INTER_NEAREST)

        return new_img

    def copy(self):
        new_img = CV2Img()
        new_img.source = np.copy(self.source)

        return new_img

    #############################################################################
    #
    # Operator
    #
    #############################################################################
    def __lt__(self, other):
        shape = self.source.shape
        other_shape = other.source.shape

        return shape[0] < other_shape[0] or shape[1] < other_shape[1]

    def __gt__(self, other):
        shape = self.source.shape
        other_shape = other.source.shape

        return shape[0] > other_shape[0] or shape[1] > other_shape[1]



