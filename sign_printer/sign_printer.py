import sys
from pyfiglet import Figlet

def main():
    if len(sys.argv) != 2:
        print("Usage: python sign_printer.py <text>")
        sys.exit(1)

    text = sys.argv[1]
    f = Figlet(font="slant")
    print(f.renderText(text))

if __name__ == "__main__":
    main()
