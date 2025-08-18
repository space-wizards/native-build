# SS14 Native-Build

A collection of submodules providing dependencies for building [Space Station 14](https://github.com/space-wizards/space-station-14) and [RobustToolbox](https://github.com/space-wizards/RobustToolbox).

Building is handled through the `Build Natives` workflow action and relies on Github's runners to perform the actual compilation.
Local building is possible by running your platform's python file under the [scripts](./scripts/) directory.

Each platform produces an zip file containing all relevant shared libs for it, any debug symbols, and a `notes.md` giving information on where and what commit the code came from.

## Building manually

You should always start by running `git submodule update --init` to initialize the source code directories.

Note that these instructions will not necessarily allow building "clean" binaries that are suitably shippable to end users. For example, Linux builds are normally ran in a container to have a clean environment.

### Windows

Ensure you have the following things installed & available in PATH:

* MSVC
* Ninja
* CMake
* Python 3

To do the build, open up a command prompt set up for compiling with MSVC (by running e.g. `x64 Native Tools Command Prompt for VS 2022`) and then run the following commands:

```
vcpkg/bootstrap-vcpkg.bat
vcpkg/vcpkg.exe install

scripts/windows.py
```

The built files will be in `artifacts/`.

### macOS

Ensure you have the following things installed & available in PATH:

* XCode
* Ninja
* CMake
* Python 3

To do the build, open up a terminal and run the following commands:

```
vcpkg/bootstrap-vcpkg.sh
vcpkg/vcpkg install

scripts/osx.py
```

The built files will be in `artifacts/`.

### Linux

Ensure you have the following things installed & available in PATH:

* A crapload of dependencies. Check the docs of the libraries we're using and keep installing `-dev` packages until it builds.
* Ninja
* CMake
* Python 3

To do the build, open up a terminal and run the following commands:

```
vcpkg/bootstrap-vcpkg.sh
vcpkg/vcpkg install

scripts/linux-server.py
scripts/linux.py
```

The built files will be in `artifacts/`.
