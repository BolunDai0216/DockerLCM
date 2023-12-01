FROM ubuntu:20.04

# Set noninteractive installation (to avoid getting stuck during building)
ARG DEBIAN_FRONTEND=noninteractive

# Update and install basic packages
RUN apt-get update && apt-get install -y \
    build-essential \
    python3 \
    python3-pip \
    git \
    libglib2.0-dev \
    cmake

WORKDIR /home

RUN git clone https://github.com/lcm-proj/lcm.git

WORKDIR /home/lcm

RUN mkdir build 

WORKDIR /home/lcm/build

RUN cmake ..
RUN cmake --build .
RUN cmake --install .

RUN mkdir DockerLCM

WORKDIR /home/DockerLCM

COPY . /home/DockerLCM

ENV PYTHONPATH "/usr/local/lib/python3.8/site-packages:${PYTHONPATH}"

CMD ["bash"]