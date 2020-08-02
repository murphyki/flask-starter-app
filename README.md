# Overview
`flask-starter-app` provides a boilerplate template for getting started wih [flask](https://flask.palletsprojects.com/en/1.1.x/).

# Deploy locally
`flask-starter-app` can be run locally using the `flask` built in development server, which is usefull for local development. 

When run in this manner, local configuration is read from the `.flaskenv` file.

To run locally while developing:
```
flask run
```

# Deploy locally using docker-compose
`flask-starter-app` provides both a `Dockerfile` that builds a `python alpine` based docker image of the `flask-starter-app` and a `docker-compose` file which allows the docker image to be spun up as a container and managed via `docker-compose`.

Running locally is as simple as issuing the following command when inside the `flask-starter-app` project:
```
docker-compose up
```

Then view the app in a browser via the url `http://localhost:5000`

When finished, tear down the app via:
```
docker-compose down
```

# Deploy on heroku
`flask-starter-app` provides a `Procfile` which allows the app to be deployed to [heroku](https://www.heroku.com/).

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