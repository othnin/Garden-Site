FROM python:3.10-slim-buster

RUN apt-get update && \
    apt-get install -y software-properties-common python3-pip python3-dev
    
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

#create dir for the app user
RUN mkdir -p /home/app

#create appropriate dir
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME


RUN addgroup --system appgroup
RUN adduser --system appuser
RUN usermod -a -G appgroup appuser

# copy project
COPY . $APP_HOME
COPY scripts/start-celerybeat.sh .
RUN chmod +x ./start-celerybeat.sh

COPY scripts/start-celeryworker.sh .
RUN chmod +x ./start-celeryworker.sh

COPY scripts/start-django.sh .
RUN chmod +x ./start-django.sh


RUN chown -R appuser:appgroup $APP_HOME
USER appuser










