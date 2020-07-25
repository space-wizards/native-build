FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y --no-install-recommends xorg-dev gcc build-essential git make cmake libpulse-dev libasound-dev

