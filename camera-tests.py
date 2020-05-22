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

        # Brightness: -64 --> 64
        self.cam.update_title('Brightness Tests: from {} --> {}'.format(-64, 64))
        time.sleep(5)
        for val in range(-64, 64, 8):
            print('Changing brghtness to: {}'.format(val))
            self.cam.update_title('TEST: Brightness: {}'.format(val))
            self.cam.set_param('brightness', val)
            time.sleep(1)

        print('Brightness tests complete. Resetting to default')
        self.cam.update_title('TEST: Brightness: DEFAULT')
        self.cam.reset_params_to_default()
        time.sleep(5)

        # Contrast: 0 --> 64
        self.cam.update_title('Contrast Tests: from {} --> {}'.format(0, 64))
        time.sleep(5)
        for val in range(0, 64, 4):
            print('Changing contrast to: {}'.format(val))
            self.cam.update_title('TEST: Contrast: {}'.format(val))
            self.cam.set_param('contrast', val)
            time.sleep(1)

        print('Contrast tests complete. Resetting to default')
        self.cam.update_title('TEST: Contrast: DEFAULT')
        self.cam.reset_params_to_default()
        time.sleep(5)

        # Saturation: 0 --> 100, default 40
        self.cam.update_title('Saturation Tests:{} --> {}, Default: {}'.format(0, 100, 40))
        time.sleep(5)
        for val in range(0, 100, 4):
            print('Changing contrast to: {}'.format(val))
            self.cam.update_title('TEST: Saturation: {}'.format(val))
            self.cam.set_param('saturation', val)
            time.sleep(1)

        print('Saturation tests complete. Resetting to default')
        self.cam.update_title('TEST: Saturation: DEFAULT')
        self.cam.reset_params_to_default()
        time.sleep(5)


if __name__ == '__main__':
    cam_tests = CameraTests()
    # cam_tests.test_fps_simple()
    # cam_tests.test_fps_iterative()

    cam_tests.test_cam_params()
