[WIP]

# About
This is the back-end to a deal flow management Next.js app ([https://github.com/jcaguirre89/crm-frontend/](repo)).
It includes authorization and the deal flow models, and the front end won't work without it.

# Local development
The app is dockerized and follows the django-cookiecutter structure as closely as possible. A lot of code came directly
from their [excellent repo](https://github.com/pydanny/cookiecutter-django). 

Most commands are run via docker-compose, and you can run django commands with 
```
docker-compose -f local.yml run --rm django python manage.py your_command
```

To run locally, first run migrations and create superuser

```
docker-compose -f local.yml run --rm django python manage.py migrate
docker-compose -f local.yml run --rm django python manage.py createsuperuser
```

And then run the stack (you might have to run this before the previous commands in order to build—not sure)
The `--build` flag is not necessary in posterior runs if you only modify the django code.

```
docker-compose -f local.yml up --build
```

For local development, the container is linked to the local filesystem so after the first build, you can develop
locally and the changes will be reflected in real time.

# Auth
The app uses Token authorization and has session auth disabled, so the only way to test the api is via an
app like Postman that allows you to include Authorization headers. This header must have the following syntax:
`Authorization: Token xxx`.

To get started, run the createsuperuser mgt. command and then create a token by sending a POST request to 
`localhost:8000/api-token-auth` with the username and password in the body, or by going directly to the
django admin in `localhost:8000/admin` and manually creating one.
