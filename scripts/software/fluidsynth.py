#!/bin/bash python3

from common import VcpkgSoftware, Platform, BuildArgs

class Fluidsynth(VcpkgSoftware):
    def __init__(self, args: BuildArgs) -> None:
        super().__init__(args, "Fluidsynth")

        self.outputs = {
            Platform.Windows: ["bin/libfluidsynth-3.dll", "bin/libfluidsynth-3.pdb"],
            Platform.Linux: ["lib/libfluidsynth.so"],
            Platform.OSX: ["lib/libfluidsynth.3.dylib"],
        }
