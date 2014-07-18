import os
import subprocess

from pycmake import platform_specifics


class CMaker(object):

    def __init__(self, generator=None, **defines):
        if generator:
            self.generator = generator
        else:
            self.generator = platform_specifics.get_platform()

    def configure(self, generator=None):
        """
        Calls cmake to generate the makefile (or VS solution, or XCode project)

        Input:
        ------
        generator: string
            The string representing the CMake generator to use.  If None, uses defaults for your platform.
        """
        generator_id = self.generator.get_best_generator(generator)
        if not os.path.exists("cmake_build"):
            os.makedirs("cmake_build")
        os.chdir("cmake_build")
        return_status = subprocess.check_call(['cmake', '../', '-G', generator_id, "-DCMAKE_PREFIX_INSTALL=."])
        os.chdir("..")
        if return_status != 0:
            raise RuntimeError(
                "Could not successfully configure your project.  Please see CMake's output for more information.")

    def make(self, config="Release", source_dir="./"):
        """
        Calls the system-specific make program to compile code
        """
        if not os.path.exists("cmake_build"):
            raise RuntimeError(
                "CMake build folder (cmake_build) does not exist.  Did you forget to run configure before make?")
        os.chdir("cmake_build")
        return_status = subprocess.check_call(["cmake", "--build", source_dir, "--target", "install", "--config", config])
        os.chdir("..")
        return return_status


if __name__ == "__main__":
    maker = CMaker()
    #os.chdir("tests")
    maker.configure("Visual Studio 11")
