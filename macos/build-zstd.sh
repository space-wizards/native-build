#!/bin/bash

mkdir build/
mkdir build/zstd

pushd build/zstd

cmake ../../../zstd/build/cmake \
    -DZSTD_BUILD_SHARED=ON \
    -DZSTD_BUILD_STATIC=OFF \
    -DZSTD_BUILD_PROGRAMS=OFF \
    -DZSTD_BUILD_TESTS=OFF \
    -DZSTD_MULTITHREAD_SUPPORT=ON \
    -DZSTD_BUILD_CONTRIB=OFF \
    -DZSTD_LEGACY_SUPPORT=OFF \
    -DCMAKE_BUILD_TYPE=Release

# I don't know how to do nproc on mac and this 10 year old iMac has 4 cores so have fun.
make -j 4

popd

mkdir ../builds
mkdir ../builds/zstd
mkdir ../builds/zstd/osx-x64
cp build/zstd/lib/libzstd.dylib ../builds/zstd/osx-x64/libzstd.dylib

