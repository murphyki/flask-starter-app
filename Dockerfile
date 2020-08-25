FROM python:3.7-slim-buster

ENV APP_NAME 'Flask Starter App'
ENV FLASK_APP 'bootstrap.py'
ENV FLASK_ENV 'production'
ENV DEBUG 0
ENV LOG_TO_STDOUT True
ENV LOG_FOLDER_NAME '.logs'
ENV LOG_FILE_NAME 'app.log'
ENV SECRET_KEY 'some-secret'
ENV DATABASE_URL 'postgresql://postgres:postgres@db:5432/database'
ENV SQLALCHEMY_TRACK_MODIFICATIONS False
ENV SQLALCHEMY_ECHO False
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN groupadd bootstrapper && \
    useradd -m -g bootstrapper bootstrapper

WORKDIR /home/bootstrapper

COPY app app
COPY bootstrap.py bootstrap.py
COPY config.py config.py
COPY docker-entrypoint.sh docker-entrypoint.sh
COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    chmod a+x docker-entrypoint.sh && \
    chown -R bootstrapper:bootstrapper ./

USER bootstrapper

EXPOSE 5000

ENTRYPOINT ["./docker-entrypoint.sh"]

CMD ["gunicorn", "-b", ":5000", "bootstrap:app"]
