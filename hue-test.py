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

def hue_test_thread():
    # Run the hue test in a range.:
    hue_range = cam.get_params_range('hue')
    cam.cam_parameter_range_test(
        'hue',
        hue_range['min'],
        hue_range['max'],
        hue_range['step'],
        hue_range['default'])

    time.sleep(2)
    print()
    print('- - - - - - - - - - - - - - - - - - - - ')
    print('Press ESC or CTRL+C to Quit.')
    print('- - - - - - - - - - - - - - - - - - - - ')

def hue_test():
    _thread = threading.Thread(target=hue_test_thread, daemon=True)
    _thread.start()

    cam.show_cam()
    cam.close_cam()

if __name__ == '__main__':
    hue_test()
