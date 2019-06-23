# Marketplace for greenhouse

## 1. Development

This apps developed by using stacks:

- Python 3.7
- Django 2.2
- PostgreSQL

## 2. Installation

1. activate your python virtualenv

2. install dependencies by run

```pip install -r requirements.txt```

3. create DB with name `greenhouse_db` on your postgres or you can setup different DB with modify `DATABASES` on `settings.py`

4. migrate migrations by run

```python manage.py migrate```

5. create your admin user by run

```python manage.py createsuperuser```

6. run local server by run

```python manage.py runserver```

