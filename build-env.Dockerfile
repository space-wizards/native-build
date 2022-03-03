FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y --no-install-recommends xorg-dev gcc build-essential git make cmake libpulse-dev libasound-dev
RUN apt-get install -y --no-install-recommends libglib2.0-dev
RUN apt-get install -y --no-install-recommends wget
RUN wget --no-check-certificate https://ziglang.org/download/0.9.1/zig-linux-x86_64-0.9.1.tar.xz
RUN echo be8da632c1d3273f766b69244d80669fe4f5e27798654681d77c992f17c237d7 zig-linux-x86_64-0.9.1.tar.xz | sha256sum -c -
RUN tar -xJf zig-linux-x86_64-0.9.1.tar.xz ; mv zig-linux-x86_64-0.9.1 zig ; rm zig-linux-x86_64-0.9.1.tar.xz
RUN ln -s /zig/zig /bin/zig

