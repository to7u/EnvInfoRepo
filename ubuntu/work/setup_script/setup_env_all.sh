#! /bin/sh
# this is setup shell script .

# package
sudo apt-get update && apt-get install -y \
    git \
    vim \
    less \
    wget \
    curl \
    net-tools \
    sysstat \
    network-manager \
    build-essential \
    libffi-dev \
    libssl-dev \
    zlib1g-dev \
    liblzma-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    libopencv-dev \
    libxml2-dev \
    libcurl4-openssl-dev \
    libjpeg-dev \
    libpng-dev \
    libmcrypt-dev \
    libtidy-dev \
    libxslt-dev \
    libzip-dev \
    tk-dev \
    autoconf \
    pkg-config \
    re2c \
    bison

# os standard python install patern    
#    python3\
#    python3-pip\

# === vagrant version ===
# === anyenv install ===
git clone https://github.com/riywo/anyenv ~/.anyenv
echo 'export PATH="$HOME/.anyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(anyenv init -)"' >> ~/.bashrc
exec $SHELL -l

echo y | anyenv install --init 
exec $SHELL -l

anyenv install rbenv
anyenv install pyenv
anyenv install phpenv
exec $SHELL -l

# python install 3.8.6
pyenv install 3.8.6
pyenv rehash
pyenv global 3.8.6

# python module install
pip install --upgrade pip setuptools
pip install pillow netifaces requests bs4 lxml

# ruby install 2.5.7
rbenv install 2.5.7
rbenv rehash
rbenv global 2.5.7

# php install 7.2.22
phpenv install 7.2.22
phpenv rehash
phpenv global 7.2.22
