import time
from camera import Camera

def hue_test():
    cam = Camera()
    cam.update_resolution(1280, 720)
    cam.reset_params_to_default()

    # Start the camera display on another thread.
    cam.start_cam_thread()

    # Change the hue values for camera.
    # TODO: Automatically get supported hue values and test them here.
    # For now, get the hue values for your camera through:
    # v4l2-ctl -d /dev/video0 --list-ctrls
    # Specify these parameter values

    # hue:
    # Range -2000 --> 2000
    # default 0
    cam.cam_parameter_range_test('hue', -2000, 2000, 50, 0)
    time.sleep(5)

if __name__ == '__main__':
    hue_test()
