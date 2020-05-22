import time
import config
from singleton_decorator import singleton
from camera import Camera

@singleton
class CameraTests(object):
    def __init__(self):
        self.cam = Camera()

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
        self.cam.start_cam_thread()

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

        # Change focus to manual focus first.
        # focus_absolute: 0 --> 256, default 0
        self.cam.set_param('focus_auto', 1)
        self._cam_param_test_num('focus_absolute', 0, 256, 10, 0)

        # Change exposure to manual first.
        # exposure_absolute: 3 --> 2047, default 166
        self.cam.set_param('exposure_absolute', 1)
        self._cam_param_test_num('exposure_absolute', 3, 10, 2047, 166)

        # Change wb_temperature_auto to manual first.
        # white_balance_temperature: 3000 --> 6500, default 4600
        self.cam.set_param('white_balance_temperature_auto', 0)
        self._cam_param_test_num('white_balance_temperature', 2800, 6500, 100, 4600)

        # TBD:
        # These need to be set together to take effect.
        # white_balance_temperature_auto & white_balance_temperature
        # focus_auto and focus_absolute
        # exposure_auto and exposure_absolute

    def _cam_param_test_num(self, param, min, max, step, default):
        self.cam.update_title('{} TESTS: {} --> {}, Default: {}'.format(param, min, max, default))
        time.sleep(3)
        for val in range(min, max, step):
            print('Changing {} to: {}'.format(param, val))
            self.cam.update_title('{}: Current {}, Default {}'.format(param.upper(), val, default))
            self.cam.set_param(param, val)
            time.sleep(1)

        print('{} tests complete. Resetting to defaults.')
        self.cam.update_title('{} TEST: Resetting to defaults.'.format(param))
        self.cam.reset_params_to_default()
        time.sleep(3)



if __name__ == '__main__':
    cam_tests = CameraTests()
    # cam_tests.test_fps_simple()
    cam_tests.test_fps_iterative()

