import cv2
import time
import config
import datetime

dev0 = '/dev/video0'
dev1 = '/dev/video1'
dev2 = '/dev/video2'


camera_0_enabled = True
camera_1_enabled = True
camera_2_enabled = True 
image_capture_enabled = False 
display_window_enabled = True 


def test_fps_simple():
    if camera_0_enabled:
        video0 = cv2.VideoCapture(dev0)
    
    if camera_1_enabled:
        video1 = cv2.VideoCapture(dev1)

    if camera_2_enabled:
        video2 = cv2.VideoCapture(dev2)

    # Number of frames to capture
    num_frames = 120
    print("Capturing {0} frames".format(num_frames))

    # Start time
    start = time.time()

    # Grab a few frames
    frame_idx = 0
    while True:
        frame_idx+=1

        if camera_0_enabled:
            ret, frame0 = video0.read()
        
        if camera_1_enabled:
            ret, frame1 = video1.read()

        if camera_2_enabled:
            ret, frame2 = video2.read()

        if frame_idx >= num_frames:
            break

        if display_window_enabled:
            try:
                if camera_0_enabled:
                    cv2.imshow('Camera0', frame0)
                
                if camera_1_enabled:
                    cv2.imshow('Camera1', frame1)

                if camera_2_enabled:
                    cv2.imshow('Camera2', frame2)

                if cv2.waitKey(10) == 27:
                    break  # esc to quit

            except Exception as ex:
                pass

        if image_capture_enabled and frame_idx % 10 == 0:
            if camera_0_enabled:
                cv2.imwrite("0-" + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.jpg', frame0)
            if camera_1_enabled:
                cv2.imwrite("1-" + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.jpg', frame1)
            if camera_2_enabled:
                cv2.imwrite("2-" + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.jpg', frame2)

    # End time
    end = time.time()

    # Time elapsed
    seconds = end - start
    print("Time taken : {:.2f} seconds, Num Frames Captured: {}".format(seconds, num_frames))

    # Calculate frames per second
    fps = num_frames / seconds
    print("Estimated frames per second : {:.2f}".format(fps))

    # Release video
    if camera_0_enabled:
        video0.release()
    
    if camera_1_enabled:
        video1.release()

    if camera_2_enabled:
        video2.release()

if __name__ == '__main__':
    test_fps_simple()
