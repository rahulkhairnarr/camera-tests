import time
from camera import Camera

def exposure_test():
    cam = Camera()

    # Enable saving video output
    cam.enable_save_feed()

#    cam.update_resolution(1280, 720)
#    cam.reset_params_to_default()

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
    time.sleep(2)

    rangelist = [3, 10, 20, 40, 60, 70, 80, 90, 100, 120, 140, 160, 180, 200, 300, 400, 600, 800, 1200, 1400, 1600, 2000]

    cam.cam_parameter_range_test_quick('exposure_absolute', 3, 2047, 20, 166, rangelist)
    time.sleep(2)

if __name__ == '__main__':
    exposure_test()
