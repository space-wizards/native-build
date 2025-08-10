import argparse
from dataclasses import dataclass

from .platform import Rid

@dataclass
class BuildArgs:
    rid: Rid

def parse_args(default_rid: Rid) -> BuildArgs:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rid", default=default_rid)

    args = parser.parse_args()

    return BuildArgs(Rid(args.rid))
