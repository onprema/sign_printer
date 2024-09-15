# sign_printer

This is a simple Python command-line application that uses the `pyfiglet` library to generate ASCII art from the text entered by the user.

## Prerequisites
To run this application, you need to have [Docker](https://docs.docker.com/engine/install/) installed on your system.


## Usage
Run the following command in your terminal:

```
make run text="hello world"
```

(change `hello world" to whatever you want to be printed)


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
