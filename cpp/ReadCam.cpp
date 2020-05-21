#include "opencv2/opencv.hpp"
#include "iostream"
#include <time.h>

using namespace std;

int main(int, char**) {
    int numFrames = 0;
    clock_t start_time, end_time;

    // open the first webcam plugged in the computer
    cv::VideoCapture camera(0);
    if (!camera.isOpened()) {
        std::cerr << "ERROR: Could not open camera" << std::endl;
        return 1;
    }

    // create a window to display the images from the webcam
    cv::namedWindow("Webcam", CV_WINDOW_AUTOSIZE);

    // this will contain the image from the webcam
    cv::Mat frame;

    start_time = clock();


    // display the frame until you press a key
    while (1) {
        numFrames++;

        // capture the next frame from the webcam
        camera >> frame;

        // show the image on the window
        cv::imshow("Webcam", frame);
        // wait (10ms) for a key to be pressed
        if (cv::waitKey(10) >= 0)
            break;
    }

    end_time = clock();

    double time_diff = double(end_time - start_time)/double(CLOCKS_PER_SEC);
    cout << "Time taken by program is : " << fixed
         << time_diff << setprecision(5);
    cout << " seconds. " << endl;

    double fps = numFrames/time_diff;
    cout << "FPS for the camera is : " << fixed
         << fps << setprecision(5);
    cout << " frames per second. " << endl;

    return 0;
}
