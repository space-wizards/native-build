from pathlib import Path
from abc import abstractmethod
import shutil

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
BUILD_DIR = ROOT_DIR.joinpath("build")
ARTIFACT_DIR = ROOT_DIR.joinpath(".artifacts")


class Build:
    def __init__(self, name: str, dir: str) -> None:
        self.name = name
        self.source_dir: Path = ROOT_DIR.joinpath(dir)
        self.dest_dir: Path = BUILD_DIR.joinpath(dir)
        self.dest_dir.mkdir(exist_ok=True, parents=True)

        self.outputs: list[Path] = []
        self.tools: dict[str, Path] = {}

    def log(self, msg: str) -> None:
        print(f"[{self.name}] {msg}")

    @abstractmethod
    def setup(self) -> None:
        pass

    @abstractmethod
    def build(self) -> bool:
        pass

    def publish(self) -> bool:
        self.log("Publishing...")
        success = True

        publish_dir = ARTIFACT_DIR.joinpath("zstd")
        publish_dir.mkdir(exist_ok=True, parents=True)

        for output in self.outputs:
            if not output.exists():
                self.log(f"Failed to find output [{output}]")
                success = False
                break
            output.rename(publish_dir.joinpath(output.name))

        self.log(f"Complete with [{'success' if success else 'failure'}]")
        return success

    def require_tool(self, tool_name: str) -> None:
        tool = shutil.which(tool_name)
        if not tool:
            raise RuntimeError(f"[{self.name}] Missing tool [{tool_name}]")
