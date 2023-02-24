

from pyfiglet import Figlet
f= Figlet(font = "slant")
import sys
s = sys.argv[1]


print(f.renderText(s))
