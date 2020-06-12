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

def gamma_test_thread():
    # Run the gamma test in a range.:
    gamma_range = cam.get_params_range('gamma')
    cam.cam_parameter_range_test(
        'gamma',
        gamma_range['min'],
        gamma_range['max'],
        gamma_range['step'],
        gamma_range['default'])

    time.sleep(2)
    print()
    print('- - - - - - - - - - - - - - - - - - - - ')
    print('Press ESC or CTRL+C to Quit.')
    print('- - - - - - - - - - - - - - - - - - - - ')

def gamma_test():
    _thread = threading.Thread(target=gamma_test_thread, daemon=True)
    _thread.start()

    cam.show_cam()
    cam.close_cam()

if __name__ == '__main__':
    gamma_test()
