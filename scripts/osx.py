#!/usr/bin/env python3

from software.zstd import ZStd
from software.glfw import GLFW
from software.sdl import SDL
from software.openal import OpenAL
from software.freetype import Freetype
from software.fluidsynth import Fluidsynth

from common import Github, Software, dump_build_notes, ARTIFACT_DIR, ROOT_DIR

if __name__ == "__main__":
    to_build: list[Software] = [
        ZStd(),
        GLFW(),
        SDL(),
        OpenAL(),
        Freetype(),
        Fluidsynth(),
    ]

    for build in to_build:
        with Github.LogGroup(f"Building {build.name}"):
            build.build()
            build.publish()

    dump_build_notes(
        "native-build (OSX x64)",
        ROOT_DIR,
        ARTIFACT_DIR.joinpath("notes.md"),
        [f"- {build.name}" for build in to_build],
    )
