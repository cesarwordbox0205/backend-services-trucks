FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN apt-get update && apt-get -y install cron

COPY src/ /app/
COPY pyproject.toml /app/
COPY poetry.lock /app/
#Copy the crontab specification to the place the cron scheduler can pick it up
COPY src/resources/crontabs/root /var/spool/cron/crontabs/root
RUN chmod 0644 /var/spool/cron/crontabs/root && crontab /var/spool/cron/crontabs/root
WORKDIR /app
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-dev --no-interaction
