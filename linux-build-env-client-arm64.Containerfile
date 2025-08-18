FROM registry.gitlab.steamos.cloud/steamrt/sniper/sdk/arm64

# Remove dubious ownership check from git
RUN git config --global --add safe.directory '*'
