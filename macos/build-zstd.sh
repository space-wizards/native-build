#!/bin/bash

VERSION=1.5.2
PLATFORM=osx-`uname -m`
LIBRARY_NAME=zstd
LIBRARY_FILE=lib/libzstd.dylib


# /-- boilerplate --\
ANSI_GREEN='\033[0;32m'
ANSI_RESET='\033[0m'

INPUT_DIR=../$LIBRARY_NAME
BUILD_DIR=build/$LIBRARY_NAME
OUTPUT_DIR=../builds/$LIBRARY_NAME/$VERSION/$PLATFORM

set -e 
# \-- boilerplate --/


# Actually do the build

cmake -S $INPUT_DIR/build/cmake -B $BUILD_DIR \
    -DZSTD_BUILD_SHARED=ON \
    -DZSTD_BUILD_STATIC=OFF \
    -DZSTD_BUILD_PROGRAMS=OFF \
    -DZSTD_BUILD_TESTS=OFF \
    -DZSTD_MULTITHREAD_SUPPORT=ON \
    -DZSTD_BUILD_CONTRIB=OFF \
    -DZSTD_LEGACY_SUPPORT=OFF \
    -DCMAKE_BUILD_TYPE=Release

pushd $BUILD_DIR
make -j `sysctl -n hw.logicalcpu`
popd


# /-- boilerplate --\
mkdir -p $OUTPUT_DIR
cp $BUILD_DIR/$LIBRARY_FILE $OUTPUT_DIR/
echo -e $ANSI_GREEN"Library file obtained: " `ls $OUTPUT_DIR` $ANSI_RESET
# \-- boilerplate --/
