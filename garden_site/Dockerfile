FROM python:3.10-slim-buster

RUN apt-get update && \
    apt-get install -y software-properties-common python3-pip python3-dev
    
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY . /app
