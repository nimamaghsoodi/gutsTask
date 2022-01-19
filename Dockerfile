FROM python:3.9-slim-buster
MAINTAINER Nima Maghsoodi
ENV PYTHONUNBUFFERED 1
RUN mkdir /apitask
WORKDIR /apitask
ADD . /apitask
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD python3 manage.py runserver 0.0.0.0:8080