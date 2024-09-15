# sign_printer

This is a simple Python command-line application that uses the `pyfiglet` library to generate ASCII art from the text entered by the user.

### Installation and Usage
```
# pip
python -m pip install poetry

# macOS
brew install poetry

# Linux / Windows
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

### Add a package
```
poetry add pyfiglet
```

### Uninstall
```
# pip
python -m pip uninstall poetry

# macOS
brew uninstall poetry

# Linux / Windows
curl -sSL https://install.python-poetry.org | python3 - --uninstall
```
