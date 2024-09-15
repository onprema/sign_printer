example:
	@poetry run python sign_printer/sign_printer.py hello

test:
	poetry run pytest --verbose tests/

lint:
	poetry run flake8 --show-source

format:
	poetry run black --diff .

clean:
	find . -type d -name '__pycache__' -exec rm -rf {} +
