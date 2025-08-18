FROM ubuntu:18.04

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends gcc build-essential git make cmake ca-certificates curl ninja-build pkg-config

# Python setup
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends zlib1g zlib1g-dev libssl-dev libbz2-dev libsqlite3-dev
ENV HOME="/root"
WORKDIR $HOME
RUN git clone --depth=1 https://github.com/pyenv/pyenv.git .pyenv
ENV PYENV_ROOT="$HOME/.pyenv"
ENV PATH="$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"
RUN pyenv install 3.11
RUN pyenv global 3.11

# Remove dubious ownership check from git
RUN git config --global --add safe.directory '*'
