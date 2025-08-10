#!/bin/bash python3

import os
import subprocess
import shutil
from common import Software, Github, Platform, ROOT_DIR, BuildArgs, Architecture
from common.cmake import locate_cmake, cmake_common_args
from common.vcpkg import get_vcpkg_host_triplet

class Fluidsynth(Software):
    def __init__(self, args: BuildArgs) -> None:
        super().__init__(args, "Fluidsynth", "fluidsynth")

        self.outputs = {
            Platform.Windows: ["src/libfluidsynth-3.dll", "src/libfluidsynth-3.pdb"],
            Platform.Linux: ["src/libfluidsynth.so"],
            Platform.OSX: ["src/libfluidsynth.3.dylib"],
        }

    def build(self) -> None:
        cmake = locate_cmake()

        Github.log("Setting up CMake...")
        generation_args = [
            cmake,
            f"-B{self.dest_dir}",
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
            "-Denable-sdl3=OFF",
            "-Denable-libinstpatch=OFF",
            "-Denable-pulseaudio=OFF",
            "-Denable-readline=OFF",
            "-Denable-lash=OFF",
            "-Denable-framework=OFF",
            "-Denable-systemd=OFF",
            "-Denable-coreaudio=OFF"
        ] + cmake_common_args(self.build_args)

        generation_env = os.environ.copy()

        arch = Architecture.from_rid(self.build_args.rid)
        platform = Platform.get()
        if platform == Platform.Windows or platform == Platform.OSX:
            if platform == Platform.Windows:
                vcpkg_triplet = f"{arch.get_vcpkg_arch()}-get-windows-static-md"
            else:
                vcpkg_triplet = f"{arch.get_vcpkg_arch()}-osx"
            vc_install_dir = ROOT_DIR.joinpath("vcpkg_installed", vcpkg_triplet)
            tools_install_dir = ROOT_DIR.joinpath("vcpkg_installed", get_vcpkg_host_triplet())
            tools_directories = [
                str(tools_install_dir.joinpath("tools", "pkgconf")),
                str(tools_install_dir.joinpath("lib")),
            ]

            generation_args += [
                "-DCMAKE_WARN_DEPRECATED=Off",  # So much spam from the vcpkg.cmake file
                f"-DCMAKE_TOOLCHAIN_FILE={os.getenv('VCPKG_ROOT')}/scripts/buildsystems/vcpkg.cmake",
                f"-DCMAKE_PROGRAM_PATH={';'.join(tools_directories)}",
            ]

            generation_env["PKG_CONFIG_PATH"] = str(
                vc_install_dir.joinpath("lib", "pkgconfig")
            )

        result = subprocess.call(
            generation_args, text=True, cwd=self.source_dir, env=generation_env
        )
        if result != 0:
            Github.bail("Failed to setup CMake")

        Github.log("Building up CMake...")
        subprocess.run(
            [
                cmake,
                "--build",
                ".",
            ],
            check=True,
            cwd=self.dest_dir,
        )
        if result != 0:
            Github.bail("Failed to build")
