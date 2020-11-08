FROM python:3.8
USER root
COPY ["requirements.txt", "/requirements.txt"]
RUN apt update -y && apt upgrade -y && \
    pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install -r requirements.txt
