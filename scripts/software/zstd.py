#!/bin/bash python3

import subprocess
import shutil
from common import Software, Github, Platform
from common.cmake import cmake_common_args


class ZStd(Software):
    def __init__(self) -> None:
        super().__init__("zstd", "zstd")

        self.outputs = {
            Platform.Windows: [
                "lib/zstd.dll",
                "lib/zstd.pdb",
            ],
            Platform.Linux: ["lib/libzstd.so"],
            Platform.OSX: ["lib/libzstd.dylib"],
        }

    def build(self) -> None:
        cmake = shutil.which("cmake")

        Github.log("Setting up CMake...")
        result = subprocess.call(
            [
                cmake,
                "build/cmake",
                f"-B{self.dest_dir}",
                "-DZSTD_BUILD_SHARED=ON",
                "-DZSTD_BUILD_STATIC=OFF",
                "-DZSTD_BUILD_PROGRAMS=OFF",
                "-DZSTD_BUILD_TESTS=OFF",
                "-DZSTD_MULTITHREAD_SUPPORT=ON",
                "-DZSTD_BUILD_CONTRIB=OFF",
                "-DZSTD_LEGACY_SUPPORT=OFF",
            ] + cmake_common_args(),
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
