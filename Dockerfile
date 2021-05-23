FROM ubuntu:latest

ARG APP_NAME=redes
ENV APP_NAME=${APP_NAME}

RUN apt update && apt upgrade
RUN apt install -y net-tools
RUN apt install -y iputils-ping
RUN apt install -y python3
RUN apt install -y python3-pip

WORKDIR /home/${APP_NAME}

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

WORKDIR /home/${APP_NAME}/src
