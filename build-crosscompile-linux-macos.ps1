#!/usr/bin/env pwsh

# Make sure to run build-build-env.ps1 first to build the Docker container.
# Then make sure to run build-glfw-openal-linux.ps1 as this prepares necessary files (precomputed tables).
docker run --rm -v "${pwd}:/opt" ss14-native-build:1.0 "/bin/bash" "/opt/__build-crosscompile-linux-macos.sh"

