#!/usr/bin/env python3

import subprocess
from software.zstd import ZStd
from software.glfw import GLFW
from software.sdl import SDL
from software.openal import OpenAL
from software.freetype import Freetype
from software.fluidsynth import Fluidsynth

from common import Github, Platform, Software, dump_build_notes, ARTIFACT_DIR, ROOT_DIR
from common.software import SoftwareImpl
from common.args import parse_args
from common.platform import RID_OSX_ARM64, RID_OSX_X64

if __name__ == "__main__":
    args = parse_args(RID_OSX_ARM64)
    to_build: list[SoftwareImpl] = [
        ZStd,
        GLFW,
        SDL,
        OpenAL,
        Freetype,
        #Fluidsynth,
    ]

    build_softwares = [b(args) for b in to_build]

    for build in build_softwares:
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
        f"native-build (macOS)",
        ROOT_DIR,
        ARTIFACT_DIR.joinpath("notes.md"),
        [f"- {build.name}" for build in build_softwares],
    )
