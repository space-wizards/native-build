#!/bin/bash

cd /opt/linux

mkdir -p build/sdl

cd build/sdl

cmake ../../../SDL/                   \
    -DCMAKE_BUILD_TYPE=Release        \
    -DSDL_STATIC=OFF                  \
    -DSDL_SHARED=ON                   \
    -DSDL_TEST=OFF

make -j $(nproc)

