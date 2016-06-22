#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""test_hello
----------------------------------

Tries to build and test the `hello` sample project.
"""

import os
import os.path
import shutil
import subprocess
import sys

from skbuild.exceptions import SKBuildError
from skbuild.cmaker import SKBUILD_DIR, CMAKE_BUILD_DIR

from .common import test_case

@test_case
def test_hello_builds():
    old_argv = sys.argv
    old_cwd = os.getcwd()

    sys.argv = ["setup.py", "install"]
    os.chdir(os.path.join("samples", "hello"))

    if os.path.exists(SKBUILD_DIR):
        shutil.rmtree(SKBUILD_DIR)

    try:
        exec(open("setup.py").read())
    finally:
        os.chdir(old_cwd)
        sys.argv = old_argv

@test_case
def test_hello_works():
    old_cwd = os.getcwd()
    os.chdir(os.path.join("samples", "hello", CMAKE_BUILD_DIR))
    try:
        subprocess.check_call(["ctest", "--output-on-failure"])
    finally:
        os.chdir(old_cwd)

