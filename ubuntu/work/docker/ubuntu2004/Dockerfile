FROM ubuntu:20.04

RUN apt-get update -y && \
    apt-get install -y tzdata

# timezone setting
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y \
    vim \
    wget \
    net-tools \
    python3 \
    python3-pip \
    less \
    network-manager \
    git

RUN pip install pillow netifaces requests bs4 lxml bottle
