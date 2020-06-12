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

def contrast_test_thread():
    # Run the contrast test in a range.:
    contrast_range = cam.get_params_range('contrast')
    cam.cam_parameter_range_test(
        'contrast',
        contrast_range['min'],
        contrast_range['max'],
        contrast_range['step'],
        contrast_range['default'])

    time.sleep(2)
    print()
    print('- - - - - - - - - - - - - - - - - - - - ')
    print('Press ESC or CTRL+C to Quit.')
    print('- - - - - - - - - - - - - - - - - - - - ')

def contrast_test():
    _thread = threading.Thread(target=contrast_test_thread, daemon=True)
    _thread.start()

    cam.show_cam()
    cam.close_cam()

if __name__ == '__main__':
    contrast_test()
