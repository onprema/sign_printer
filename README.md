# sign_printer

This is a simple Python command-line application that uses the `pyfiglet` library to generate ASCII art from the text entered by the user.

## Prerequisites
To run this application, you need to have Python 3.x and `poetry` installed on your system.

You can install `poetry` by running the following command in your terminal:

```
python -m pip install poetry
```

## Usage
Run the following command in your terminal:

```
poetry install
make example
```

To print custom text, run
```
poetry run python sign_printer/sign_printer.py <text>
```
Replace `<text>` with the text for which you want to print.

## Tests
The unit tests for the sign_printer app require `pytest`, which can be installed with `pip`:

```
make test
```

## Linting

To lint the code, run the following command:

```
make lint
```

## Formatting

To format the code, run the following command:

```
make format
```

## pre-commit

### Installation

To enable the pre-commit hook, run the following command:
```
poetry run pre-commit install
```
