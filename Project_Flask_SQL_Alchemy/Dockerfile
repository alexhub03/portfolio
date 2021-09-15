# Dockerfile - blueprint for building the image, template for running the container
# Image - tempalate for running containers
# Container - the actual running process of the package project

FROM ubuntu:latest

RUN apt-get update -y && apt-get install -y python3-pip python-dev

EXPOSE 80
EXPOSE 5000
EXPOSE 5433
EXPOSE 6000

WORKDIR /docker-flask

ADD . /docker-flask

RUN pip3 install flask_sqlalchemy psycopg2-binary
RUN pip3 --no-cache-dir install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD ["app.py"]

