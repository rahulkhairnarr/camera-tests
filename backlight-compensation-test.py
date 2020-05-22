import time
from camera import Camera

def backlight_compensation_test():
    cam = Camera()
    cam.update_resolution(1280, 720)
    cam.reset_params_to_default()

    # Start the camera display on another thread.
    cam.start_cam_thread()

    # Change the backlight_compensation values for camera.
    # TODO: Automatically get supported backlight_compensation values and test them here.
    # For now, get the backlight_compensation values for your camera through:
    # v4l2-ctl -d /dev/video0 --list-ctrls
    # Specify these parameter values

    # backlight_compensation:
    # Range 0 --> 256
    # default 65
    cam.cam_parameter_range_test('backlight_compensation', 0, 256, 4, 65)
    time.sleep(5)

if __name__ == '__main__':
    backlight_compensation_test()
