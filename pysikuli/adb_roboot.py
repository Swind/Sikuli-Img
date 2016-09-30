import re

from sh import adb, sed, grep

from .cv2img import CV2Img
from .keycode import ANDROID_KEYCODE
from .robot import Robot

KEYCODE = ANDROID_KEYCODE

class ADBRobot(Robot):

    def send_keys(self, keys):
        for key in keys:
            self.send_key(KEYCODE[key])

    def send_key(self, keycode):
        return adb("shell", "input", "keyevent", keycode)

    def drag_and_drop(self, start_x, start_y, end_x, end_y, duration=None):
        adb("shell", "input", "swipe", start_x, start_y, end_x, end_y, duration)

    def capture_screen(self):
        """
        Use adb shell screencap
        :return: CV2Img
        """
        img = CV2Img()
        result = sed(adb("shell", "screencap", "-p"), 's/\r$//')

        return img.load_binary(result.stdout)

    def tap(self, x, y, duration=None):
        if duration:
            adb("shell", "input", "swipe", x, y, x, y, duration)
        else:
            adb("shell", "input", "tap", x, y)

    @property
    def windows_size(self):
        """
        adb shell dumpsys display | grep mBaseDisplayInfo

        :return:
        """
        #real 1080 X 1920
        real_size_pattern = r"real (\d+) x (\d+),"

        #density 480 (480.0 x 480.0) dpi,
        #density_pattern = re.compile(r"density (\d+) \((\d+.\d+ x \d+.\d+)\) dpi,")

        result = grep(adb("shell", "dumpsys", "display"), "mBaseDisplayInfo").__str__()
        match = re.search(real_size_pattern, result)
        if match:
            size = (int(match.group(1)), int(match.group(2)))
        else:
            size = None

        return size
