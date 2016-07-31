from pyramid_template_matcher import PyramidTemplateMatcher
from cv2img import CV2Img

def test_pyramid_template_matcher():
    source = CV2Img()
    source.load_file("./screen.png")

    target = CV2Img()
    target.load_file("./gmail.png")

    ratio = min(target.rows / 12, target.cols / 12)

    matcher = PyramidTemplateMatcher(source, target, 1, ratio)
    for i in range(0, 20):
        result = matcher.next()
        print(result)
