#!/bin/bash python3

import subprocess
import shutil
from common import CmakeSoftware, Github, Platform
from common.cmake import cmake_common_args, locate_cmake
from common.args import BuildArgs


class GLFW(CmakeSoftware):
    def __init__(self, args: BuildArgs) -> None:
        super().__init__(args, "GLFW", "3.4", "glfw")

        self.outputs = {
            Platform.Windows: [
                "src/glfw3.dll",
                "src/glfw3.pdb",
            ],
            Platform.Linux: ["src/libglfw.so.3"],
            Platform.OSX: ["src/libglfw.3.dylib"],
        }

    def build(self) -> None:
        cmake = locate_cmake()

        Github.log("Setting up CMake...")
        result = subprocess.call(
            [
                cmake,
                f"-B{self.dest_dir}",
                "-DBUILD_SHARED_LIBS=On",
                "-DGLFW_BUILD_EXAMPLES=Off",
                "-DGLFW_BUILD_TESTS=Off",
                "-DGLFW_BUILD_DOCS=Off",
                "-DGLFW_INSTALL=Off",
                "-DGLFW_BUILD_WAYLAND=Off",
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
