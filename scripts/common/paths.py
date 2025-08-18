from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent.parent
BUILD_DIR = ROOT_DIR.joinpath("build")
ARTIFACT_DIR = ROOT_DIR.joinpath("artifacts")
VCPKG_INSTALLED_DIR = ROOT_DIR / "vcpkg_installed"

__all__ = ["SCRIPT_DIR", "ROOT_DIR", "BUILD_DIR", "ARTIFACT_DIR"]
