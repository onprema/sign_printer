"""
Module sign_printer contains the sign_printer app.
"""
import sys
import utils
from pyfiglet import Figlet


figlet = Figlet(font=utils.random_font())
s = sys.argv[1]


print(f.renderText(s))
