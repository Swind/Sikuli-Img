from multiscale_template_matching import MultiScaleTemplateMatcher
from finder import Finder
from cv2img import CV2Img
from config import IMG_PATH

import pytest
import numpy as np

size_list = np.arange(0.2, 1.0, 0.01)
error = 10 #px

@pytest.mark.parametrize("size", size_list)
def test_multiscale_template_matcher(size):
    source = CV2Img()
    source.load_file(IMG_PATH("screen.png"))

    target = CV2Img()
    target.load_file(IMG_PATH("gmail.png"))

    # Use finder to get the location of target
    finder = Finder(source)
    result_generator = finder.find(target, 0.9)
    result = result_generator.next()
    assert result.score == 1.0

    # Resize the target image and use multiple scale template matcher to find the location
    target = target.resize(size)
    matcher = MultiScaleTemplateMatcher(source, target)
    result2 = matcher.find_best()

    assert result2.x >= result.x - error and result2.x <= result.x + error
    assert result2.y >= result.y - error and result2.y <= result.y + error
    assert result2.w >= result.w - error and result2.w <= result.w + error
    assert result2.h >= result.h - error and result2.h <= result.h + error


