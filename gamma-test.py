import time
from camera import Camera

def gamma_test():
    cam = Camera()
    cam.update_resolution(1280, 720)
    cam.reset_params_to_default()

    # Start the camera display on another thread.
    cam.start_cam_thread()

    # Change the gamma values for camera.
    # TODO: Automatically get supported gamma values and test them here.
    # For now, get the gamma values for your camera through:
    # v4l2-ctl -d /dev/video0 --list-ctrls
    # Specify these parameter values

    # gamma:
    # Range 100 --> 300
    # default 160
    cam.cam_parameter_range_test('gamma', 100, 300, 5, 160)
    time.sleep(5)

if __name__ == '__main__':
    gamma_test()
