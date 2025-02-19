#!/bin/bash python3
from software.zstd import ZStd
from software.glfw import GLFW
from software.sdl import SDL
from software.openal import OpenAL
from software.fluidsynth import Fluidsynth
from software.freetype import Freetype

from common import Github, Software, dump_build_notes, ARTIFACT_DIR, ROOT_DIR

if __name__ == "__main__":
    to_build: list[Software] = [
        Fluidsynth(),
        ZStd(),
        GLFW(),
        SDL(),
        OpenAL(),
        Freetype(),
    ]

    # We expect vcpkg_installed to exist on system, else Fluidsynth is going to fail
    vcpkg_dir = ROOT_DIR.joinpath("vcpkg_installed")
    if not vcpkg_dir.exists():
        Github.notice("VCPkgs are not installed to {vcpkg_dir}, some builds may fail")

    for build in to_build:
        with Github.LogGroup(f"Building {build.name}"):
            build.build()
            build.publish()

    dump_build_notes(
        "native-build (Windows x64)",
        ROOT_DIR,
        ARTIFACT_DIR.joinpath("notes.md"),
        [f"- {build.name}" for build in to_build],
    )
