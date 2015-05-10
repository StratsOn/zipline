#A Container for QuantStudio applications
FROM ubuntu:14.04
MAINTAINER bleedtodry@hotmail.com

COPY sources.list /etc/apt/
RUN apt-get update \
        && apt-get install -y build-essential \
        && apt-get install -y curl \
        && apt-get install -y python-pip \
        && apt-get install -y python-dev \
	&& apt-get install -y python-logbook \
	&& apt-get install -y python-numpy \
	&& apt-get install -y python-pandas

RUN pip install kafka-python -i http://pypi.v2ex.com/simple

#CMD ["echo","QuantStudio"]
ADD . /data/engine        
