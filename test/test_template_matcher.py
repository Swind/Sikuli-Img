from config import IMG_PATH

from pysikuli.cv2img import CV2Img
from pysikuli.template_matcher import TemplateMatcher


def test_pyramid_template_matcher():
    source = CV2Img()
    source.load_file(IMG_PATH("screen.png"))

    target = CV2Img()
    target.load_file(IMG_PATH("gmail.png"))

    ratio = min(target.rows / 12, target.cols / 12)

    matcher = TemplateMatcher(source, target, 1, ratio)
    result = matcher.next()
    assert result.score == 1.0

    result_image = source.crop(result)
    assert result_image == target
