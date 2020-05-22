import time
from camera import Camera

def contrast_test():
    cam = Camera()
    cam.update_resolution(1280, 720)
    cam.reset_params_to_default()

    # Start the camera display on another thread.
    cam.start_cam_thread()

    # Change the contrast values for camera.
    # TODO: Automatically get supported contrast values and test them here.
    # For now, get the contrast values for your camera through:
    # v4l2-ctl -d /dev/video0 --list-ctrls
    # Specify these parameter values

    # contrast:
    # Range 0 --> 64
    # default 32
    cam.cam_parameter_range_test('contrast', 0, 64, 2, 0)
    time.sleep(5)


if __name__ == '__main__':
    contrast_test()
