import shutil
from dataclasses import dataclass
from abc import abstractmethod, ABCMeta
from pathlib import Path
from typing import Callable, Iterable

from .platform import Platform
from .github import Github
from .helpers import dump_build_notes, copy_file_or_tree
from .paths import *
from .args import BuildArgs


@dataclass
class SoftwareOutput:
    src: str
    dst: str

    def get_src(self: "SoftwareOutputLike") -> str:
        if isinstance(self, SoftwareOutput):
            return self.src

        if isinstance(self, str):
            return self

        raise ValueError()

    def get_dst(self: "SoftwareOutputLike") -> str:
        if isinstance(self, SoftwareOutput):
            return self.dst

        if isinstance(self, str):
            return self

        raise ValueError()

    def get_dst_name(self: "SoftwareOutputLike") -> str:
        return Path(SoftwareOutput.get_dst(self)).name


SoftwareOutputLike = str | SoftwareOutput


def software_output_get_src(output: SoftwareOutputLike) -> str:
    if output is str:
        return Path(output).name

    if output is SoftwareOutput:
        return Path(output.dst).name

    raise ValueError()


def software_output_get_name(output: SoftwareOutputLike) -> str:
    if output is str:
        return Path(output).name

    if output is SoftwareOutput:
        return Path(output.dst).name

    raise ValueError()


class Software(metaclass=ABCMeta):
    def __init__(self, build_args: BuildArgs, name: str) -> None:
        self.name = name

        self.publish_dir = ARTIFACT_DIR.joinpath(self.name, build_args.rid)
        if self.publish_dir.exists():
            shutil.rmtree(self.publish_dir)
        self.publish_dir.mkdir(exist_ok=True, parents=True)

        self.outputs: dict[Platform, list[SoftwareOutputLike]] = {}
        self.tools: dict[str, Path] = {}
        self.build_args = build_args

    @abstractmethod
    def build(self) -> None:
        pass

    @abstractmethod
    def publish(self) -> None:
        pass


SoftwareImpl = Callable[[BuildArgs], Software]


def filter_software_to_build(software_available: Iterable[SoftwareImpl], build_args: BuildArgs) -> list[Software]:
    softwares = []
    for software_type in software_available:
        software = software_type(build_args)
        if build_args.software is not None and software.name not in build_args.software:
            continue
        
        softwares.append(software)

    return softwares


class SelfBuiltSoftware(Software):
    def __init__(self, build_args: BuildArgs, name: str, dir: str) -> None:
        super().__init__(build_args, name)

        self.source_dir: Path = ROOT_DIR.joinpath(dir)
        self.dest_dir: Path = BUILD_DIR.joinpath(dir, build_args.rid)
        if self.dest_dir.exists():
            shutil.rmtree(self.dest_dir)
        self.dest_dir.mkdir(exist_ok=True, parents=True)

    def publish(self) -> None:
        os = Platform.get()
        if os not in self.outputs.keys():
            Github.bail(f"Unknown platform {os}, unable to handle outputs")

        for output in self.outputs[os]:
            output_path = self.dest_dir.joinpath(
                SoftwareOutput.get_src(output)
            ).resolve()  # Ensure we have resolved symlinks
            if not output_path.exists():
                Github.bail(f"Failed to find output [{output_path}]")
                continue  # Shouldn't be hit, but leaving this here anyway

            # Since output_path might have changed (due to symlinks), re-use the expected
            # output name here
            new_path = self.publish_dir / SoftwareOutput.get_dst_name(output)
            Github.log(f"[{output_path}] => [{new_path}]")
            copy_file_or_tree(output_path, new_path)

        dump_build_notes(
            f"{self.name} (`{self.build_args}`)",
            self.source_dir,
            self.publish_dir.joinpath("notes.md"),
            [f"- {SoftwareOutput.get_dst_name(output)}" for output in self.outputs[os]]
        )
