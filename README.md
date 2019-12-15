# Medium Article: multiple services in docker
Git repository to my medium article which teaches how to run multiple Flask application/services in a single docker container

###### Medium article link: _soon_
---

## Multiple Services in Docker
#### Abstract
Recently, I passed through a tough situation at work. Me and a college were called to refector a microservice application to a monolith one, in a few days. One of ours problem was the application magnitude. First, we try to place all the services in one python molude, but with no success. Then, after some reading and tests, we solve the ploblem without much changes in code.

Here is the solution.

#### Folders tree
```
├── LICENSE
├── project
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── microservice_1
│   │   └── app.py
│   ├── microservice_2
│   │   └── app.py
│   ├── requirements.txt
│   └── run.sh
└── README.md
```

You can also see the git repository used to this article here

#### Flask applications
To simulate a microservice application, I developed a simple flask application with 2 routes: ``localhost:9001/application_1`` and ``localhost:9002/application_2``.
``` python
from flask import Flask

app = Flask(__name__)

@app.route('/application_1')
def index():
    return '<h1>Micro Service 1</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001)
```
```python
from flask import Flask

app = Flask(__name__)

@app.route('/application_2')
def index():
    return '<h1>Micro Service 2</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9002)
```
Each one is separated folder and being routed in differents ports.  
Back to my job project, the folders architecture was almost the same, but with Dockerfiles in microservices folders and a docker-compose in project folder.  

#### Dockerfile
To deploy ours applications, a Ubuntu 18.04 Docker image will be used.
```
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
```
All what Dockerfile is doing is update Ubuntu image, installing python3 and flask requirements, copying /project files into /code folder inside the container and giving us permition to access /code folder

#### Docker Compose
Here in the ``docker-compose`` i'm just creating the microservices volumes, exposing the ports and calling the ``bash run.sh`` command.
```
version: '3'

services:

  monolith:
    build:
      context: ./
      dockerfile: Dockerfile
    command: /bin/bash /code/run.sh
    volumes:
      -  ./microservice_1/:/code/microservice_1
      -  ./microservice_2/:/code/microservice_2
    ports:
      - 9001:9001
      - 9002:9002
    networks:
      - backend

networks:
  backend:
    driver: bridge
```

#### Bash file (the "magic" to run multiple services)
Here is the magic to run more then one Flask API inside onde docker. Actually, it's more linux than docker approach.  
```sh
python3 microservice_1/app.py &
python3 microservice_2/app.py
```
What the ``&`` character does is get the command execution and put it in background. So, to run more than one FLASK API inside a docker you need to execute all services in background and keep the last one in forebround (without the ``&`` character).  
```sh
python3 microservice_1/app.py &
python3 microservice_2/app.py &
python3 microservice_3/app.py &
python3 microservice_4/app.py &
python3 microservice_n/app.py
```
