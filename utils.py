from singleton_decorator import singleton
import v4l2
import v4l2ctrl
import fcntl

@singleton
class Utils(object):
    def __init__(self):
        pass

    def get_resolutions(self):
        v4l2.

