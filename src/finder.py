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
        self._roi = None

    def set_roi(self, x, y, w, h):
        self._roi = Rect(x, y, w, h)

    def find(self, target_img, min_similarity):

        if self._roi:
            source_img = self._source_img.crop(self._roi)
        else:
            source_img = self._source_img

        target_rows, target_cols = target_img.shape
        matcher = None

        if target_img > source_img:
            return None

        ratio = min(target_img.rows / self._pyramid_min_target_dimension,
                    target_img.cols / self._pyramid_min_target_dimension)

        result_list = []

        def save_results_and_check(_matcher):
            result_list.extend(_matcher.next(5))
            sorted(result_list, key=lambda item: item.score, reversed=True)

            # Good enough
            if result_list[0] >= max(min_similarity, CENTER_REMATCH_THRESHOLD):
                return True

            return False

        # Step 1: Get the resuls by pyramid template matcher with color
        for resize_ratio in self._resize_ratio_list:
            new_ratio = ratio * resize_ratio

            if new_ratio >= 1:
                matcher = PyramidTemplateMatcher(source_img, target_img, 1, new_ratio)

                # Good enough
                if save_results_and_check(matcher):
                    return

        # Step 2: If the min_similarity is smaller than 0.99 and can't get good result in step 1
        # Use the gray image to search
        if min_similarity < 0.99:
            source_img = source_img.gray()
            target_img = target_img.gray()

            matcher = PyramidTemplateMatcher(source_img, target_img, 0, 1)

            # Good enough
            if save_results_and_check(matcher):
                return

        # Step 3: If

