FROM webfetch/base
LABEL maintainer "Ian Wang <jingwangian@gmail.com>"

USER root

# Install development tools


## Install packages required to compile required python modules

RUN pip3 install --upgrade pip

# Install requirements + build/test tools
COPY requirements.txt /tmp/requirements.txt
RUN pip3 --no-cache install -r /tmp/requirements.txt

# Setup app volumes

# Setup a runtime user
RUN adduser --home /opt/news -u 1000 news

# Setup code location
VOLUME /opt/news
WORKDIR /opt/news

USER news
