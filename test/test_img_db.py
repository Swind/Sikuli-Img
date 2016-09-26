from img_db import ImgDB
import pytest


def test_img_db():
    db = ImgDB("./resources")
    home = db.browser.home

    img = home.load()
    img.show()

