#!/bin/bash

# This script is used internally in the Docker container.
# Don't run it directly. Run build-glfw-openal-linux.ps1 instead

cd /opt

# Build GLFW.
pushd glfw
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=ON -DGLFW_BUILD_EXAMPLES=OFF -DGLFW_BUILD_TESTS=OFF -DGLFW_BUILD_DOCS=OFF
make -j $(nproc)
popd

# Build OpenAL.
pushd openal-soft
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j $(nproc)
popd

# Build FluidSynth
pushd fluidsynth
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release \
-Denable-aufile=OFF -Denable-dbus=OFF -Denable-ipv6=OFF -Denable-jack=OFF -Denable-ladspa=OFF \
-Denable-libsndfile=OFF -Denable-midishare=OFF -Denable-network=OFF -Denable-oss=OFF -Denable-sdl2=OFF -Denable-pulseaudio=OFF -Denable-readline=OFF \
-Denable-lash=OFF
make -j $(nproc)
popd

