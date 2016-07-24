import cv2
import numpy as np
import base64

DEFAULT_PYRAMID_MIN_TARGET_DIMENSION = 12
DEFAULT_FIND_ALL_MAX_RETURN = 100

PYRAMID_MIN_TARGET_DIMENSION_ALL = 50
CENTER_REMATCH_THRESHOLD = 0.99
BORDER_MARGIN = 0.2

class Finder:
    def __init__(self):
        self._source = None
        self._roi = None

        self._matcher = None
        self._pyramid_min_target_dimension = DEFAULT_PYRAMID_MIN_TARGET_DIMENSION

    def set_roi(self, x, y, w, h):
        self.roi = Rect(x, y, w, h)

    def _init_info(self):
        rows, cols, _ = self._source.shape
        self._roi = Rect(0, 0, rows, cols)

    def find(self, target, min_similarity):
        target_rows, target_cols = target.shape
        pass

if __name__ == "__main__":
    finder = Finder()
    #finder.load_file("./resources/screen.png")

    with open("./resources/base64-img", 'rb')  as img_stream:
        binary = img_stream.read()

    finder.load_base64(binary)

    print("test")

