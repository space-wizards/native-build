#!/usr/bin/env pwsh

docker run --rm -v "${pwd}/..:/opt" ss14-native-build:1.1 "/bin/bash" "/opt/linux/__build-opus.sh"

new-item -Force -itemtype Directory ../builds/opus/
copy-item build/opus/libopus.so.0 ../builds/opus/
copy-item build/opus/libopus.dll ../builds/opus/
copy-item build/opus/libopus.dylib ../builds/opus/

