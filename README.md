# Camera Tests

This repository provides automated test cases for validating web-camera functionality.

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
```
python3 camera-fps-test.py
python3 camera-params-test.py
python3 camera-aperture-test.py
<etc>
```

* Run all tests
```
python3 all-tests.py
```

* Most tests do require manual observation. Go through individual test documentation for more details.
