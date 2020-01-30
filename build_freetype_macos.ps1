#!/usr/bin/env pwsh

if (test-path builds/freetype)
{
    write-host "removing previous build directory"
    remove-item -recurse builds/freetype
}

new-item -itemtype directory builds/freetype | Out-Null

set-location builds/freetype

cmake ../../freetype -DCMAKE_RELEASE_TYPE=Release -DBUILD_SHARED_LIBS=true
$procCount = [Environment]::ProcessorCount
make "-j$procCount"