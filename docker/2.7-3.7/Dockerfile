FROM dockershelf/debian:buster
LABEL maintainer="Luis Alejandro Martínez Faneyth <luis@collagelabs.org>"

RUN apt-get update && apt-get install \
    python3.7 python3-pip python3-setuptools python3-wheel \
    python2.7 python-pip python-setuptools python-wheel

RUN pip2 install pypicontents
RUN pip3 install pypicontents

CMD ["/bin/bash"]
