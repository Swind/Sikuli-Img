from finder import Finder
from cv2img import CV2Img

def test_pyramid_template_matcher():
    source = CV2Img()
    source.load_file("./screen.png")

    target = CV2Img()
    target.load_file("./gmail.png")
    target = target.resize(0.8)

    finder = Finder(source)
    result_generator = finder.find(target, 0.99)

    for result in result_generator:
        print(result)
