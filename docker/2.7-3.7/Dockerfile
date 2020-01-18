FROM dockershelf/python:2.7
LABEL maintainer="Luis Alejandro Martínez Faneyth <luis@collagelabs.org>"

RUN apt-get update && apt-get install python3.7 python3-pip

RUN pip2.7 install pypicontents
RUN pip3.7 install pypicontents

CMD ["/bin/bash"]