# /bin/bash python3

import subprocess
import shutil
from common import Build


class ZStd(Build):
    def __init__(self) -> None:
        super().__init__("zstd", "zstd")

        self.outputs = [
            self.dest_dir.joinpath("lib/zstd.dll"),
            self.dest_dir.joinpath("lib/zstd.lib"),
        ]

    def setup(self) -> None:
        self.require_tool("cmake")
        self.require_tool("ninja")

    def build(self) -> bool:
        cmake = shutil.which("cmake")

        self.log("Setting up CMake")
        subprocess.call(
            [
                cmake,
                "build/cmake",
                f"-B{self.dest_dir}",
                "-GNinja",
                "-DZSTD_BUILD_SHARED=ON",
                "-DZSTD_BUILD_STATIC=OFF",
                "-DZSTD_BUILD_PROGRAMS=OFF",
                "-DZSTD_BUILD_TESTS=OFF",
                "-DZSTD_MULTITHREAD_SUPPORT=ON",
                "-DZSTD_BUILD_CONTRIB=OFF",
                "-DZSTD_LEGACY_SUPPORT=OFF",
                "-DCMAKE_BUILD_TYPE=Release",
            ],
            text=True,
            cwd=self.source_dir,
        )

        self.log("Building up CMake")
        subprocess.call(
            [cmake, "--build", "."],
            text=True,
            cwd=self.dest_dir,
        )
        return True


if __name__ == "__main__":
    library = ZStd()
    library.setup()
    library.build()
    library.publish()
