#!/bin/bash python3

import subprocess
import shutil
from common import Software, Github, Platform
from common.cmake import cmake_common_args, locate_cmake
from common.args import BuildArgs


class Freetype(Software):
    def __init__(self, args: BuildArgs) -> None:
        super().__init__(args, "Freetype", "freetype")

        self.outputs = {
            Platform.Windows: [
                "freetype.dll",
                "freetype.pdb",
            ],
            Platform.Linux: ["libfreetype.so"],
            Platform.OSX: ["libfreetype.dylib"],
        }

    def build(self) -> None:
        cmake = locate_cmake()

        Github.log("Setting up CMake...")
        result = subprocess.call(
            [
                cmake,
                f"-B{self.dest_dir}",
                "-DBUILD_SHARED_LIBS=On",
                "-DFT_DISABLE_PNG=TRUE",
                "-DFT_DISABLE_BROTLI=TRUE",
                "-DFT_DISABLE_HARFBUZZ=TRUE",
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
