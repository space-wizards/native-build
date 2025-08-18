#!/bin/bash python3

import subprocess
import shutil
from common import CmakeSoftware, Github, Platform
from common.cmake import cmake_common_args, locate_cmake
from common.args import BuildArgs


class SDL(CmakeSoftware):
    def __init__(self, build_args: BuildArgs) -> None:
        super().__init__(build_args, "SDL", "3.2.20", "SDL")

        self.outputs = {
            Platform.Windows: [
                "SDL3.dll",
                "SDL3.pdb",
            ],
            Platform.Linux: ["libSDL3.so.0"],
            Platform.OSX: ["libSDL3.0.dylib"],
        }

    def build(self) -> None:
        cmake = locate_cmake()

        cmake_args = [
            cmake,
            f"-B{self.dest_dir}",
            "-DSDL_SHARED=On",
            "-DSDL_STATIC=Off",
            "-DSDL_WERROR=Off",
            "-DSDL_TESTS=Off",
            "-DSDL_INSTALL_TESTS=Off",
            "-DSDL_GPU=Off",
            "-DSDL_RENDER=Off",
            "-DSDL_CAMERA=Off",
        ] + cmake_common_args(self.build_args)

        Github.log("Setting up CMake...")
        result = subprocess.call(
            cmake_args,
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
