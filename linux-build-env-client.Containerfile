FROM registry.gitlab.steamos.cloud/steamrt/sniper/sdk

# Remove dubious ownership check from git
RUN git config --global --add safe.directory '*'
