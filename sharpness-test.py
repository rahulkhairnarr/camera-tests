import time
from camera import Camera
import threading
import atexit

cam = Camera()
cam.open_cam()
cam.set_default_resolution()

def cleanup():
    cam.reset_params_to_default()

atexit.register(cleanup)

def sharpness_test_thread():
    # Run the sharpness test in a range.:
    sharpness_range = cam.get_params_range('sharpness')
    cam.cam_parameter_range_test(
        'sharpness',
        sharpness_range['min'],
        sharpness_range['max'],
        sharpness_range['step'],
        sharpness_range['default'])

    time.sleep(2)
    print()
    print('- - - - - - - - - - - - - - - - - - - - ')
    print('Press ESC or CTRL+C to Quit.')
    print('- - - - - - - - - - - - - - - - - - - - ')

def sharpness_test():
    _thread = threading.Thread(target=sharpness_test_thread, daemon=True)
    _thread.start()

    cam.show_cam()
    cam.close_cam()

if __name__ == '__main__':
    sharpness_test()
