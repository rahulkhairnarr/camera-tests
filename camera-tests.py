import time
import config
import threading
from singleton_decorator import singleton
from camera import Camera

@singleton
class CameraTests(object):
    def __init__(self):
        self.cam = Camera()
        self._thread = threading.Thread(target=self.show_cam_thread)
        self._thread.daemon = True

    def show_cam_thread(self):
        print('Starting cam display on second thread.')
        self.cam.open_cam()
        self.cam.show_cam()
        self.cam.close_cam()

    def test_fps_simple(self):
        self.cam.open_cam()
        self.cam.show_cam()
        self.cam.close_cam()

    def test_fps_iterative(self):
        resolutions = config.get_supported_resolutions()

        for res in resolutions:
            self.cam.open_cam()
            self.cam.update_resolution(res[0], res[1])
            exit_prog = self.cam.show_cam()
            self.cam.close_cam()

            if exit_prog is True:
                print('Exiting program.')
                break

    def test_cam_params(self):
        # Start with 1080p resolution
        self.cam.update_resolution(1280, 720)
        self.cam.reset_params_to_default()

        # Start the camera display on another thread.
        print('Starting camera display thread')
        self._thread.start()
        time.sleep(5)

        # Run different tests for changing camera parameters.

        # Brightness: -64 --> 64, default 0
        self._cam_param_test_num('brightness', -64, 64, 4, 0)

        # Contrast: 0 --> 64, default 32
        self._cam_param_test_num('contrast', 0, 64, 4, 32)

        # Saturation: 0 --> 100, default 40
        self._cam_param_test_num('saturation', 0, 100, 4, 40)

        # Hue: -2000 --> 2000, default 0
        self._cam_param_test_num('hue', -2000, 2000, 200, 0)

        # Gamma: 100 --> 300, default 160
        self._cam_param_test_num('gamma', 100, 300, 10, 160)

        # sharpness: 1 --> 7, default 2
        self._cam_param_test_num('sharpness', 1, 7, 1, 2)

        # backlight_compensation: 0 --> 256, default 65
        self._cam_param_test_num('backlight_compensation', 0, 256, 10, 65)

        # TBD:
        # These need to be set together to take effect.
        # white_balance_temperature_auto & white_balance_temperature
        # focus_auto and focus_absolute
        # exposure_auto and exposure_absolute

    def _cam_param_test_num(self, param, min, max, step, default):
        self.cam.update_title('{} TEST:{} --> {}, Default: {}'.format(param, min, max, default))
        time.sleep(5)
        for val in range(min, max, step):
            print('Changing {} to: {}'.format(param, val))
            self.cam.update_title('{} TEST: Saturation: {} [Default {}]'.format(param, val, default))
            self.cam.set_param(param, val)
            time.sleep(1)

        print('{} tests complete. Resetting to defaults.')
        self.cam.update_title('{} TEST: Resetting to defaults.'.format(param))
        self.cam.reset_params_to_default()
        time.sleep(5)


if __name__ == '__main__':
    cam_tests = CameraTests()
    # cam_tests.test_fps_simple()
    # cam_tests.test_fps_iterative()

    cam_tests.test_cam_params()
