set(VCPKG_TARGET_ARCHITECTURE x64)
set(VCPKG_CRT_LINKAGE dynamic)
set(VCPKG_LIBRARY_LINKAGE static)

set(VCPKG_CMAKE_SYSTEM_NAME Linux)

if(PORT MATCHES fluidsynth)
    set(VCPKG_LIBRARY_LINKAGE dynamic)
    set(VCPKG_FIXUP_ELF_RPATH ON)

    set(VCPKG_CXX_FLAGS -Wl,-Bsymbolic)
    set(VCPKG_C_FLAGS -Wl,-Bsymbolic)
endif()
