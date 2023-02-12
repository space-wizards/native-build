# Build all vcpkg-provided packages on Windows.

TRIPLET=$1
RID=$2

docker run --rm -v "$(pwd)/..:/opt" ss14-native-build:1.0 /opt/vcpkg/vcpkg install --triplet "$TRIPLET" "sdl2[vulkan]" "openal-soft" "freetype[core]" "glfw3"

TO_COPY=("libSDL2-2.0.so.0" "libfreetype.so.6" "libglfw.so.3" "libopenal.so.1")

mkdir -p "builds/$RID"

for native in ${TO_COPY[@]}; do
  cp "vcpkg/installed/$TRIPLET/lib/$native" "builds/$RID/$native"
done
