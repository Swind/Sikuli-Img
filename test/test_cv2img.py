from cv2img import CV2Img
import cv2
from cv2img import Rect


def test_cv2img_load_image_from_file():
    img = CV2Img()
    img.load_file("./screen.png")

    assert img.rows == 1280
    assert img.cols == 768


def test_cv2img_load_image_from_binary():
    img = CV2Img()

    with open("./screen.png", 'rb') as img_file:
        binary = img_file.read()

    img.load_binary(binary)

    assert img.rows == 1280
    assert img.cols == 768


def test_cv2img_load_image_from_base64():
    img = CV2Img()

    with open("./base64-img", 'rb') as img_file:
        base64 = img_file.read()

    img.load_base64(base64)

    assert img.rows == 1280
    assert img.cols == 768


def test_cv2img_operations():
    img = CV2Img()
    img.load_file("./screen.png")

    img2 = CV2Img()
    img2.load_file("./gmail.png")

    assert img.is_same_color() == False
    assert img.is_black() == False
    assert img > img2
    assert (img < img2) == False

    # Resize
    img3 = img.resize(0.5)
    assert img3.rows == 640
    assert img3.cols == 384
    assert img.rows == 1280
    assert img.cols == 768

    # Copy
    img4 = img.copy()
    assert img4.rows == img.rows
    assert img4.cols == img.cols

    # Crop
    roi = Rect(0, 0, 640, 384)
    img5 = img.crop(roi)
    assert img5.rows == 384
    assert img5.cols == 640

    # Invert
    img6 = img.invert()
    assert img6.rows == 1280
    assert img6.cols == 768

    img7 = img6.invert()
    assert img == img7
