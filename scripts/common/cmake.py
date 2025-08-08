from .osx import DEPLOYMENT_TARGET

def cmake_common_args() -> list[str]:
    return [
        "-GNinja",
        f"-DCMAKE_OSX_DEPLOYMENT_TARGET={DEPLOYMENT_TARGET}",
        "-DCMAKE_BUILD_TYPE=RelWithDebInfo",
    ]
