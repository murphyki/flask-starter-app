# Overview
`flask-starter-app` provides a boilerplate template for getting started wih [flask](https://flask.palletsprojects.com/en/1.1.x/).

Inspiration for this project was provided by these two fantastic tutorial series:
- [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by Miguel Grinberg
- [Building a python app in flask](https://hackersandslackers.com/your-first-flask-application) by hackersandslackers.com

# Deploy locally
`flask-starter-app` can be run locally using the `flask` built in development server, which is usefull for local development. 

When run in this manner, local configuration is read from the `.flaskenv` file.

`flask-starter-app` was written using python3.7 and all dependecies are defined in the `requirements.txt` file.

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
`flask-starter-app` provides both a `Dockerfile` that builds a `python alpine` based docker image of the `flask-starter-app` and a `docker-compose` file which allows the docker image to be spun up as a container and managed via `docker-compose`.

Also defined in the `docker-compose` file is a nginx reverse proxy which forwards requests from port 8080 on the host to the gunicorn WSGI server which is actually serving the `flask-starter-app` content, replacing the need to run the `flask` built in development server, which should only be used for local development as mentioned above.

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
