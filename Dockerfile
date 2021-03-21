FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
COPY src/ /app/
COPY pyproject.toml /app/
COPY poetry.lock /app/
WORKDIR /app
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-dev --no-interaction
