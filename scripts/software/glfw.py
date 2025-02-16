#!/bin/bash python3

import subprocess
import shutil
from common import Software, Github, Platform


class GLFW(Software):
    def __init__(self) -> None:
        super().__init__("GLFW", "glfw")

        self.outputs = {
            Platform.Windows: [
                "src/glfw3.dll",
                "src/glfw3.pdb",
            ],
            Platform.Linux: ["src/libglfw.so"],
            Platform.OSX: ["src/libglfw.dylib"],
        }

    def build(self) -> None:
        cmake = shutil.which("cmake")

        Github.log("Setting up CMake...")
        result = subprocess.call(
            [
                cmake,
                f"-B{self.dest_dir}",
                "-GNinja",
                "-DBUILD_SHARED_LIBS=On",
                "-DGLFW_BUILD_EXAMPLES=Off",
                "-DGLFW_BUILD_TESTS=Off",
                "-DGLFW_BUILD_DOCS=Off",
                "-DGLFW_INSTALL=Off",
                "-DCMAKE_BUILD_TYPE=RelWithDebInfo",
            ],
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
