FROM ubuntu:18.04
RUN mkdir /code
WORKDIR /code

RUN apt-get update && apt-get install -y \
        python3 \
        python3-pip \
        python3-setuptools \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /code
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /code

RUN chmod +x -R /code/
