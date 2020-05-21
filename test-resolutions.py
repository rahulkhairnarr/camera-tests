# Check for resolutions supported by camera

import config
import utils

class ResolutionsTest(object):
    def __init__(self):
        self.device = config.settings['device']
        self.resolutions = config.get_resolutions()
