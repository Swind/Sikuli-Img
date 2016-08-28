import numpy as np
import cv2
from pyramid_template_matcher import FindResult

class MultiScaleTemplateMatcher:
    def __init__(self, source_img, target_img):
        self.source_img = source_img.gray()
        self.target_img = target_img.gray().canny(50, 200)

    def find_best(self):
        found = None

        for scale in np.linspace(0.2, 1.0, 20)[::-1]:
            # resize the image according to the scale, and keep track
            # of the ratio of the resizing
            r = 1 / scale
            resized_source = self.source_img.resize(scale)

            # if the resized image is smaller than the template, then break
            # from the loop
            if resized_source < self.target_img:
                break

            edged = resized_source.canny(50, 200)
            result = cv2.matchTemplate(edged.source, self.target_img.source, cv2.TM_CCOEFF_NORMED)
            _, maxVal, _, maxLoc = cv2.minMaxLoc(result)
            print(maxVal)
            if found is None or maxVal > found[0]:
                found = (maxVal, maxLoc, r)

        maxVal, maxLoc, r = found

        x, y = maxLoc
        x *= r
        y *= r


        return FindResult(x, y, self.target_img.cols * r, self.target_img.rows * r, maxVal)
