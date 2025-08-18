#!/usr/bin/env python3

from software.zstd import ZStd

from common import Github, dump_build_notes, filter_software_to_build, ARTIFACT_DIR, ROOT_DIR
from common.software import SoftwareImpl
from common.args import parse_args
from common.linux import separate_debug_info

if __name__ == "__main__":
    args = parse_args()

    to_build: list[SoftwareImpl] = [
        ZStd,
    ]

    build_softwares = filter_software_to_build(to_build, args)

    for build in build_softwares:
        with Github.LogGroup(f"Building {build.name}"):
            build.build()
            build.publish()

            separate_debug_info(build)


    dump_build_notes(
        "native-build (Linux)",
        ROOT_DIR,
        ARTIFACT_DIR.joinpath("notes.md"),
        [f"- {build.name}" for build in build_softwares],
    )
