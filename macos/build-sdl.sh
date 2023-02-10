#!/bin/bash

set -e

mkdir -p "build/sdl/"
pushd "build/sdl"

mkdir "arm64"
mkdir "x64"

(
    # ARM64 build
    cmake -S ../../../sdl/ -B arm64       \
        -DCMAKE_BUILD_TYPE=Release        \
        -DCMAKE_OSX_DEPLOYMENT_TARGET=11  \
        -DCMAKE_OSX_ARCHITECTURES=arm64   \
        -DSDL_STATIC=OFF                  \
        -DSDL_SHARED=ON                   \
        -DSDL_TEST=OFF

    cmake --build arm64 --parallel
) &

(
    # x64 build
    cmake -S ../../../sdl/ -B x64           \
        -DCMAKE_BUILD_TYPE=Release          \
        -DCMAKE_OSX_DEPLOYMENT_TARGET=10.15 \
        -DCMAKE_OSX_ARCHITECTURES=x86_64    \
        -DSDL_STATIC=OFF                    \
        -DSDL_SHARED=ON                     \
        -DSDL_TEST=OFF

    cmake --build x64 --parallel
) &

wait

popd

mkdir -p builds/sdl/osx-arm64
mkdir -p builds/sdl/osx-x64

cp build/sdl/arm64/libSDL2-2.0.0.dylib builds/sdl/osx-arm64/
cp build/sdl/x64/libSDL2-2.0.0.dylib builds/sdl/osx-x64/