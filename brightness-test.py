import time
from camera import Camera

def brightness_test():
    cam = Camera()
    cam.update_resolution(1280, 720)
    cam.reset_params_to_default()

    # Start the camera display on another thread.
    cam.start_cam_thread()

    # Change the brightness values for camera.
    # TODO: Automatically get supported brightness values and test them here.
    # For now, get the brightness values for your camera through:
    # v4l2-ctl -d /dev/video0 --list-ctrls
    # Specify these parameter values

    # Brightness:
    # Range -64 --> 64
    # default 0
    cam.cam_parameter_range_test('brightness', -64, 64, 4, 0)
