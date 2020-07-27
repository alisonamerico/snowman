# snowman

An application for users to create and explore tourist spots on a map.

Application available at: https://touristspots.herokuapp.com

![Django CI](https://github.com/alisonamerico/snowman/workflows/Django%20CI/badge.svg)
[![codecov](https://codecov.io/gh/alisonamerico/snowman/branch/master/graph/badge.svg)](https://codecov.io/gh/alisonamerico/snowman)
[![Updates](https://pyup.io/repos/github/alisonamerico/snowman/shield.svg)](https://pyup.io/repos/github/alisonamerico/snowman/)
[![Python 3](https://pyup.io/repos/github/alisonamerico/snowman/python-3-shield.svg)](https://pyup.io/repos/github/alisonamerico/snowman/)

Dependencies used in the project:

```console
[tool.poetry.dependencies]
python = "^3.8"
django = "^3.0.8"
gunicorn = "^20.0.4"
python-decouple = "^3.3"
dj-database-url = "^0.5.0"
psycopg2-binary = "^2.8.5"
dj-static = "^0.0.6"
djangorestframework = "^3.11.0"
djangorestframework-jwt = "^1.11.0"
django-cors-headers = "^3.4.0"
Pillow = "^7.2.0"
djangorestframework-gis = "^0.15"
django-filter = "^2.3.0"

[tool.poetry.dev-dependencies]
flake8 = "^3.8.3"
autopep8 = "^1.5.3"
pytest-django = "^3.9.0"
pytest-cov = "^2.10.0"
codecov = "^2.1.8"
```

## Prerequisite Installed:

- Docker
- Docker Compose

For Linux(Ubuntu):
https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-engine---community-1

For Mac:
https://docs.docker.com/docker-for-mac/install/

For Windows:
https://docs.docker.com/docker-for-windows/install/

## How to execute:

```console
git clone https://github.com/alisonamerico/snowman.git
cd snowman
docker-compose build
docker-compose up or docker-compose up -d
```

Create SuperUser:

```console
docker-compose run web python manage.py createsuperuser
```

Inform:

```console
 - email
 - password
```

List the urls that exist

```console
http://0.0.0.0:8000/api/v1/
```

API Root

```console
http://0.0.0.0:8000/api/v1/touristspots/
http://0.0.0.0:8000/api/v1/favorites/
```

Note: But to view, you must first have:

```console
http://0.0.0.0:8000/api/v1/auth/api-token-auth/
```

To access url:

```console
 - email
 - password
```

Configuration for accessing urls
When you’re done, don’t forget to close down your Docker container.

```console
docker-compose down
```

Run the tests:

```shell script
pytest coffee --cov=coffee
```
