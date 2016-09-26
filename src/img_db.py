import os
import json
from cv2img import CV2Img
from rectangle import Rectangle

class ImgFile:
    def __init__(self, file_path, roi=None):
        self._path = file_path
        self._roi = roi

        dir_path = os.path.dirname(file_path)
        filename, file_extension = os.path.splitext(file_path)

        if os.path.exists(filename + ".json"):
            with open(filename + ".json", "r") as fp:
                self._map = json.loads(fp.read())
        else:
            self._map = None

    def load(self):
        img = CV2Img()
        img.load_file(self.file_path)

        if self._roi:
            img = img.crop(self._roi)

        return img

    def __getattr__(self, item):
        if self._map is None:
            return None

        map_item = map[item]

        if "_roi" in map_item:
            roi = Rectangle(**map_item["_roi"])
        else:
            roi = self._roi

        return ImgFile(self.file_path, roi)


class ImgDB:
    def __init__(self, root_dir):
        self._root = root_dir

    def __getattr__(self, item):
        path = os.path.join(self._root, item)

        if os.path.exists(path):
            if os.path.isdir(path):
                return ImgDB(path)
            elif os.path.isfile(path):
                return ImgFile(path)
