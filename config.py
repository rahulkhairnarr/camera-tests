import platform

def get_device():
    # Update device id if more than one camera is connected.
    device_idx = 0

    if platform.system() == 'Darwin' or platform.system() == 'Windows':
        return device_idx
    elif platform.system() == 'Linux':
        return '/dev/video{}'.format(device_idx)


def get_supported_resolutions():
    # TBD: Use v4l2-ctl/gst-device-monitor-1.0 to get these dynamically.
    # Commands:
    # 1. v4l2-ctl --list-formats-ext
    # 2. gst-device-monitor-1.0
    # 3. uvcdynctrl -d /dev/video0 -f
    return [
        (640, 480),
        (800, 600),
        (1024, 768),
        (1280, 720),
        (1080, 1080),
        (1280, 960),
        (1600, 1200),
        (1920, 1080),
        (2048, 1536),
        (2593, 1944),
        (3264, 2448)
    ]

