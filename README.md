# USB Camera Tests
This repository provides automated test cases for validating USB web-camera functionality. This is supported for USB cameras through v4l2 driver. This test-suite is validated on Ubuntu 18.04 operating system with Intel and NVIDIA Jetson chipsets.

This library uses Python OpenCV package and v4l2-ctl library for validation. 

## Pre-requisites

* Install latest **python3** and **pip3** library.
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
# config.py
# Example: resolutions to be tested.
resolutions = [
    (640, 480),
    (800, 600),
    (1024, 768),
    (1280, 720),
    (1280, 960),
]
```


## Test Suite
### *Test default resolution video capture and calculate FPS.*
* **Objective**: Get resolution for default resolution
* **Run Command**: `python3 fps-test-simple.py`
* **Output**: This test will open a OpenCV display window showing current video. It will capture 120 frames and print out the FPS obtained. 


### *Resolutions: Iterate through all supported FPS.*
* **Objective**: Iterate through all resolutions to be tested. Calculate & display FPS for each resolution.  
* **Run Command**: `python3 resolutions-test.py` 
* **Output**: This will open an OpenCV window showing current video, current resolution and the FPS. To go to the next resolution, hit "SPACE" key. To exit the program, hit "ESC".
* **Note**: To change the contrast values to be tested, please edit `resolutions` field in `config.py` file

### *Brightness: Iterate through all supported brightness values.*
* **Objective**: Iterate through all supported brightness values.   
* **Run Command**: `python3 brightness-test.py` 
* **Output**: This will open an OpenCV window iterating through different brightness values at regular intervals.
* **Note**: To change the brightness values to be tested, please edit `parameters` field in `config.py` file

### *Contrast: Iterate through all supported contrast values.*
* **Objective**: Iterate through all supported contrast values.   
* **Run Command**: `python3 contrast-test.py` 
* **Output**: This will open an OpenCV window iterating through different contrast values at regular intervals.
* **Note**: To change the contrast values to be tested, please edit `parameters` in field `config.py` file

### *Saturation: Iterate through all supported saturation values.*
* **Objective**: Iterate through all supported saturation values.   
* **Run Command**: `python3 saturation-test.py` 
* **Output**: This will open an OpenCV window iterating through different saturation values at regular intervals.
* **Note**: To change the saturation values to be tested, please edit `parameters` in field `config.py` file

### *Hue: Iterate through all supported hue values.*
* **Objective**: Iterate through all supported hue values.   
* **Run Command**: `python3 hue-test.py` 
* **Output**: This will open an OpenCV window iterating through different hue values at regular intervals.
* **Note**: To change the hue values to be tested, please edit `parameters` in field `config.py` file

### *Gamma: Iterate through all supported gamma values.*
* **Objective**: Iterate through all supported gamma values.   
* **Run Command**: `python3 gamma-test.py` 
* **Output**: This will open an OpenCV window iterating through different gamma values at regular intervals.
* **Note**: To change the gamma values to be tested, please edit `parameters` in field `config.py` file

### *Sharpness: Iterate through all supported sharpness values.*
* **Objective**: Iterate through all supported sharpness values.   
* **Run Command**: `python3 sharpness-test.py` 
* **Output**: This will open an OpenCV window iterating through different sharpness values at regular intervals.
* **Note**: To change the sharpness values to be tested, please edit `parameters` in field `config.py` file

### *Reset Parameters to default values.*
* **Objective**: Reset all parameter to defaults
* **Run Command**: `python3 reset-test.py`
* **Note**: To change default values for parameters, edit `default` field for that parameter in `config.py`
 

