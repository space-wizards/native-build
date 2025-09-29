from common import VcpkgSoftware, Platform, BuildArgs

class Angle(VcpkgSoftware):
    def __init__(self, args: BuildArgs) -> None:
        super().__init__(args, "ANGLE", "chromium_7440")

        self.outputs = {
            Platform.Windows: ["bin/libEGL.dll", "bin/libEGL.pdb", "bin/libGLESv2.dll", "bin/libGLESv2.pdb"],
        }
