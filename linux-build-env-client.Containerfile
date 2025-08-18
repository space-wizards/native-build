FROM registry.gitlab.steamos.cloud/steamrt/sniper/sdk

# Python setup
ENV HOME="/root"
WORKDIR $HOME
RUN git clone --depth=1 https://github.com/pyenv/pyenv.git .pyenv
ENV PYENV_ROOT="$HOME/.pyenv"
ENV PATH="$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"
RUN pyenv install 3.11
RUN pyenv global 3.11

# Remove dubious ownership check from git
RUN git config --global --add safe.directory '*'
