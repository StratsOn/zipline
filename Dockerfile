#A Container for QuantStudio applications
FROM ubuntu:14.04
MAINTAINER bleedtodry@hotmail.com

COPY sources.list /etc/apt/
RUN apt-get update \
        && apt-get install -y build-essential \
        && apt-get install -y python-pip \
        && apt-get install -y python-dev

RUN pip install logbook pandas

#CMD ["echo","QuantStudio"]
ADD . /data/engine        
