FROM python:3.7-alpine

ENV FLASK_APP bootstrap.py
ENV LOG_TO_STDOUT True
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN adduser -D bootstrapper

WORKDIR /home/bootstrapper

COPY app app
COPY bootstrap.py config.py docker-entrypoint.sh requirements.txt ./

RUN python -m venv .venv
RUN .venv/bin/pip install -r requirements.txt
RUN chmod a+x docker-entrypoint.sh
RUN chown -R bootstrapper:bootstrapper ./

USER bootstrapper

EXPOSE 5000
ENTRYPOINT ["./docker-entrypoint.sh"]
