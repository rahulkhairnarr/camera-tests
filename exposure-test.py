import time
from camera import Camera

def exposure_test():
    cam = Camera()
    cam.update_resolution(1280, 720)
    cam.reset_params_to_default()

    # Start the camera display on another thread.
    cam.start_cam_thread()

    # Change the exposure values for camera.
    # TODO: Automatically get supported exposure values and test them here.
    # For now, get the exposure values for your camera through:
    # v4l2-ctl -d /dev/video0 --list-ctrls
    # Specify these parameter values

    # exposure:
    # Range 3 --> 2047
    # default 166
    # To change exposure, we should have exposure_auto set in manual mode (1)
    cam.set_param('exposure_auto', 1)
    cam.cam_parameter_range_test('exposure_absolute', 3, 2047, 20, 166)
    time.sleep(5)

if __name__ == '__main__':
    exposure_test()
