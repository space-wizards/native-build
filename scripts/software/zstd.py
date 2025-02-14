#!/bin/bash python3

import subprocess
import shutil
from common import Software, Github


class ZStd(Software):
    def __init__(self) -> None:
        super().__init__("zstd", "zstd")

        self.outputs = {
            "Windows": [
                "lib/zstd.dll",
                "lib/zstd.pdb",
            ],
            "Linux": ["lib/libzstd.so"],
            "Darwin": ["lib/libzstd.dylib"],
        }

    def build(self) -> None:
        cmake = shutil.which("cmake")

        Github.log("Setting up CMake...")
        result = subprocess.call(
            [
                cmake,
                "build/cmake",
                f"-B{self.dest_dir}",
                "-GNinja",
                "-DZSTD_BUILD_SHARED=ON",
                "-DZSTD_BUILD_STATIC=OFF",
                "-DZSTD_BUILD_PROGRAMS=OFF",
                "-DZSTD_BUILD_TESTS=OFF",
                "-DZSTD_MULTITHREAD_SUPPORT=ON",
                "-DZSTD_BUILD_CONTRIB=OFF",
                "-DZSTD_LEGACY_SUPPORT=OFF",
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
