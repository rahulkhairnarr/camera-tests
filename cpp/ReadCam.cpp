#include "opencv2/opencv.hpp"
#include "iostream"
#include <time.h>
#include <ctime>

using namespace std;

int main(int, char**) {
    int numFrames = 0;
    clock_t start_time, end_time;
    time_t start, end;

    // open the first webcam plugged in the computer
    cv::VideoCapture camera("/dev/video0");
    if (!camera.isOpened()) {
        std::cerr << "ERROR: Could not open camera" << std::endl;
        return 1;
    }

    // create a window to display the images from the webcam
    cv::namedWindow("Webcam", cv::WINDOW_GUI_NORMAL);

    // this will contain the image from the webcam
    cv::Mat frame;
    
    int width, height;
    width = camera.get(cv::CAP_PROP_FRAME_WIDTH);
    height = camera.get(cv::CAP_PROP_FRAME_HEIGHT);
    printf("Resolution: %dx%d\n\n", width, height);

    int w, h;
    w = 1920;
    h = 1080;

    camera.set(cv::CAP_PROP_FRAME_WIDTH, w);
    camera.set(cv::CAP_PROP_FRAME_HEIGHT, h);

    width = camera.get(cv::CAP_PROP_FRAME_WIDTH);
    height = camera.get(cv::CAP_PROP_FRAME_HEIGHT);
    printf("New Resolution: %dx%d\n\n", width, height);

    start_time = clock();
    time(&start);

    // display the frame until you press a key
    while (1) {
        numFrames++;

        // capture the next frame from the webcam
        camera >> frame;

        // show the image on the window
//        cv::imshow("Webcam", frame);
        // wait (10ms) for a key to be pressed
        if (cv::waitKey(10) >= 0)
            break;
    }

    end_time = clock();
    time(&end);

    double time_taken = difftime(end, start);

    double time_diff = double(end_time - start_time)/double(CLOCKS_PER_SEC);
    cout << "Time taken by program is : " << fixed
         << time_diff << setprecision(5);
    cout << " seconds. " << endl;

    printf("Time taken (second method): %f\n", time_taken);

    double fps = numFrames/time_diff;
    cout << "FPS for the camera is : " << fixed
         << fps << setprecision(5);
    cout << " frames per second. " << endl;

    double fps2 = numFrames/time_taken;
    printf("FPS (2nd method): %f\n", fps2); 

    return 0;
}
