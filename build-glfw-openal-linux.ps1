#!/usr/bin/env pwsh

# Make sure to run build-build-env.ps1 first to build the Docker container.
docker run --rm -v "${pwd}:/opt" ss14-native-build:1.0 "/bin/bash" "/opt/__build-glfw-openal.sh"

new-item -Force -itemtype Directory builds/glfw/
new-item -Force -itemtype Directory builds/openal/
new-item -Force -itemtype Directory builds/fluidsynth/

copy-item glfw/build/src/libglfw.so.3.3 builds/glfw/libglfw.so
copy-item openal-soft/build/libopenal.so.1.20.1 builds/openal/libopenal.so
copy-item fluidsynth/build/src/libfluidsynth.so.2.3.3 builds/fluidsynth/libfluidsynth.so

