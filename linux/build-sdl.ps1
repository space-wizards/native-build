#!/usr/bin/env pwsh

docker run --rm -v "${pwd}/..:/opt" ss14-native-build:1.0 "/bin/bash" "/opt/linux/__build-sdl.sh"

new-item -Force -itemtype Directory ../builds/sdl/
copy-item build/sdl/libSDL2-2.0.so ../builds/sdl/

