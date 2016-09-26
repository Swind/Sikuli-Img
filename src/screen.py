from cv2img import CV2Img
from region import Region

class Screen:
    def __init__(self, robot):
        self._robot = robot

    @property
    def image(self):
        return self._robot.capture_screen()

    @property
    def size(self):
        return self._robot.windows_size

    def click(self, x, y):
        return self._robot.tap(x, y, 0.1)

    def capture(self):
        w, h = self.size
        img = self._robot.capture_screen()
        return Region(0, 0, w, h, img, self)
