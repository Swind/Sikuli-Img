from pysikuli.cv2img import CV2Img
from pysikuli.template_finder import TemplateFinder
from .config import IMG_PATH


def _test_template_finder(source_path, target_path, result_len):
    source = CV2Img()
    source.load_file(IMG_PATH(source_path))

    target = CV2Img()
    target.load_file(IMG_PATH(target_path))

    finder = TemplateFinder(source)
    results = finder.find_all(target, 0.9)

    assert len(results) == result_len

    for item in results:
        result = source.crop(item)
        assert result == target


def test_template_finder_find_gmail():
    _test_template_finder(IMG_PATH("screen.png"), IMG_PATH("gmail.png"), 1)

def test_template_finder_find_checkbox():
    _test_template_finder(IMG_PATH("puffin_settings.png"), IMG_PATH("puffin_settings_check.png"), 2)
