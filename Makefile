test:
	poetry run pytest --verbose tests/

lint:
	poetry run flake8 --show-source

format:
	poetry run black --diff .