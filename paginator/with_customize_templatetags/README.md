# Paginator with customized templatetags

## Brief

This example shows how to use Paginator and some custom template tags.

## Start

### Go to the project folder

_If you are in the root folder of this repository._

```zsh
cd paginator/with_customize_templatetags
```

### Setup Virtual ENV & Install packages

```zsh
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

### Run Django migration

_The migration script of this project will automatically insert a thousand records of test data._

```zsh
python3 manage.py migrate
```

### Start service

_`localhost:8000` is the default site._

```zsh
python3 manage.py runserver
```
