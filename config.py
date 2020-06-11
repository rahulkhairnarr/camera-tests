
# Device name to test. You can find it via: v4l2-ctl --list-devices
device = "/dev/video0"

# Different resolutions to be tested.
# You can find these by v4l2-ctl --list-formats-ext
# Update to add/remove resolutions as needed.
resolutions = [
    (640, 480),
    (800, 600),
    (1024, 768),
    (1280, 720),
    (1280, 960),
    (1600, 1200),
    (1920, 1080),
    (2048, 1536),
    (2592, 1944),
    (3264, 2448)
]

