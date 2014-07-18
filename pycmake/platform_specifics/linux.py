from . import abstract


class LinuxPlatform(abstract.CMakePlatform):

    def __init__(self):
        super(LinuxPlatform, self).__init__()
        self.default_generators = ["Unix Makefiles", ]
