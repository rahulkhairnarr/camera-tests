import time
from camera import Camera

def saturation_test():
    cam = Camera()
    cam.update_resolution(1280, 720)
    cam.reset_params_to_default()

    # Start the camera display on another thread.
    cam.start_cam_thread()

    # Change the saturation values for camera.
    # TODO: Automatically get supported saturation values and test them here.
    # For now, get the saturation values for your camera through:
    # v4l2-ctl -d /dev/video0 --list-ctrls
    # Specify these parameter values

    # saturation:
    # Range 0 --> 100
    # default 40
    cam.cam_parameter_range_test('saturation', 0, 100, 4, 0)
    time.sleep(5)

if __name__ == '__main__':
    saturation_test()
