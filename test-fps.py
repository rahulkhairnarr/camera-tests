import cv2
import time
import psutil

if __name__ == '__main__':

    # Start default camera
    video = cv2.VideoCapture(2)
    print("Updated video resolution. New Reoslution: {}x{}".format(video.get(3), video.get(4)))

    # Find OpenCV version
    # fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
    # print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))

    fps = video.get(cv2.CAP_PROP_FPS)
    print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

    # Number of frames to capture
    num_frames = 120

    print("Capturing {0} frames".format(num_frames))

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
