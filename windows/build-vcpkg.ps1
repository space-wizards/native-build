# Build all vcpkg-provided packages on Windows.

param(
    [Parameter(Position = 0, mandatory = $true)]
    [string]$triplet,

    [Parameter(Position = 1, mandatory = $true)]
    [string]$rid
)

Push-Location $(Join-Path $PSScriptRoot "..")

vcpkg\vcpkg.exe install --triplet $triplet "sdl2[vulkan]" "openal-soft" "freetype[core]" "glfw3"

$files_to_copy = @("glfw3.dll", "SDL2.dll", "OpenAL32.dll", "freetype.dll", "libfluidsynth-3.dll", "glib-2.0-0.dll", "iconv-2.dll", "intl-8.dll", "pcre2-8.dll")
New-Item -ItemType Directory -Force "builds"
New-Item -ItemType Directory -Force "builds\$rid"

$files_to_copy | ForEach-Object { 
    Copy-Item "vcpkg\installed\$triplet\bin\$_" "builds\$rid\$_"
}
