from config import IMG_PATH
from cv2img import CV2Img
from finder.template_finder import Finder


def test_pyramid_template_matcher():
    source = CV2Img()
    source.load_file(IMG_PATH("screen.png"))

    target = CV2Img()
    target.load_file(IMG_PATH("gmail.png"))

    finder = Finder(source)
    result_generator = finder.find(target, 0.9)

    results = list(result_generator)
    assert len(results) == 1
    print(results[0])

    result = source.crop(results[0])
    assert result == target


