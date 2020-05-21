import config
from singleton_decorator import singleton
from camera import Camera

@singleton
class CameraTests(object):
    def __init__(self):
        self.cam = Camera()

    def test_fps_simple(self):
        self.cam.open_cam()
        exit_prog = self.show_cam()
        self.cam.close_cam()
        if exit_prog is True:
            print('Done.')

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


if __name__ == '__main__':
    cam_tests = CameraTests()
    #cam_tests.test_fps_simple()
    cam_tests.test_fps_iterative()
