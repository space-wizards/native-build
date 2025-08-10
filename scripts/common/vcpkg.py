import platform as _platform

def get_vcpkg_host_triplet() -> str:
    platform = _platform.system()
    machine = _platform.machine()

    platform = _platform.system()
    if platform == "Windows":
        if machine == "arm64":
            return "arm64-windows"
        if machine == "AMD64":
            return "x64-windows"
    elif platform == "Linux":
        if machine == "arm64":
            return "arm64-linux"
        if machine == "AMD64":
            return "x64-linux"
    elif platform == "Darwin":
        if machine == "arm64":
            return "arm64-osx"
        if machine == "AMD64":
            return "x64-osx"

    raise RuntimeError(f"Unknown platform {platform}")
