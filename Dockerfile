FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN apt-get update --fix-missing
RUN apt-get install -y \
    python3-pip \
    python-dev \
    libpq-dev 
# gettext \
# libreadline-dev \
# libssl-dev \
# libjpeg-dev \
# libfreetype6-dev \
# binutils \
# libproj-dev \
# setuptools


RUN apt-get autoclean -y \
    clean -y \
    autoremove -y

RUN pip3 install --upgrade pip

RUN mkdir /code
VOLUME /code

COPY requeriments.txt /code/requeriments.txt

WORKDIR /code
RUN pip install -r requeriments.txt

COPY . /code





# Install requirements
CMD ["python3"]
