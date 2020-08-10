# snowman

An application for users to create and explore tourist spots on a map.

Application available at: https://touristspots.herokuapp.com

![Django CI](https://github.com/alisonamerico/snowman/workflows/Django%20CI/badge.svg)
[![codecov](https://codecov.io/gh/alisonamerico/snowman/branch/master/graph/badge.svg)](https://codecov.io/gh/alisonamerico/snowman)
[![Updates](https://pyup.io/repos/github/alisonamerico/snowman/shield.svg)](https://pyup.io/repos/github/alisonamerico/snowman/)
[![Python 3](https://pyup.io/repos/github/alisonamerico/snowman/python-3-shield.svg)](https://pyup.io/repos/github/alisonamerico/snowman/)

Processes used in project development:

Continuous Delivery:

- Integration with Poetry, Github(Actions) and Pyup

- Automatic Deploy for Heroku

- Pytest: To set up and build automated tests for Django.

- Codecov: For Test Coverage

- python-decouple: To decouple application instance settings.

- Docker: Run applications by using containers.

Dependencies used in the project:

```toml
[tool.poetry]
name = "snowman"
version = "0.1.0"
description = ""
authors = ["alisonamerico <alison.americo@gmail.com>"]

[tool.poetry.dependencies]
python = "^3.8"
django = "^3.0.8"
gunicorn = "^20.0.4"
python-decouple = "^3.3"
dj-database-url = "^0.5.0"
psycopg2-binary = "^2.8.5"
dj-static = "^0.0.6"
djangorestframework = "^3.11.0"
django-cors-headers = "^3.4.0"
Pillow = "^7.2.0"
djangorestframework-gis = "^0.15"
django-filter = "^2.3.0"
dj-rest-auth = "^1.1.1"
django-allauth = "^0.42.0"

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

![home](readme-images/0_home.png)

## How to execute:

```console
git clone https://github.com/alisonamerico/snowman.git
cd snowman
cp contrib/env-sample .env
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

How to generate a token:

![create_token](readme-images/1_create_token.png)

Url:

```console
http://0.0.0.0:8000/api/v1/auth/api-token-auth/
```

Enter email and password created:

Obs.: I'm using a custom user, so enter your email in the username field.

```json
{
  "username": "admin@snowman.com",
  "password": "labs@123"
}
```

Method HTTP:

```console
POST
```

Generated token:

![genered_token](readme-images/2_generated_token.png)

Copy the generated token, enter the key and value in Headers:

![headers](readme-images/3_headers.png)

```console
Key:
Authorization

Value:
Token + key genered
```

To access list of available urls:

```console
http://0.0.0.0:8000/api/v1/
```

![list_urls](readme-images/4_list_urls.png)

API Root:

```console
http://0.0.0.0:8000/api/v1/touristspots/
http://0.0.0.0:8000/api/v1/favorites/
http://0.0.0.0:8000/api/v1/pictures/
```

![content_example](readme-images/5_content_example.png)

Run the tests:

```console
docker-compose run web pytest touristspots --cov=touristspots
```

Screenshots admin:

![6_admin](readme-images/6_admin.png)

Admin Touristspots:

![admin_touristspots](readme-images/7_admin_touristspots.png)

Admin Touristspots Detail:
![admin_touristspots_detail](readme-images/8_admin_touristspots_detail.png)

Admin Favorite
![admin_favorite](readme-images/9_1_admin_favorite.png)

Admin Picture
![admin_favorite](readme-images/9_2_admin_picture.png)

Example of json created:

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "Parque Dona Lindu",
      "geographical_location": {
        "type": "Point",
        "coordinates": [-34.90402578821604, -8.14141043176408]
      },
      "category": "PARK",
      "pictures": [
        {
          "id": 3,
          "picture": "http://0.0.0.0:8000/media/pic_folder/parque-dona-lindu.jpeg",
          "tourist_spot": "Parque Dona Lindu",
          "user": "Zezinho"
        },
        {
          "id": 4,
          "picture": "http://0.0.0.0:8000/media/pic_folder/recife-antigo.jpeg",
          "tourist_spot": "Parque Dona Lindu",
          "user": "Zezinho"
        },
        {
          "id": 5,
          "picture": "http://0.0.0.0:8000/media/pic_folder/museu-cais-do-sertao.jpeg",
          "tourist_spot": "Parque Dona Lindu",
          "user": "Zezinho"
        }
      ],
      "created": "2020-08-09T02:49:48.523116Z",
      "modified": "2020-08-09T14:28:59.968699Z"
    }
  ]
}
```

## Allow login with Facebook

![facebook](readme-images/10_facebook.png)

Access the link, login with your Facebook account, to generate the `Access Token`:
https://developers.facebook.com/tools/explorer/3227255577337637/

Endpoint:

![endpoint_facebook](readme-images/11_endpoint_facebook.png)

```console
http://0.0.0.0:8000/api/v1/dj-rest-auth/facebook/
```

Copy the token generated by the link and paste in `Access token`.

You will need the `Client id` and `Secret key` of the application created on Facebook, to insert in the Django Admin.

Obs.: These values are not public, they will be provided for specific people to access.

### Admin:

In the admin go to `Sites` and change `example.com` to `http://0.0.0.0:8000/`:

![admin](readme-images/12_admin.png)

![admin_sites](readme-images/13_admin_sites.png)

Change the fields to `http://0.0.0.0:8000/` and save:

![admin_sites_detail](readme-images/14_admin_sites_detail.png)

Go back to the admin's `Home` page and go to`Social applications`:

![admin_sites_home](readme-images/15_admin_sites_home.png)

Select the provider, which will be `Facebook`, choose the name: `Touristspot`, insert the `client id` and `secret key` and then switch from `Available sites` to `Chosen sites` and save:

![admin_sites_social_applications](readme-images/16_admin_sites_social_applications.png)

Access endpoint:

```console
http://0.0.0.0:8000/api/v1/dj-rest-auth/facebook/
```

![access_token](readme-images/17_access_token.png)

![token](readme-images/18_token.png)

When you’re done, don’t forget to close down your Docker container! ;)

```console
docker-compose down
```
