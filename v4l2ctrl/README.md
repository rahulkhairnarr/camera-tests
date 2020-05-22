# Camera Tests
This project provides scripts for automated testing of cameras. These tests include:
- Using OpenCV to open and display camera.
- Calculating FPS for the camera.
- Updating various v4l2 parameters and calculating FPS and quality with them.
- Resetting v4l2 parameters so camera can go back to its initial state.

# Build and Test Python code
```
git clone <this repo>
cd camera-tests
pip install -r requirements.txt
python3 run-all-tests.py
python3 set-optimal-params.py
python3 reset-params.py
```

# Build and Test C code.
```
cd v4l2ctrl
mkdir build
cd build
cmake ..
make
```
This will build v4l2ctrl application. 

