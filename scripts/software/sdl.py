#!/bin/bash python3

import subprocess
import shutil
from common import Software, Github, Platform


class SDL(Software):
    def __init__(self) -> None:
        super().__init__("SDL", "SDL")

        self.outputs = {
            Platform.Windows: [
                "SDL2.dll",
                "SDL2.pdb",
            ],
            Platform.Linux: ["libSDL2-2.0.so"],
            Platform.OSX: ["libSDL2-2.0.dylib"],
        }

    def build(self) -> None:
        cmake = shutil.which("cmake")

        cmake_args = [
            cmake,
            f"-B{self.dest_dir}",
            "-GNinja",
            "-DSDL_SHARED=On",
            "-DSDL_STATIC=Off",
            "-DSDL_WERROR=Off",
            "-DSDL_TESTS=Off",
            "-DSDL_INSTALL_TESTS=Off",
            "-DCMAKE_BUILD_TYPE=RelWithDebInfo",
        ]

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
