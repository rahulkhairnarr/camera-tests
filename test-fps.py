import cv2
import time
import psutil

if __name__ == '__main__':

    # Start default camera
    video = cv2.VideoCapture(0)

    width = 1280
    height = 960

    video.set(3, width)
    video.set(4, height)

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
    for i in range(num_frames):
        ret, frame = video.read()
        cv2.imshow('Video', frame)
        # cv2.imwrite(f'{i}.jpg', frame)
        print(psutil.cpu_percent())

    # End time
    end = time.time()

    # Time elapsed
    seconds = end - start
    print("Time taken : {0} seconds".format(seconds))

    # Calculate frames per second
    fps = num_frames / seconds
    print("Estimated frames per second : {0}".format(fps))

    # Release video
    video.release()
