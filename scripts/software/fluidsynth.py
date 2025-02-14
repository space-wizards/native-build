#!/bin/bash python3

import subprocess
import shutil
from common import Software, Github


class Fluidsynth(Software):
    def __init__(self) -> None:
        super().__init__("Fluidsynth", "fluidsynth")

        self.outputs = {
            "Windows": [],
            "Linux": ["src/libfluidsynth.so"],
            "Darwin": ["src/FluidSynth.framework"],
        }

    def build(self) -> None:
        cmake = shutil.which("cmake")

        Github.log("Setting up CMake...")
        result = subprocess.call(
            [
                cmake,
                f"-B{self.dest_dir}",
                "-GNinja",
                "-Denable-aufile=OFF",
                "-Denable-dbus=OFF",
                "-Denable-ipv6=OFF",
                "-Denable-jack=OFF",
                "-Denable-ladspa=OFF",
                "-Denable-libsndfile=OFF",
                "-Denable-midishare=OFF",
                "-Denable-network=OFF",
                "-Denable-oss=OFF",
                "-Denable-sdl2=OFF",
                "-Denable-pulseaudio=OFF",
                "-Denable-readline=OFF",
                "-Denable-lash=OFF",
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
    library = Fluidsynth()
    library.build()
    library.publish()
