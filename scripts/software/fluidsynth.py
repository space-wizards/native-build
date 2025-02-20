#!/bin/bash python3

import os
import subprocess
import shutil
from common import Software, Github, Platform, ROOT_DIR


class Fluidsynth(Software):
    def __init__(self) -> None:
        super().__init__("Fluidsynth", "fluidsynth")

        self.outputs = {
            Platform.Windows: ["src/fluidsynth.lib", "src/fluidsynth.pdb"],
            Platform.Linux: ["src/libfluidsynth.so"],
            Platform.OSX: ["src/FluidSynth.framework"],
        }

    def build(self) -> None:
        cmake = shutil.which("cmake")

        Github.log("Setting up CMake...")
        generation_args = [
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
        ]

        generation_env = os.environ.copy()

        if Platform.get() == Platform.Windows:
            vc_install_dir = ROOT_DIR.joinpath("vcpkg_installed/x64-windows-release")
            tools_directories = [
                str(vc_install_dir.joinpath("tools/pkgconf")),
                str(vc_install_dir.joinpath("lib")),
            ]

            generation_args += [
                "-DCMAKE_WARN_DEPRECATED=Off",  # So much spam from the vcpkg.cmake file
                f"-DCMAKE_TOOLCHAIN_FILE={os.getenv('VCPKG_ROOT')}/scripts/buildsystems/vcpkg.cmake",
                f"-DCMAKE_PROGRAM_PATH={';'.join(tools_directories)}",
            ]

            generation_env["PKG_CONFIG_PATH"] = str(
                vc_install_dir.joinpath("lib\\pkgconfig")
            )

        result = subprocess.call(
            generation_args, text=True, cwd=self.source_dir, env=generation_env
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
