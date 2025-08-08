#!/usr/bin/env python3

import subprocess
from software.zstd import ZStd
from software.glfw import GLFW
from software.sdl import SDL
from software.openal import OpenAL
from software.freetype import Freetype
from software.fluidsynth import Fluidsynth

from common import Github, Platform, Software, dump_build_notes, ARTIFACT_DIR, ROOT_DIR

if __name__ == "__main__":
    to_build: list[Software] = [
        ZStd(),
        GLFW(),
        SDL(),
        OpenAL(),
        Freetype(),
        #Fluidsynth(),
    ]

    for build in to_build:
        with Github.LogGroup(f"Building {build.name}"):
            build.build()

            new_outputs = []
            for output_name in build.outputs[Platform.OSX]:
                Github.log(f"Moving debug information for {output_name}")
                debug_name = f"{output_name}.dSYM"
                subprocess.run(
                    [
                        "dsymutil",
                        str(build.dest_dir.joinpath(output_name)),
                    ],
                    check=True
                )
                subprocess.run(
                    [
                        "strip",
                        "-S",
                        str(build.dest_dir.joinpath(output_name)),
                    ],
                    check=True
                )

                new_outputs.append(debug_name)
            build.outputs[Platform.OSX].extend(new_outputs)

            build.publish()

    dump_build_notes(
        "native-build (OSX x64)",
        ROOT_DIR,
        ARTIFACT_DIR.joinpath("notes.md"),
        [f"- {build.name}" for build in to_build],
    )
