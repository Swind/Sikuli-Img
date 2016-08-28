from multiscale_template_matching import MultiScaleTemplateMatcher
from cv2img import CV2Img

def test_pyramid_template_matcher():
    source = CV2Img()
    source.load_file("./screen.png")

    target = CV2Img()
    target.load_file("./gmail.png")
    target.resize(0.5)


    matcher = MultiScaleTemplateMatcher(source, target)
    result = matcher.find_best()

    source.draw_result_range(result)
    source.show()


