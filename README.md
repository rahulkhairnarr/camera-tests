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

## Camera configuration
We have to configure the correct camera inputs and resolutions before running the test cases.


## Run Tests
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
