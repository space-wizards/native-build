from typing import NewType
from enum import Enum, auto
import platform as _platform  # Python gets confused with similar names here

Rid = NewType('Rid', str)

RID_WIN_X64 = Rid("win-x64")
RID_WIN_ARM64 = Rid("win-arm64")
RID_OSX_X64 = Rid("osx-x64")
RID_OSX_ARM64 = Rid("osx-arm64")
RID_LINUX_X64 = Rid("linux-x64")
RID_LINUX_ARM64 = Rid("linux-arm64")


def get_host_rid() -> Rid:
    platform = _platform.system()
    machine = _platform.machine()

    platform = _platform.system()
    if platform == "Windows":
        if machine == "arm64":
            return RID_WIN_ARM64
        if machine == "AMD64":
            return RID_WIN_X64
    elif platform == "Linux":
        if machine == "arm64":
            return RID_LINUX_ARM64
        if machine == "AMD64":
            return RID_LINUX_X64
    elif platform == "Darwin":
        if machine == "arm64":
            return RID_OSX_ARM64
        if machine == "AMD64":
            return RID_OSX_X64

    raise RuntimeError(f"Unknown platform {platform}")


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

    def get_vcpkg_arch(self) -> str:
        if self == Architecture.X64:
            return "x64"
        if self == Architecture.Arm64:
            return "arm64"
        raise ValueError()

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
