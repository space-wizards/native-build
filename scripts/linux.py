#!/usr/bin/env python3

from software.zstd import ZStd
from software.glfw import GLFW
from software.sdl import SDL
from software.openal import OpenAL
from software.freetype import Freetype
from software.fluidsynth import Fluidsynth

from common import Github, Software, dump_build_notes, filter_software_to_build, ARTIFACT_DIR, Platform, ROOT_DIR
from common.software import SoftwareImpl
from common.args import parse_args
from common.platform import RID_LINUX_X64

import subprocess

if __name__ == "__main__":
    args = parse_args(RID_LINUX_X64)

    to_build: list[SoftwareImpl] = [
        ZStd,
        GLFW,
        SDL,
        OpenAL,
        #Fluidsynth,
    ]

    build_softwares = filter_software_to_build(to_build, args)

    for build in build_softwares:
        with Github.LogGroup(f"Building {build.name}"):
            build.build()
            build.publish()

            # Strip debug information out per build's outputs
            new_outputs = []
            for output_name in build.outputs[Platform.Linux]:
                Github.log(f"Moving debug information for {output_name}")
                debug_name = f"{output_name}.debug"
                subprocess.run(
                    [
                        "objcopy",
                        "--only-keep-debug",
                        str(build.publish_dir.joinpath(output_name)),
                        str(build.publish_dir.joinpath(debug_name)),
                    ],
                    check=True
                )
                new_outputs.append(debug_name)
            build.outputs[Platform.Linux].extend(new_outputs)

    dump_build_notes(
        "native-build (Linux)",
        ROOT_DIR,
        ARTIFACT_DIR.joinpath("notes.md"),
        [f"- {build.name}" for build in build_softwares],
    )
