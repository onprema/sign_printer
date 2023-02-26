# sign_printer

This is a simple Python command-line application that uses the `pyfiglet` library to generate ASCII art from the text entered by the user.

## Prerequisites
To run this application, you need to have Python 3.x and the pyfiglet library installed on your system.

You can install `pyfiglet` library via `pip, by running the following command in your terminal:

```
pip install pyfiglet
```

## Usage
To use this app, navigate to the directory where the `app.py` file is located and run the following command in your terminal:

```
python figlet_app.py <text>
```
Replace `<text>` with the text for which you want to print.

## `poetry`

### Installation
```
curl -sSL https://install.python-poetry.org | python3 -
```

### Initialize
```
poetry init
```

### Install dependencies
```
poetry install
```

### Activate virtual environment
```
poetry shell
```

### Deactivate virtual environment
```
exit
```

### Run the app
```
poetry run python sign_printer/sign_printer.py <text>
```

### Uninstall
```
curl -sSL https://install.python-poetry.org | python3 - --uninstall
```
