import os
import time
import cv2
import config
import subprocess
import re
from singleton_decorator import singleton

@singleton
class Camera(object):
    def __init__(self):
        self.device = config.get_device()
        self.cam = None
        self.window_name = 'Camera'

    def open_cam(self):
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        self.cam = cv2.VideoCapture(self.device)
        self.window = cv2.namedWindow(self.window_name)

    def close_cam(self):
        self.cam.release()
        self.cam = None
        cv2.destroyAllWindows()
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

    def show_cam(self):
        # Camera must be opened before calling this method.

        # print('- - - - - - - - - - - - - - - - - - - - - - - - - -')
        print('Showing camera: {}'.format(self.device))
        w, h = self.cam.get(cv2.CAP_PROP_FRAME_WIDTH), self.cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print('Resolution: {}x{}'.format(int(w), int(h)))

        start_time = time.time()
        num_frames = 0
        key = None
        while True:
            num_frames += 1

            ret, frame = self.cam.read()
            if ret == -1 or frame is None:
                time.sleep(0.1)
                continue

            try:
                end_time = time.time()
                time_diff = end_time - start_time
                fps = num_frames / time_diff

                font = cv2.FONT_HERSHEY_PLAIN
                font_size = 2
                thickness = 2
                color = (230, 80, 0)

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

        end_time = time.time()
        time_diff = end_time - start_time
        fps = num_frames / time_diff
        print('Camera stopped.')
        print('Total duration: {:.2f} seconds.'.format(time_diff))
        print('FPS: {:.2f} frames per second.'.format(fps))
        if key == 27 or key == ord('q') or key == ord('Q'):
            return True
        else:
            return False
        # print('- - - - - - - - - - - - - - - - - - - - - - - - - -')

    def update_resolution(self, width, height):
        # Cam must be opened before calling this.

        w, h = self.cam.get(cv2.CAP_PROP_FRAME_WIDTH), self.cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print('Current resolution: {}x{}'.format(int(w), int(h)))
        print('Updating resolution to: {}x{}'.format(int(width), int(height)))
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        w, h = self.cam.get(cv2.CAP_PROP_FRAME_WIDTH), self.cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
        if int(width) != int(w) or int(height) != int(h):
            print('ERROR: Unable to update resolution. Resolution defaulted set to: {}x{}'.format(int(w), int(h)))
        else:
            print('Updated resolution to: {}x{}'.format(int(w), int(h)))

    def get_params(self):
        # Get camera parameters through v4l2-ctl
        device = config.get_device()
        res = subprocess.check_output(['v4l2-ctl', '-d', device, '-l']).decode('utf-8')
        # Output should look like:
        # brightness 0x00980900 (int|bool|menu) : min=x max=x step=1 default=0 value=0 flags=x
        print('Output of \n: v4l2-ctl -d {} -l'.format(device))
        print(res)
        print('- - - - - - - - -')
        params = []

        for line in res.splitlines():
            param = {}
            regex = re.compile('\s+(\w+)\s+(0[xX][0-9a-fA-F]+)\s+\((\w+)\)\s+:\s+(.+)')
            match = regex.match(line)
            if match is not None and match.group(0) is not None:
                param_name = match.group(0)
                param[param_name] = {}
                param[param_name]['hex_code'] = match.group(1)
                param[param_name]['type'] = match.group(2)
                param[param_name]['value'] = match.group(3)

                params.append(param)

        return params

def main():
    cam_test = Camera()
    results = cam_test.get_params()
    print(results)

if __name__ == '__main__':
    main()
