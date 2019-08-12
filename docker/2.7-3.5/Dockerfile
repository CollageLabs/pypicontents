FROM dockershelf/python:2.7
LABEL maintainer="Luis Alejandro Martínez Faneyth <luis@luisalejandro.org>"

RUN apt-get update && apt-get install python3.5

RUN pip2.7 install pypicontents
RUN pip3.5 install pypicontents

CMD ["/bin/bash"]