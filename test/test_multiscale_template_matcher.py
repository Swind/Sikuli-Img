from multiscale_template_matching import MultiScaleTemplateMatcher
from cv2img import CV2Img

def test_multiscale_template_matcher():
    source = CV2Img()
    source.load_file("./screen.png")

    target = CV2Img()
    target.load_file("./gmail.png")
    target = target.resize(0.434)
    target.show()

    matcher = MultiScaleTemplateMatcher(source, target)
    result = matcher.find_best()

    print(result)

    source.draw_result_range(result)
    source.show()


