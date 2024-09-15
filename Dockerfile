FROM python:3.9.16-slim-buster

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install poetry && poetry install

COPY . .

ENTRYPOINT ["poetry", "run", "python", "sign_printer/sign_printer.py"]
