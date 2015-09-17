∆∆∆ ~ WELCOME TO THE CAFE SERVER CODE ~ ∆∆∆

first make sure you have psycopg installed and
that cafe/cafe/settings.py is pointed at the right database

and that celery is pointed at the right rabbitMQ instance

sudo python -m pip install Django==1.8.4

pip install celery
pip install requests

$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver