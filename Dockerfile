
FROM python:3.7-alpine3.8

RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev
RUN pip3 install pipenv
ENV LIBRARY_PATH=/lib:/usr/lib

COPY . /usr/server
WORKDIR /usr/server
RUN pipenv install --system --deploy 

ENV FLASK_APP=src/main.py
EXPOSE 5000
CMD ["python", "src/main.py"]