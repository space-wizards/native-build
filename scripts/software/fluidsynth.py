#!/bin/bash python3

from common import VcpkgSoftware, Platform, BuildArgs

class Fluidsynth(VcpkgSoftware):
    def __init__(self, args: BuildArgs) -> None:
        super().__init__(args, "Fluidsynth", "2.4.6")

        self.outputs = {
            Platform.Windows: ["bin/libfluidsynth-3.dll", "bin/libfluidsynth-3.pdb"],
            Platform.Linux: ["lib/libfluidsynth.so.3"],
            Platform.OSX: ["lib/libfluidsynth.3.dylib"],
        }
