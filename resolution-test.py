import time
from camera import Camera

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

