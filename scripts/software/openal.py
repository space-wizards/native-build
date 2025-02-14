#!/bin/bash python3

import subprocess
import shutil
from common import Software, Github


class OpenAL(Software):
    def __init__(self) -> None:
        super().__init__("OpenAL-Soft", "openal-soft")

        self.outputs = {
            "Windows": [
                "OpenAL32.dll",
                "OpenAL32.pdb",
            ],
            "Linux": ["libopenal.so"],
            "Darwin": ["libopenal.dylib"],
        }

    def build(self) -> None:
        cmake = shutil.which("cmake")

        Github.log("Setting up CMake...")
        result = subprocess.call(
            [
                cmake,
                f"-B{self.dest_dir}",
                "-GNinja",
                "-DALSOFT_UTILS=Off",
                "-DALSOFT_EXAMPLES=Off",
                "-DALSOFT_TESTS=Off",
                "-DALSOFT_INSTALL=Off",
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
