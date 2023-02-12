FROM ubuntu:20.04

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends xorg-dev gcc build-essential git make cmake libpulse-dev libasound-dev zip tar curl unzip ca-certificates
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends libglib2.0-dev
# SDL2 dependencies
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends build-essential git make autoconf automake libtool pkg-config cmake ninja-build gnome-desktop-testing libasound2-dev libpulse-dev libaudio-dev libjack-dev libsndio-dev libsamplerate0-dev libx11-dev libxext-dev libxrandr-dev libxcursor-dev libxfixes-dev libxi-dev libxss-dev libwayland-dev libxkbcommon-dev libdrm-dev libgbm-dev libgl1-mesa-dev libgles2-mesa-dev libegl1-mesa-dev libdbus-1-dev libibus-1.0-dev libudev-dev fcitx-libs-dev
RUN DEBIAN_FRONTEND=noninteractive apt-get upgrade -y
