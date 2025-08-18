import shutil
import platform as _platform
from pathlib import Path


from . import platform as p
from .args import BuildArgs
from .software import Software, SoftwareOutput
from .platform import Platform, Rid, get_host_rid
from .github import Github
from .paths import VCPKG_INSTALLED_DIR, ROOT_DIR
from .helpers import dump_build_notes, copy_file_or_tree


# vcpkg triplets we're using to build stuff.
RID_TO_TRIPLET_MAP = {
    p.RID_WIN_X64: "x64-windows",
    p.RID_WIN_ARM64: "arm64-windows",
    p.RID_OSX_X64: "x64-osx",
    p.RID_OSX_ARM64: "arm64-osx",
    p.RID_LINUX_X64: "x64-linux",
    p.RID_LINUX_ARM64: "arm64-linux",
}


def vcpkg_triplet_for_rid(rid: Rid) -> str:
    res = RID_TO_TRIPLET_MAP.get(rid)
    if res is None:
        raise RuntimeError(f"Unknown RID: '{rid}'")

    return res


def get_vcpkg_host_triplet() -> str:
    return vcpkg_triplet_for_rid(get_host_rid())


class VcpkgSoftware(Software):
    def __init__(self, build_args: BuildArgs, name: str, version: str) -> None:
        super().__init__(build_args, name, version)

        self.vcpkg_installed_dir = VCPKG_INSTALLED_DIR / vcpkg_triplet_for_rid(build_args.rid)

    def build(self) -> None:
        # Assume vcpkg installed ahead of time.
        # Idk maybe I'll change this later.
        Github.log("Not building vcpkg directly, expect it to be done before running script")

    def publish(self) -> None:
        os = Platform.get()
        if os not in self.outputs.keys():
            Github.bail(f"Unknown platform {os}, unable to handle outputs")

        for output in self.outputs[os]:
            output_path = self.vcpkg_installed_dir.joinpath(
                SoftwareOutput.get_src(output)
            ).resolve()  # Ensure we have resolved symlinks
            if not output_path.exists():
                Github.bail(f"Failed to find vcpkg output [{output_path}]")
                continue  # Shouldn't be hit, but leaving this here anyway

            # Since output_path might have changed (due to symlinks), re-use the expected
            # output name here
            new_path = self.publish_dir / SoftwareOutput.get_dst_name(output)
            Github.log(f"[{output_path}] => [{new_path}]")
            copy_file_or_tree(output_path, new_path)

        dump_build_notes(
            f"{self.name} (`{self.build_args}`)",
            ROOT_DIR,
            self.publish_dir.joinpath("notes.md"),
            [f"- {SoftwareOutput.get_dst_name(output)}" for output in self.outputs[os]]
        )

