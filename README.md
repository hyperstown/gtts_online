# GTTS ONLINE

## Installation

```bash
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

## Starting development server

```bash
$ redis-server 
```

```bash
$ python manage.py runserver 
```

If you starting development server for a first time make sure to run these commands to apply migrations and create new superuser.

```bash
$ python manage.py migrate 
```
```bash
$ python manage.py createsuperuser 
```

## Usage example 

`$ curl http://127.0.0.1:8000/sound?tl=ja&text=走る`

