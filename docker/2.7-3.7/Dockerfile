FROM dockershelf/python:2.7
LABEL maintainer="Luis Alejandro Martínez Faneyth <luis@collagelabs.org>"

RUN apt-get update && apt-get install python3.7 python3-pip \
    python3-setuptools python3-wheel

RUN pip2.7 install pypicontents
RUN pip3 install pypicontents

CMD ["/bin/bash"]