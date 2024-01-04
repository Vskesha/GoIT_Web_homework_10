FROM python:3.11-slim

ENV APP_HOME /app

WORKDIR $APP_HOME

RUN mkdir -p $APP_HOME/hw10project/static
RUN mkdir -p $APP_HOME/hw10project/media

COPY pyproject.toml $APP_HOME/pyproject.toml
COPY poetry.lock $APP_HOME/poetry.lock

RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --only main

COPY hw10project/ $APP_HOME/hw10project/

EXPOSE 8000

CMD ["python", "hw10project/manage.py", "runserver", "0.0.0.0:8000"]
LABEL maintainer="vskesha@gmail.com"