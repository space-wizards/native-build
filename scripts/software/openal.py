#!/bin/bash python3

import subprocess
import shutil
from common import CmakeSoftware, Github, Platform
from common.cmake import cmake_common_args, locate_cmake
from common.args import BuildArgs

class OpenAL(CmakeSoftware):
    def __init__(self, args: BuildArgs) -> None:
        super().__init__(args, "OpenAL-Soft", "openal-soft")

        self.outputs = {
            Platform.Windows: [
                "OpenAL32.dll",
                "OpenAL32.pdb",
            ],
            Platform.Linux: ["libopenal.so.1"],
            Platform.OSX: ["libopenal.1.dylib"],
        }

    def build(self) -> None:
        cmake = locate_cmake()

        Github.log("Setting up CMake...")
        result = subprocess.call(
            [
                cmake,
                f"-B{self.dest_dir}",
                "-DALSOFT_UTILS=Off",
                "-DALSOFT_EXAMPLES=Off",
                "-DALSOFT_TESTS=Off",
                "-DALSOFT_INSTALL=Off",
                "-DCMAKE_BUILD_TYPE=RelWithDebInfo",
            ] + cmake_common_args(self.build_args),
            text=True,
            cwd=self.source_dir,
        )
        if result != 0:
            Github.bail("Failed to setup CMake")

        Github.log("Building up CMake...")
        subprocess.call(
            [
                cmake,
                "--build",
                ".",
            ],
            text=True,
            cwd=self.dest_dir,
        )
        if result != 0:
            Github.bail("Failed to build")
