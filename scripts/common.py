from abc import abstractmethod
from pathlib import Path
from enum import Enum
import platform as _platform  # Python gets confused with similar names here
import shutil
import subprocess
import sys

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
BUILD_DIR = ROOT_DIR.joinpath("build")
ARTIFACT_DIR = ROOT_DIR.joinpath("artifacts")


class Platform(Enum):
    Windows = (1,)
    Linux = (2,)
    OSX = (3,)

    @staticmethod
    def get() -> "Platform":
        platform = _platform.system()
        if platform == "Windows":
            return Platform.Windows
        elif platform == "Linux":
            return Platform.Linux
        elif platform == "Darwin":
            return Platform.OSX
        else:
            raise RuntimeError(f"Unknown platform {platform}")


class Github:
    @staticmethod
    def log(msg: str) -> None:
        print(msg, flush=True)

    @staticmethod
    def notice(msg: str) -> None:
        print(f"::notice::{msg}", flush=True)

    @staticmethod
    def warning(msg: str) -> None:
        print(f"::warning::{msg}", flush=True)

    @staticmethod
    def error(msg: str) -> None:
        print(f"::error::{msg}", flush=True)

    @staticmethod
    def bail(msg: str) -> None:
        Github.error(msg)
        sys.exit(1)

    class LogGroup:
        def __init__(self, msg: str) -> None:
            self.msg = msg

        def __enter__(self) -> None:
            print(f"::group::{self.msg}", flush=True)

        def __exit__(self, type, value, traceback) -> None:
            print(f"::endgroup::", flush=True)


def dump_build_notes(name: str, working_dir: Path, output: Path, contents: list[str]):
    # Check if the source directory is a git one, if so we can add some cool
    # git information to the output directory for storage later.
    try:
        remote = subprocess.check_output(
            ["git", "remote", "get-url", "origin"], text=True, cwd=working_dir
        ).strip()
        commit_hash = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True, cwd=working_dir
        ).strip()

        note_text = f"""# {name}

Compiled from `{remote}`:`{commit_hash}`

Contains:

"""
        note_text += "\n".join(contents)
        output.write_text(note_text)

    except Exception as e:
        # Not a git directory or some other failure, don't need to fail anything though
        Github.notice(
            f"Skipping git information for {working_dir} due to exception: {e}"
        )
        pass


class Software:
    def __init__(self, name: str, dir: str) -> None:
        self.name = name
        self.source_dir: Path = ROOT_DIR.joinpath(dir)
        self.dest_dir: Path = BUILD_DIR.joinpath(dir)
        if self.dest_dir.exists():
            shutil.rmtree(self.dest_dir)
        self.dest_dir.mkdir(exist_ok=True, parents=True)

        self.publish_dir = ARTIFACT_DIR.joinpath(self.name)
        if self.publish_dir.exists():
            shutil.rmtree(self.publish_dir)
        self.publish_dir.mkdir(exist_ok=True, parents=True)

        self.outputs: dict[str, list[str]] = []
        self.tools: dict[str, Path] = {}

    @abstractmethod
    def build(self) -> None:
        pass

    def publish(self) -> None:
        os = Platform.get()
        if os not in self.outputs.keys():
            Github.bail(f"Unknown platform {os}, unable to handle outputs")

        for output in self.outputs[os]:
            output_path = self.dest_dir.joinpath(
                output
            ).resolve()  # Ensure we have resolved symlinks
            if not output_path.exists():
                Github.bail(f"Failed to find output [{output_path}]")
                continue  # Shouldn't be hit, but leaving this here anyway

            # Since output_path might have changed (due to symlinks), re-use the expected
            # output name here
            new_path = self.publish_dir.joinpath(Path(output).name)
            Github.log(f"[{output_path}] => [{new_path}]")
            output_path.rename(new_path)

        dump_build_notes(
            self.name,
            self.source_dir,
            self.publish_dir.joinpath("notes.md"),
            [f"- {self.dest_dir.joinpath(output).name}" for output in self.outputs[os]],
        )
