FROM python:3.7-slim-buster

ENV FLASK_APP bootstrap.py
ENV LOG_TO_STDOUT True
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN groupadd bootstrapper
RUN useradd -m -g bootstrapper bootstrapper

WORKDIR /home/bootstrapper

COPY app app
COPY bootstrap.py bootstrap.py
COPY config.py config.py
COPY docker-entrypoint.sh docker-entrypoint.sh
COPY requirements.txt requirements.txt

RUN python -m venv .venv
RUN .venv/bin/pip install --upgrade pip
RUN .venv/bin/pip install --no-cache-dir -r requirements.txt
RUN chmod a+x docker-entrypoint.sh
RUN chown -R bootstrapper:bootstrapper ./

USER bootstrapper

EXPOSE 5000

ENTRYPOINT ["./docker-entrypoint.sh"]
