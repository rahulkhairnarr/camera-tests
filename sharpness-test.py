import time
from camera import Camera

def sharpness_test():
    cam = Camera()
    cam.update_resolution(1280, 720)
    cam.reset_params_to_default()

    # Start the camera display on another thread.
    cam.start_cam_thread()

    # Change the sharpness values for camera.
    # TODO: Automatically get supported sharpness values and test them here.
    # For now, get the sharpness values for your camera through:
    # v4l2-ctl -d /dev/video0 --list-ctrls
    # Specify these parameter values

    # sharpness:
    # Range 0 --> 7
    # default 2
    cam.cam_parameter_range_test('sharpness', 0, 7, 1, 2)
    time.sleep(5)

if __name__ == '__main__':
    sharpness_test()
