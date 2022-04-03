ARG DOCKER_BASE
FROM $DOCKER_BASE

USER root:root
ENV DEBIAN_FRONTEND=noninteractive
COPY . /home/docker/gfootball
RUN chown -R docker:docker /home/docker/gfootball &&\
  apt-get update && apt-get --no-install-recommends install -yq git cmake build-essential \
  libgl1-mesa-dev libsdl2-dev \
  libsdl2-image-dev libsdl2-ttf-dev libsdl2-gfx-dev libboost-all-dev \
  libdirectfb-dev libst-dev mesa-utils xvfb x11vnc \
  python3-pip

USER docker:docker
RUN cd /home/docker/gfootball && \
  conda create -n football python=3.7.9 && \
  source deactivate && conda activate football && \
  pip install --upgrade pip setuptools wheel && \
  pip install psutil && \
  pip install . && \
  echo -e "\nconda activate football" >> $HOME/.bashrc && \
  source $HOME/.bashrc && source /etc/profile

WORKDIR '/home/docker'
