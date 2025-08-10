from typing import NewType
from enum import Enum, auto
import platform as _platform  # Python gets confused with similar names here

Rid = NewType('Rid', str)

RID_WIN_X64 = Rid("win-x64")
RID_WIN_AMR64 = Rid("win-arm64")
RID_OSX_X64 = Rid("osx-x64")
RID_OSX_ARM64 = Rid("osx-arm64")
RID_LINUX_X64 = Rid("linux-x64")
RID_LINUX_ARM64 = Rid("linux-arm64")


class Architecture(Enum):
    X64 = auto()
    Arm64 = auto()

    @staticmethod
    def from_rid(rid: Rid) -> "Architecture":
        if "arm64" in rid:
            return Architecture.Arm64
        if "x64" in rid:
            return Architecture.X64
        raise ValueError(f"Unable to determine architecture from RID: {rid}")

class Platform(Enum):
    Windows = (1,)
    Linux = (2,)
    OSX = (3,)
    FreeBSD = (4,)

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

    @staticmethod 
    def from_rid(rid: Rid) -> "Platform":
        start = rid.split("-", maxsplit=1)[0]
        if start == "osx":
            return Platform.OSX
        elif start == "win":
            return Platform.Windows
        elif start == "linux":
            return Platform.Linux
        elif start == "freebsd":
            return Platform.FreeBSD
        else:
            raise RuntimeError(f"Unknown rid {rid}")
