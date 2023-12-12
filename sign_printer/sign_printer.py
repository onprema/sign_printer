#!/usr/bin/env python3
"""
Module sign_printer contains the sign_printer app.
"""
import sys
import utils
from pyfiglet import Figlet


def main():
    """Main function gets called when invoked from the command-line"""
    figlet = Figlet(font=utils.random_font())
    text_to_print = " ".join(sys.argv[1:])
    print(figlet.renderText(text_to_print))


if __name__ == "__main__":
    if not utils.validate_args(sys.argv):
        print(utils.USAGE)
        sys.exit(1)
    main()
