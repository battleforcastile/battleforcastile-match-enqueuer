FROM python:3.7-alpine

RUN mkdir /app

COPY . /app

RUN pip install pipenv

RUN pipenv install

# -- Replace with the correct path to your app's main executable
CMD uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app

EXPOSE 5000