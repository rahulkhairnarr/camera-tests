import os
import time
import cv2
import config
import subprocess
import re
import json 
import threading
from datetime import datetime
from singleton_decorator import singleton

@singleton
class Camera(object):
    def __init__(self):
        self.device = config.get_device()
        self.cam = None
        self.window_name = 'Camera'
        self.title = 'Camera Tests'
        self.cam = cv2.VideoCapture(self.device)
        self.window = cv2.namedWindow(self.window_name)
        self._thread = threading.Thread(target=self.show_cam_thread)
        self._thread.daemon = True
        self.save_feed = False
        self.save_file = 'out-{}.avi'.format(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.vid_writer = None

    def open_cam(self):
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        if self.cam is None:
            self.cam = cv2.VideoCapture(self.device)
            self.window = cv2.namedWindow(self.window_name)

            if self.save_feed is True:
                self.vid_writer = cv2.VideoWriter(self.save_file, self.fourcc, 20.0, (640, 480))

    def close_cam(self):
        self.cam.release()
        self.cam = None
        cv2.destroyAllWindows()
        self.window = None

        if self.vid_writer is not None:
            self.vid_writer.release()
            self.vid_writer = None

        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

    def update_title(self, title):
        # Update title within the imshow window.
        self.title = title

    def show_cam_thread(self):
        self.open_cam()
        self.show_cam()
        self.close_cam()

    def start_cam_thread(self):
        print('Starting camera display thread')
        self._thread.start()
        time.sleep(5)

    def get_supported_resolutions(self):
        print('Get supported resolutions')
        # TODO: Get this from v4l2 command dynamically.
        return config.get_supported_resolutions()

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

            # This is needed to keep FPS as a moving average of last 10 frames
            if num_frames % 10 == 0:
                num_frames = 1
                start_time = time.time()

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

                # Print Test Title in the Top left
                title_txt = self.title
                box_size, _ = cv2.getTextSize(title_txt, font, font_size, thickness)
                txt_size = box_size[0]
                txt_loc = (20, 35)
                cv2.putText(frame, title_txt, txt_loc, font, font_size, color, thickness)

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

                # Save feed if that option is set.
                if self.save_feed is True:
                    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                    self.vid_writer.write(hsv)

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

        # Output lines should look like:
        # brightness 0x00980900 (int|bool|menu) : min=x max=x step=1 default=0 value=0 flags=x
        # print('Output of >>>> v4l2-ctl -d {} -l'.format(device))
        # print(res)
        # print('- - - - - - - - -')
        params = {}

        for line in res.splitlines():
            line = line.strip()
            regex = re.compile('(\w+)\s+(0[xX][0-9a-fA-F]+)\s+\((\w+)\)\s+:\s+(.+)')
            match = regex.match(line)
            if match is not None and match.group(1) is not None:
                param_name = match.group(1)
                params[param_name] = {}

                param = {}
                param['hex_code'] = match.group(2)
                param['type'] = match.group(3)
                param['values'] = {}
                
                values_str = match.group(4)
                values = values_str.split(' ')

                for val in values:
                    val = val.strip()
                    val_name = val.split('=')[0]
                    val_val = val.split('=')[1]
                    
                    try:
                        val_val = int(val_val)
                    except:
                        pass

                    param['values'][val_name] = val_val

                params[param_name] = param

        return params

    def set_param(self, name, value):
        # Validate input values.
        params = self.get_params()
        if name not in params.keys():
            print('.... ERROR: Unknown parameter {}'.format(name))
            return False

        # Validate input values for params.
        param_details = params[name]
        if param_details['type'] == 'int' or param_details['type'] == 'menu':
            if value < param_details['values']['min'] or value > param_details['values']['max']:
                print('.... {} should be between {} and {}, default is {}'.format(
                    name,
                    param_details['values']['min'],
                    param_details['values']['max'],
                    param_details['values']['default']))
                return False
        elif param_details['type'] == 'bool':
            if value != 0 or value != 1 or value != True or value != False:
                print('.... {} should be boolean (0 or 1)'.format(name))
                return False
        else:
            print('.... Invalid parameter type for {}'.format(name))
            return False

        # exposure_absolute is only editable if exposure_auto is set to manual (1)
        if name == 'exposure_absolute':
            exposure_auto_val = params['exposure_auto']['values']['value']
            if exposure_auto_val != 1:
                # print('.... exposure_absolute is only editable if exposure_auto is set to manual (1)')
                return False

        # focus_absolute is only editable if focus_auto is set to manual (1)
        if name == 'focus_absolute':
            focus_auto_val = params['focus_auto']['values']['value']
            if focus_auto_val != 1:
                # print('.... focus_absolute is only editable if focus_auto is set to manual (1)')
                return False

        # Construct the v4l2 command to set the parameter.
        cmd = ['v4l2-ctl', '-d', self.device, '--set-ctrl={}={}'.format(name, value)]
        print('.... Command: {}'.format(' '.join(cmd)))
        output = subprocess.check_output(cmd)
        print('.... Done.')
        return True

    def reset_params_to_default(self):
        print('Resetting all params to default.')
        params = self.get_params()
        for key in params.keys():
            param_details = params[key]
            default_value = param_details['values']['default']
            current_value = param_details['values']['value']

            # Exposure absolute default value 78 (though default says 166) (not sure why)
            if key == 'exposure_absolute':
                default_value = 78

            if default_value != current_value:
                print('.. Setting {} to default value {}'.format(key, default_value))
                ret = self.set_param(key, default_value)
                if ret is False:
                    print('.. Error setting parameter {}'.format(key))

        print('Done.')

    def cam_parameter_range_test(self, param, min, max, step, default):
        self.update_title('{} TESTS: {} --> {}, Default: {}'.format(param, min, max, default))
        time.sleep(5)
        for val in range(min, max, step):
            print('Changing {} to: {}'.format(param, val))
            self.update_title('{}: Current {}, Default {}'.format(param.upper(), val, default))
            self.set_param(param, val)
            time.sleep(2)

        print('{} tests complete. Resetting to defaults.')
        self.update_title('{} TEST: Resetting to defaults.'.format(param))
        self.reset_params_to_default()
        time.sleep(5)

def main():
    cam_test = Camera()
    results = cam_test.get_params()
    with open('cam_params.json', 'w') as f:
        json.dump(results, f, indent=2)

    cam_test.set_param('brightness', 30)

    results = cam_test.get_params()
    with open('cam_params2.json', 'w') as f:
        json.dump(results, f, indent=2)

    cam_test.reset_params_to_default()
    print('Done.')

if __name__ == '__main__':
    main()
