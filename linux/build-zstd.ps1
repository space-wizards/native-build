#!/usr/bin/env pwsh

docker run --rm -v "${pwd}/..:/opt" ss14-native-build:1.0 "/bin/bash" "/opt/linux/__build-zstd.sh"

new-item -Force -itemtype Directory ../builds/zstd/
copy-item build/zstd/lib/libzstd.so ../builds/zstd/

