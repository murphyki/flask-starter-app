FROM python:3.7-slim-buster

ENV FLASK_APP bootstrap.py
ENV LOG_TO_STDOUT True
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY app ./app
COPY bootstrap.py ./bootstrap.py
COPY config.py ./config.py
COPY docker-entrypoint.sh ./docker-entrypoint.sh
COPY requirements.txt ./requirements.txt

RUN pip install --upgrade pip \
    && pip install -r ./requirements.txt \
    && chmod a+x ./docker-entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["./docker-entrypoint.sh"]
