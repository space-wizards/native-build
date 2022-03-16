#!/bin/bash

cd /opt/linux

mkdir build/
mkdir build/zstd

cd build/zstd

cmake ../../../zstd/build/cmake \
    -DZSTD_BUILD_SHARED=ON \
    -DZSTD_BUILD_STATIC=OFF \
    -DZSTD_BUILD_PROGRAMS=OFF \
    -DZSTD_BUILD_TESTS=OFF \
    -DZSTD_MULTITHREAD_SUPPORT=ON \
    -DZSTD_BUILD_CONTRIB=OFF \
    -DZSTD_LEGACY_SUPPORT=OFF \
    -DCMAKE_BUILD_TYPE=Release

make -j $(nproc)

