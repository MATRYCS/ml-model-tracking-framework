FROM ubuntu:22.04

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN : \
    && apt-get update --fix-missing \
    && apt-get upgrade --yes \
    && apt-get install --yes --quiet git libyaml-cpp-dev libyaml-dev python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && :

COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir -Ur requirements.txt