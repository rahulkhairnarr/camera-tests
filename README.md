# USB Camera Tests

This repository provides automated test cases for validating web-camera functionality. This is supported for USB cameras through v4l2 driver.

## Pre-requisites
This test-suite is validated on Ubuntu 18.04 operating system with Intel and NVIDIA Jetson chipsets.

* Install Python 3.x Latest Version
```
sudo apt-get update
sudo apt-get install python3.6
```

* Validate Python is working
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
git clone https://coolertech@dev.azure.com/coolertech/mp-on-shelf-availability/_git/camera-tests
cd camera-tests
```

* Install python dependencies (create a virtual env if needed)
```
pip3 install -r requirements.txt
```

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
