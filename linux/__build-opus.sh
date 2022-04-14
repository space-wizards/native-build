#!/bin/bash

cd /opt/linux

mkdir build/
mkdir build/opus

# zig takes over the whole build, this isn't necessarily great for concurrency but let's not get in it's way, hmm?
make -f opus.mk

