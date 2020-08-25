#!/bin/bash

echo "APP_NAME=${APP_NAME}"
echo "FLASK_APP=${FLASK_APP}"
echo "FLASK_ENV=${FLASK_ENV}"
echo "DEBUG=${DEBUG}"
echo "LOG_TO_STDOUT=${LOG_TO_STDOUT}"
echo "LOG_FOLDER_NAME=${LOG_FOLDER_NAME}"
echo "LOG_FILE_NAME=${LOG_FILE_NAME}"
echo "SECRET_KEY=${SECRET_KEY}"
echo "SQLALCHEMY_DATABASE_URI=${SQLALCHEMY_DATABASE_URI}"
echo "SQLALCHEMY_TRACK_MODIFICATIONS=${SQLALCHEMY_TRACK_MODIFICATIONS}"
echo "SQLALCHEMY_ECHO=${SQLALCHEMY_ECHO}"
echo "PYTHONDONTWRITEBYTECODE=${PYTHONDONTWRITEBYTECODE}"
echo "PYTHONUNBUFFERED=${PYTHONUNBUFFERED}"

exec "$@"