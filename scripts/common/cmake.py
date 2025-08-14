import shutil

from .platform import Architecture
from .osx import DEPLOYMENT_TARGET
from .args import BuildArgs
from .software import SelfBuiltSoftware


def locate_cmake() -> str:
    path = shutil.which("cmake")
    if path is None:
        raise RuntimeError("Unable to locate cmake!")
    
    return path


def cmake_common_args(args: BuildArgs) -> list[str]:
    cmake_args = [
        "-GNinja",
        f"-DCMAKE_OSX_DEPLOYMENT_TARGET={DEPLOYMENT_TARGET}",
        "-DCMAKE_BUILD_TYPE=RelWithDebInfo"
    ]
    arch = Architecture.from_rid(args.rid)
    if arch == Architecture.X64:
        cmake_args.append(f"-DCMAKE_OSX_ARCHITECTURES=x86_64")
    elif arch == Architecture.Arm64:
        cmake_args.append(f"-DCMAKE_OSX_ARCHITECTURES=arm64")

    return cmake_args


class CmakeSoftware(SelfBuiltSoftware):
    pass
