# Pull base image
FROM python:3.7-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system

# Copy project
COPY . /code/

RUN pip shell
RUN python /code/manage.py runserver 0.0.0.0:8000

EXPOSE 8000