# USB Camera Tests
This repository provides automated test cases for validating USB web-camera functionality. This is supported for USB cameras through v4l2 driver. This test-suite is validated on Ubuntu 18.04 operating system with Intel and NVIDIA Jetson chipsets.

This library uses Python OpenCV package and v4l2-ctl library for validation. 

## Pre-requisites

* Install latest Python 3.x and PIP library.
```
sudo apt-get update
sudo apt-get install python3.6
sudo apt-get install python3-pip
```

* Validate ```python3``` & ```pip3``` are working. 
```
python3 --version
```

* Install Video4Linux2 Dependencies
```
sudo apt-get update
suto apt-get install v4l-utils
```

* Validate v4l2 is working
```
v4l2-ctl --list-devices
<Should show list of connected USB cameras.>
```

## Installation
* Clone this repository
```
git clone <this-repo>
cd camera-tests
```

* (Optional) Create a Python virtual environment.
```
python3 -m pip install --user virtualenv
python3 -m venv venv
source venv/bin/activate
``` 

* Install python dependencies 
```
python3 -m pip install -r requirements.txt
```

## Camera Test Configuration
You can configure the input camera device by editing `device` variable in `config.py`. Change this to the camera to be tested. You can find the connected cameras using `v4l2-ctl --list-devices`
```
device = "/dev/video0"
```

The cameras can support multiple resolutions. Update the field `resolutions` in `config.py` to add/remove any resolutions to be tested. (The supported resolutions for the device can be found using `v4l2-ctl --device /dev/video0 --list-formats-ext`).

```
resolutions = [
    (640, 480),
    (800, 600),
    (1024, 768),
    (1280, 720),
    (1280, 960),
]
```


## Test Suite
#### Test default resolution video capture and calculate FPS.
* **Objective**: Get resolution for default resolution
* **Run Command**: `python3 fps-test-simple.py` 
* **Output**: This test will open a OpenCV display window showing current video. It will capture 120 frames and print out the FPS obtained. 


#### Test all supported resolutions and calculate FPS for each.
* **Objective**: Iterate through all resolutions to be tested. Calculate & display FPS for each resolution.  
* **Run Command**: `python3 resolutions-test.py` 
* **Output**: This test will open an OpenCV display window showing current video, resolution and the FPS obtained. To go to the next resolution, hit "SPACE" key. To exit the program, hit "ESC".



* Run individual tests
  * This will open a OpenCV window and iterate through different brightness values.
  * There are other similar tests for updating other parameters. Ex: `contrast-test.py`, `gamma-test.py`, `hue-test.py` etc.
```
python3 brightness-test.py
```


* Run resolution tests:
  * This will open a OpenCV window showing current video frame and resolution.
  * Hit Space key to test the next supported resolution
  * Hit ESC key to exit the program.
```
python3 resolution-tests.py
```

* Run all tests
   * TBD
```
python3 all-tests.py
```

* Some tests do require manual observation. Go through individual test documentation for more details.
