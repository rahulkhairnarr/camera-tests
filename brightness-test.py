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

def brightness_test_thread():
    # Run the brightness test in a range.:
    brightness_range = cam.get_params_range('brightness')
    cam.cam_parameter_range_test(
        'brightness',
        brightness_range['min'],
        brightness_range['max'],
        brightness_range['step'],
        brightness_range['default'])

    time.sleep(2)
    print()
    print('- - - - - - - - - - - - - - - - - - - - ')
    print('Press ESC or CTRL+C to Quit.')
    print('- - - - - - - - - - - - - - - - - - - - ')

def brightness_test():
    _thread = threading.Thread(target=brightness_test_thread, daemon=True)
    _thread.start()

    cam.show_cam()
    cam.close_cam()

if __name__ == '__main__':
    brightness_test()
