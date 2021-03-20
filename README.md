# Django API Starter Kit

## Create enviroment

Create a virtual enviroment and install dependencies

```sh
$> virtualenv .env
$>source .env/bin/activate
(.env)$> pip install -r requirements.txt
```

To exit virtual enviroment

```sh
(.env)$> deactivate
```

## Create django app

```sh
(.env)$> django-admin startproject app
(.env)$> cd app
(.env)$> python3 manage.py  startapp api
manage.py makemigrations
manage.py migrate
manage.py createsuperuser
manage.py createsuperuser --noinput --username admin --email admin@fuf.me

DJANGO_SUPERUSER_PASSWORD=ammin ./manage.py createsuperuser \
    --no-input \
    --username=admin \
    --email=admin@fuf.me
```
    """
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    """