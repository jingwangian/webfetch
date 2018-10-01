FROM centos/python-36-centos7
LABEL maintainer "Ian Wang <jingwangian@gmail.com>"

USER root

# Enable EPEL
# RUN sed -i s/enabled=1/enabled=0/ /etc/yum/pluginconf.d/fastestmirror.conf \
#     && sed -i s/enabled=1/enabled=0/ /etc/yum/pluginconf.d/ovl.conf
# RUN yum -y install epel-release \
#     && yum -y clean all

WORKDIR /tmp

RUN chsh --shell /bin/bash root

RUN wget http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
RUN rpm -ivh epel-release-latest-7.noarch.rpm
