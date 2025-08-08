#!/usr/bin/env python3

from software.zstd import ZStd
from software.glfw import GLFW
from software.sdl import SDL
from software.openal import OpenAL
from software.freetype import Freetype
from software.fluidsynth import Fluidsynth

from common import Github, Software, dump_build_notes, ARTIFACT_DIR, Platform, ROOT_DIR

import subprocess

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

            # Strip debug information out per build's outputs
            new_outputs = []
            for output_name in build.outputs[Platform.Linux]:
                Github.log(f"Moving debug information for {output_name}")
                debug_name = f"{output_name}.debug"
                subprocess.run(
                    [
                        "objcopy",
                        "--only-keep-debug",
                        str(build.dest_dir.joinpath(output_name)),
                        str(build.dest_dir.joinpath(debug_name)),
                    ],
                    check=True
                )
                new_outputs.append(debug_name)
            build.outputs[Platform.Linux].extend(new_outputs)

            build.publish()

    dump_build_notes(
        "native-build (Linux x64)",
        ROOT_DIR,
        ARTIFACT_DIR.joinpath("notes.md"),
        [f"- {build.name}" for build in to_build],
    )
