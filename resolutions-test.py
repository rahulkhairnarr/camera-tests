import time
from camera import Camera

# How to run:
# python3 resolution-test.py
# It will open a OpenCV window showing current video frame and resolution.
# Hit Space key to test the next supported resolution
# Hit ESC key to exit the program.

def all_resolutions_test():
    cam = Camera()
    resolutions = cam.get_supported_resolutions()
    cam.reset_params_to_default()

    for res in resolutions:
        cam.open_cam()
        cam.update_resolution(res[0], res[1])
        exit_prog = cam.show_cam()
        cam.close_cam()

        if exit_prog is True:
            print('Exiting program.')
            break

if __name__ == '__main__':
    all_resolutions_test()

# Calculated FPS:
# 640x480 - 18fps
# 800x600 - 17fps
# 1024x768 - 15fps
# 1280x720 - 10fps
# 1080x1080 - Does not work.
# 1280x960 - 5fps
# 1600x1200 - 5fps
# 1920x1080 - Does not work.
# 2048x1536 - 3.7fps
# 2592x1944 - 2.2fps
# 3264x2448 - 1.5fps
