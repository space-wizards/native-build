#!/bin/bash python3

import subprocess
import shutil
from common import Software, Github, Platform


class Freetype(Software):
    def __init__(self) -> None:
        super().__init__("Freetype", "freetype")

        self.outputs = {
            Platform.Windows: [
                "freetype.dll",
                "freetype.pdb",
            ],
            Platform.Linux: ["libfreetype.so"],
            Platform.OSX: ["libfreetype.dylib"],
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


if __name__ == "__main__":
    library = Freetype()
    library.build()
    library.publish()
