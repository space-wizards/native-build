import argparse
from dataclasses import dataclass
from typing import Optional

from .platform import Rid

@dataclass
class BuildArgs:
    rid: Rid
    software: Optional[set[str]]

def parse_args(default_rid: Rid) -> BuildArgs:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rid", default=default_rid)
    parser.add_argument("--software", nargs="*")

    args = parser.parse_args()

    return BuildArgs(Rid(args.rid), set(args.software) or None)
