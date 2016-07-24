import cv2
import numpy as np

class FindResult:
    def __init__(self, x=0, y=0, w=0, h=0, score=-1):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.score = score

class PyramidTemplateMatcher:
    def __init__(self, source_img, target_img, level, factor):
        self.source_img = source_img
        self.target_img = target_img
        self.factor = factor
        self.level = level
        self.lower_pyramid = None

        self._has_matched_result = False

        if self.source_img < self.target_img:
            return

        if level > 0:
            self.lower_pyramid = self._create_small_matcher()

    def _create_small_matcher(self):
        return PyramidTemplateMatcher(
            self.source_img.resize(self.factor),
            self.target_img.resize(self.factor),
            self.level - 1,
            self.factor
        )

    def find_best(self, roi=None):
        source_img = self.source_img
        target_img = self.target_img

        if roi:
            source_img = source_img.crop(roi)

        if target_img.is_same_color():
            if target_img.is_black():
                source_img = source_img.invert()
                target_img = target_img.invert()

            result = cv2.matchTemplate(source_img.source,
                                       target_img.source,
                                       cv2.CV_TM_SQDIFF_NORMED)

            result = np.ones(result.size(), np.float32) - result
        else:
            result = cv2.matchTemplate(source_img.source,
                                       target_img.source,
                                       cv2.CV_TM_CCOEFF_NORMED)

        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)

        return maxVal, maxLoc

    def erase_result(self, x, y, x_margin, y_margin):
        x0 = max(x - x_margin, 0)
        y0 = max(y - y_margin, 0)

        pass

    def next(self):

        if self.source_img < self.target_img:
            return FindResult(0, 0, 0, 0, -1)

        if self.lower_pyramid != None:
            return self._next_from_lower_pyramid()

        detection_score = -1
        detection_loc = None

        if not self._has_matched_result:
            detection_score, detection_loc = self.find_best()
            self._has_matched_result = True
        else:
            _, detection_score, _, detection_loc = cv2.minMaxLoc(self.result)

        x_margin = self.target_img.cols / 3
        y_margin = self.target_img.rows / 3

        self.erase_result(detection_loc.x,
                          detection_loc.y,
                          x_margin,
                          y_margin)

        return FindResult(detection_loc.x,
                          detection_loc.y,
                          self.target_img.cols,
                          self.target_img.rows,
                          detection_score)
