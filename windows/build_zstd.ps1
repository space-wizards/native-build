# Run from VS 2015 native tools (x64)

$dir = New-Item -Force -ItemType Directory build/zstd
Push-Location $dir

cmake ../../../zstd/build/cmake `
    -GNinja `
    -DZSTD_BUILD_SHARED=ON `
    -DZSTD_BUILD_STATIC=OFF `
    -DZSTD_BUILD_PROGRAMS=OFF `
    -DZSTD_BUILD_TESTS=OFF `
    -DZSTD_MULTITHREAD_SUPPORT=ON `
    -DZSTD_BUILD_CONTRIB=OFF `
    -DZSTD_LEGACY_SUPPORT=OFF `
    -DCMAKE_BUILD_TYPE=Release

cmake --build .

$dest = New-Item -Force -ItemType Directory ../../../builds/zstd
Copy-Item lib/zstd.dll $dest

Pop-Location