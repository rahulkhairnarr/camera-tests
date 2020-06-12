import os
import time
import cv2
import config
import subprocess
import threading
from datetime import datetime
from singleton_decorator import singleton

@singleton
class Camera(object):
    def __init__(self):
        self.device = config.device
        self.cam = None
        self.window_name = 'Camera'
        self.title = 'Camera Tests'
        self.title2 = None
        self.cam = cv2.VideoCapture(self.device)
        self.window = cv2.namedWindow(self.window_name)
        self._thread = threading.Thread(target=self.show_cam_thread)
        self._thread.daemon = True

    def open_cam(self):
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        if self.cam is None:
            self.cam = cv2.VideoCapture(self.device)
            self.window = cv2.namedWindow(self.window_name)

    def close_cam(self):
        if self.cam is not None:
            self.cam.release()
            self.cam = None
            cv2.destroyAllWindows()
            self.window = None
            print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

    def update_title(self, title):
        # Update title within the imshow window.
        self.title = title
        self.title2 = None

    def update_title2(self, title1, title2=None):
        # Update both lines of the title
        self.title = title1
        self.title2 = title2

    def show_cam_thread(self):
        self.open_cam()
        self.show_cam()
        self.close_cam()

    def start_cam_thread(self):
        print('Starting camera display thread')
        self._thread.start()
        time.sleep(5)

    def get_supported_resolutions(self):
        return config.resolutions

    def show_cam(self):
        # Camera must be opened before calling this method.
        if self.cam is None:
            self.open_cam()

        w, h = self.cam.get(cv2.CAP_PROP_FRAME_WIDTH), self.cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print('Showing camera {} at {}x{}'.format(self.device, int(w), int(h)))
        initial_time = time.time()
        total_frames = 0

        start_time = time.time()
        num_frames = 0
        fps = 0.0
        key = None

        while True:
            total_frames += 1
            num_frames += 1

            # This is needed to keep FPS as a moving average of last 10 frames
            if num_frames % 10 == 0:
                end_time = time.time()
                time_diff = end_time - start_time
                fps = num_frames / time_diff
                
                num_frames = 0
                start_time = time.time()

            ret, frame = self.cam.read()
            if ret == -1 or frame is None:
                time.sleep(1)
                continue

            try:

                font = cv2.FONT_HERSHEY_PLAIN
                font_size = 2
                thickness = 2
                color = (80, 230, 0)

                # Print Test Title in the Top left
                title_txt = self.title
                box_size, _ = cv2.getTextSize(title_txt, font, font_size, thickness)
                txt_size = box_size[0]
                txt_loc = (20, 35)
                cv2.putText(frame, title_txt, txt_loc, font, font_size, color, thickness)

                # Print second line of the title in Top Left (if available)
                if self.title2 is not None: 
                    title2_txt = self.title2
                    box_size, _ = cv2.getTextSize(title2_txt, font, font_size, thickness)
                    txt_size = box_size[0]
                    txt_loc = (20, 60)
                    cv2.putText(frame, title2_txt, txt_loc, font, font_size, color, thickness)

                # Print FPS in the bottom right
                fps_txt = 'FPS: {:.2f}'.format(fps)
                box_size, _ = cv2.getTextSize(fps_txt, font, font_size, thickness)
                txt_size = box_size[0]
                txt_loc = (int(w - txt_size - 10), int(h - 20))
                cv2.putText(frame, fps_txt, txt_loc, font, font_size, color, thickness)

                # Print Resolution on top-right
                res_txt = '{}x{}'.format(int(w), int(h))
                box_size, _ = cv2.getTextSize(res_txt, font, font_size, thickness)
                txt_size = box_size[0]
                txt_loc = (int(w - txt_size - 10), int(30))
                cv2.putText(frame, res_txt, txt_loc, font, font_size, color, thickness)

                cv2.imshow(self.window_name, frame)
                key = cv2.waitKey(10)

                # ESC Key
                if key == 27 or key == ord('q') or key == ord('Q'):
                    break

                # Space Key
                elif key == 32:
                    break

                # Any other key
                elif key > 0:
                    break

            except Exception as ex:
                print('Exception: {}'.format(str(ex)))
                pass

        final_time = time.time()
        total_duration = final_time - initial_time
        total_fps = total_frames / total_duration
        print('Camera stopped.')
        print('Total duration: {:.2f} seconds.'.format(final_time - initial_time))
        print('FPS: {:.2f} frames per second.'.format(total_fps))
        if key == 27 or key == ord('q') or key == ord('Q'):
            return True
        else:
            return False

    def update_resolution(self, width, height):
        # Cam must be opened before calling this.

        print('Updating resolution to: {}x{}'.format(int(width), int(height)))
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        w, h = self.cam.get(cv2.CAP_PROP_FRAME_WIDTH), self.cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
        if int(width) == int(w) and int(height) == int(h):
            print('Updated resolution to: {}x{}'.format(int(w), int(h)))
        else:
            print('Error updating resolution. Set to defaults: {}x{}'.format(int(w), int(h)))

    def set_default_resolution(self):
        self.update_resolution(config.default_resolution[0], config.default_resolution[1])

    def get_params_range(self, param):
        if param in config.parameters.keys():
            return config.parameters[param]
        else:
            return None

    def set_param(self, param, val):
        cmd = ['v4l2-ctl', '-d', self.device, '--set-ctrl={}={}'.format(param, val)]
        print('.... Command: {}'.format(' '.join(cmd)))
        try:
            output = subprocess.check_output(cmd)
        except Exception as ex:
            print('Exception during setting parameter. Ignore error. \nCommand {}, Exception: {}.'.format(' '.join(cmd),
                                                                                                          ex))
        print('.... Done.')
        return True

    def reset_params_to_default(self):
        print('Resetting all params to default.')
        for key in config.parameters.keys():
            self.set_param(key, config.parameters[key]['default'])
            time.sleep(0.2)
        print('Done.')

    def cam_parameter_range_test(self, param, min, max, step, default):
        self.update_title2('{} TEST'.format(param),
                '{} --> {}, Default: {}'.format(min, max, default))

        time.sleep(5)
        for val in range(min, max, step):
            print('Changing {} to: {}'.format(param, val))
            self.update_title2('{}: '.format(param.upper()), 'Current {}, Default {}'.format(val, default))
            self.set_param(param, val)
            time.sleep(2)

        print('{} tests complete. Resetting to default.'.format(param.upper()))
        self.update_title2('{} TEST'.format(param.upper()), 'Reset {} to default.'.format(param))
        self.set_param(param, default)
        time.sleep(2)

