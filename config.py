
# DEVICE NAME
# Device name to test. You can find it via: v4l2-ctl --list-devices
device = "/dev/video2"

# RESOLUTIONS
# Different resolutions to be tested.
# You can find these by v4l2-ctl --list-formats-ext
# Update to add/remove resolutions as needed.
resolutions = [
    # (640, 480),
    # (800, 600),
    # (1024, 768),
    # (1280, 720),
    (1280, 960),
    (1600, 1200),
    (1920, 1080),
    (2048, 1536),
    (2592, 1944),
    # (3264, 2448)
]

# DEFAULT RESOLUTION
# Parameter tests can be run for any single resolution.
# Update this field to update the default resolution of testing.
default_resolution = (1280, 960)

# PARAMETER RANGES
# Update the parameter ranges to configure your test case.
# For example, for brightness - use the following structure.
# 'brightness' : {
#     'min' : -64,
#     'max' : 64,
#     'step' : 4
# }
# This means iterate through brightness values: -64, -60, -56, ..., 0, ..., +56, +60, +64
#
# Note: the default values for your camera might be different.
# You can find the default parameters using the command:
# v4l2-ctl -d /dev/video0 --list-ctrls
#
parameters = {
    'brightness' : {
        'min' : -64,
        'max' : 64,
        'step' : 4,
        'default': 0
    },
    'contrast' : {
        'min': 0,
        'max': 64,
        'step': 4,
        'default': 30
    },
    'saturation' : {
        'min': 0,
        'max': 100,
        'step': 10,
        'default': 64
    },
    'hue': {
        'min': -2000,
        'max': 2000,
        'step': 100,
        'default': 80
    },
    'gamma' : {
        'min': 0,
        'max': 2,
        'step': 1,
        'default': 0
    },
    'sharpness' : {
        'min': 1,
        'max': 7,
        'step': 1,
        'default': 3
    }
}

