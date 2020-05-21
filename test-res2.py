
import cv2
import time

def test_resolution(w, h):
   capture = cv2.VideoCapture(0)
   num_frames = 0

   size_new = capture.set(cv2.CAP_PROP_FRAME_WIDTH, w), capture.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
   size = capture.get(cv2.CAP_PROP_FRAME_WIDTH), capture.get(cv2.CAP_PROP_FRAME_HEIGHT)

   print(size)

   start = time.time()

   while(True):
       ret, frame = capture.read()
       if num_frames < 60:
           num_frames = num_frames + 1
           cv2.imshow('Test', frame)
           key = cv2.waitKey(10)
           if key == 27:
                break
       else:
           break

   total_time = time.time() - start
   fps = (num_frames / total_time)
   print('Resolution: {}, Total Time: {}, FPS: {:.2f}'.format(size, total_time, fps))

   capture.release()
   cv2.destroyAllWindows()

def run():
    resolutions = [(320, 480), (640, 480), (800, 600), (1280, 720), (1920, 1080)]
    for res in resolutions:
        test_resolution(res[0], res[1])


if __name__ == '__main__':
    run()
