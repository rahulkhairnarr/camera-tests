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

def saturation_test_thread():
    # Run the saturation test in a range.:
    saturation_range = cam.get_params_range('saturation')
    cam.cam_parameter_range_test(
        'saturation',
        saturation_range['min'],
        saturation_range['max'],
        saturation_range['step'],
        saturation_range['default'])

    time.sleep(2)
    print()
    print('- - - - - - - - - - - - - - - - - - - - ')
    print('Press ESC or CTRL+C to Quit.')
    print('- - - - - - - - - - - - - - - - - - - - ')

def saturation_test():
    _thread = threading.Thread(target=saturation_test_thread, daemon=True)
    _thread.start()

    cam.show_cam()
    cam.close_cam()

if __name__ == '__main__':
    saturation_test()
