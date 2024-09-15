# sign_printer

This is a simple Python command-line application that uses the `pyfiglet` library to generate ASCII art from the text entered by the user.

## Prerequisites
To run this application, you need to have Python 3.x and the `virtualenv` module.

You can install `virtualenv` library via `pip`, by running the following command in your terminal:

```
pip install virtualenv
```

## Usage

Create a virtual environment, run the following command:

```
python -m venv sign_printer_venv
```

To activate the virtual environment, run the following command:

```
source sign_printer_venv/bin/activate
```

To install the app's dependencies, run the following command:

```
pip install -r requirements.txt
```

To use this app, navigate to the directory where the `app.py` file is located and run the following command in your terminal:

```
python sign_printer/sign_printer.py <text>
```
Replace `<text>` with the text for which you want to print.

Example:
```
$ python sign_printer/sign_printer.py "hello world"
                                                    
                                                    
##        ##  ##                          ##    ##  
 #         #   #                           #     #  
 ###   ##  #   #   ##    ## # #  ##  ####  #   ###  
 # #  ###  #   #  #  #   # ## # #  #  # #  #  #  #  
 # #  #    #   #  #  #    ####  #  #  #    #  #  #  
#####  ## ### ###  ##     #  #   ##  ###  ### ##### 
                                                    
```

To exit the virtual environment, run the following command:

```
deactivate
```


## Tests

To run the tests, use the following command:

```
pytest
```

## Linting

To lint the code, run the following command:

```
flake8
```

# Formatting

To format the code, run the following command:

```
black sign_printer
```

