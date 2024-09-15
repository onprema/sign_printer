poetry-setup:
	python -m pip install poetry
	poetry install

test: poetry-setup
	poetry run pytest --verbose tests/

lint: poetry-setup
	poetry run flake8 --show-source

format: poetry-setup
	poetry run black --diff .

clean:
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -type d -name '.pytest_cache' -exec rm -rf {} +

build:
	docker build --tag sign_printer .

run: build
	docker run sign_printer $(text)
