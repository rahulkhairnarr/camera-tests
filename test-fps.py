#!/usr/bin/env python

import cv2
import time

if __name__ == '__main__':

    # Start default camera
    video = cv2.VideoCapture(2)

    width = 1280
    height = 960

    video.set(3, width)
    video.set(4, height)


    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

    # With webcam get(CV_CAP_PROP_FPS) does not work.
    # Let's see for ourselves.

    # Start time
    start = time.time()

    # Grab a few frames
    num_frames = 0
    while True:
        num_frames+=1

        ret, frame = video.read()

        if num_frames >= 100:
            break

        # try:
        #     cv2.imshow('Test', frame)
        #     if cv2.waitKey(10) == 27:
        #         break  # esc to quit
        # except Exception as ex:
        #     pass

    # End time
    end = time.time()

    # Time elapsed
    seconds = end - start
    print("Time taken : {} seconds, Num Frames: {}".format(seconds, num_frames))

    # Calculate frames per second
    fps = num_frames / seconds
    print("Estimated frames per second : {0}".format(fps))

    # Release video
    video.release()
