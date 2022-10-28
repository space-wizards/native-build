#!/bin/bash

PLATFORM="osx-`uname -m`"
ANSI_GREEN='\033[0;32m'
ANSI_RESET='\033[0m'

# set this to 1 if you want everything to be completely isolated from your global brew install,
# but it forces some things to be built from source.
USE_LOCAL_BUILD_ENV=

brew install --quiet jq

echo "Assembling native libraries for $PLATFORM..."

if [ -z USE_LOCAL_BUILD_ENV ]; then

    echo "Setting up homebrew build environment..."

    git clone https://github.com/Homebrew/brew brewbuild
    mkdir -p brewbuild
    curl -L https://github.com/Homebrew/brew/tarball/3.6.7 | tar xz --strip 1 -C brewbuild
    eval "$(brewbuild/bin/brew shellenv)"

else

    echo <<EOF 
This will build using your global homebrew install. This may cause some errors to be 
printed about linking, but if you have newer versions of the libraries this script 
installs, these errors are because the old versions will not overwrite the new versions,
and should be able to coexist without any problem.

EOF

fi

set -e 
brew -v
set +e

echo "Packages will be built at $HOMEBREW_PREFIX"

# i find these names for things extremely stupid, but that's what brew calls them
TAP_NAME=swbuild/local
brew tap-new --no-git $TAP_NAME
TAP_PATH=`brew tap-info --json swbuild/local | jq -r '.[0].path'`

grab() {
    output_dir=$1
    version=$2
    source=$3
    
    target=$output_dir/$version/$PLATFORM/

    mkdir -p $target
    chmod 0644 $source
    cp -f $source $target
    echo -e $ANSI_GREEN"Library file obtained: " `ls $target` $ANSI_RESET
    echo
}

brewgrab() {
    package=$1
    version=$2
    library_file=$3
    output_dir=$4

    if [ -z $output_dir ]; then output_dir=$package; fi

    if [ ! -f "$TAP_PATH/Formula/$package@$version.rb" ]; then 
        brew extract --version=$version $package $TAP_NAME
    else
        echo "Package build script already retrieved from github for $package@$version"
    fi

    brew install $package@$version
    set -e
    grab $output_dir $version "$HOMEBREW_PREFIX/Cellar/$package@$version/*/$library_file"
    set +e
}

mkdir -p ../builds

pushd ../builds

    brewgrab freetype 2.10.1 lib/libfreetype.6.dylib
    brewgrab glfw 3.3.2 lib/libglfw.3.dylib
    brewgrab libsodium 1.0.18 lib/libsodium.dylib 

    # other archs are using 2.1.0 of fluidsynth but that patchlevel does not exist on brew
    brewgrab fluid-synth 2.1.8 lib/libfluidsynth.2.dylib fluidsynth

    # we build zstd with different options than brew uses
    # it would be:
    #   brewgrab zstd 1.5.2 lib/libzstd.dylib
popd


echo "Building zstd..."
set -e
./build-zstd.sh
set +e
echo

echo "Building swnfd..."
set -e
../swnfd/link_macos.sh
grab swnfd 0.1.0 ../swnfd/build/darwin_multiarch/libswnfd.dylib 
set +e

echo
ls ../builds/*/*/$PLATFORM/*
echo -e $ANSI_GREEN"All done." $ANSI_RESET
