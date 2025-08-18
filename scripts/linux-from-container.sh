#/usr/bin/env bash

set -xeu

cd /work

vcpkg/bootstrap-vcpkg.sh
vcpkg/vcpkg install --triplet=$2
scripts/linux.py --rid=$1
