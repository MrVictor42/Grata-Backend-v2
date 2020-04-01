FROM python:3.6.7
LABEL maintainer MrVictor42
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install --upgrade pip -r requirements.txt
ADD . /code/