# Overview
`flask-starter-app` provides a boilerplate template for getting started wih [flask](https://flask.palletsprojects.com/en/1.1.x/).

Inspiration for this project was provided by these two fantastic tutorial series:
- [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by Miguel Grinberg
- [Building a python app in flask](https://hackersandslackers.com/your-first-flask-application) by hackersandslackers.com

# Development setup
`flask-starter-app` was written using python3.7 and all dependencies are defined in the `requirements.txt` file.

To install these dependencies, create a python virtual environment based on python3.7 as follows (i'm using `virtualenv` there are [alternatives](https://realpython.com/python-virtual-environments-a-primer/)):
```
virtualenv --python=python3.7 .venv
```

Activate the virtual environment:
```
source .venv/bin/activate
```

Install dependencies:
```
pip install -r requirements.txt
```

Run the app:
```
flask run
```

# Deploy locally using docker-compose
`flask-starter-app` provides both a `Dockerfile` that builds a `python slim-buster` based docker image of the `flask-starter-app` and a `docker-compose` file which allows the docker image to be spun up as a container and managed via `docker-compose`.

Defined in the `docker-compose` file are a number of services:
- the main `flask-starter-app` app service
- the nginx reverse proxy service which forwards requests to the app service
- the database service which will eventually used to store content

By default the `flask-starter-app` container runs the gunicorn WSGI server which is actually serving the `flask-starter-app` content.

The gunicorn WSGI server command is overridden in the `docker-compose` file which instead runs the `flask` built in development server.
Also defined in the `docker-compose` file is a bind mount for the `flask-starter-app` code which allows code changes to be reloaded without the need to rebuild the container.

The `docker-compose` file depends on a number of environment variables being available which are automatically loaded from a `.env` file located at the root of the project file tree. A `.env.sample` file is provided which provides sane defaults for a local development setup. Just rename the file to `.env` and thats it.

Running locally is as simple as issuing the following command when inside the `flask-starter-app` project:
```
docker-compose up
```

Then view the app in a browser via the url `http://localhost:8080`

When finished, tear down the app via:
```
docker-compose down
```

# Deploy on heroku
`flask-starter-app` provides a `Procfile` which allows the app to be deployed to [heroku](https://www.heroku.com/).

The following steps are based on [this](https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true) excellent article provided by heroku.

First install the heroku commandline utility, see [here](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) for options:
```
sudo snap install heroku --classic
```

Next, log into heroku using your heroku credentials:
```
heroku login
```

Next, `git clone` the `flask-starter-app`.

Next, change directory into the `flask-starter-app` project.

Now create a heroku app:
```
heroku create flask-app-starter
```

Push code to heroku:
```
git push heroku master
```

Scale the app:
```
heroku ps:scale web=1
```

View in a browser:
```
heroku open
```

View logs:
```
heroku logs
```
or
```
heroku logs --tail
```

When finished, scale down the app:
```
heroku ps:scale web=0
```
