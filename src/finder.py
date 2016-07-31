from cv2img import Rect
from pyramid_template_matcher import PyramidTemplateMatcher

DEFAULT_PYRAMID_MIN_TARGET_DIMENSION = 12
DEFAULT_FIND_ALL_MAX_RETURN = 100

CENTER_REMATCH_THRESHOLD = 0.99
BORDER_MARGIN = 0.2

class Finder:
    def __init__(self, source_img):
        self._source_img = None

        self._matcher = None
        self._pyramid_min_target_dimension = DEFAULT_PYRAMID_MIN_TARGET_DIMENSION

        self._resize_ratio_list = [1, 0.75, 0.5, 0.25]

    def find(self, target_img, min_similarity):
        target_rows, target_cols = target_img.shape
        matcher = None

        if target_img > self._source_img:
            return None

        ratio = min(target_img.rows / self._pyramid_min_target_dimension,
                    target_img.cols / self._pyramid_min_target_dimension)

        for resize_ratio in self._resize_ratio_list:
            new_ratio = ratio * resize_ratio

            if new_ratio >= 1:
                matcher = PyramidTemplateMatcher(self._source_img, target_img, 1, new_ratio)
            else:
                return None

