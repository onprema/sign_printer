"""
test_utils contains unit tests for the sign_printer utilities.
"""
import pytest
from sign_printer.utils import FONTS, random_font, validate_args


def test_fonts_are_strings():
    """Fonts should be strings"""
    assert all(isinstance(font, str) for font in FONTS)


def test_random_font_returns_a_random_font():
    """random_font should return a font from the list of fonts."""
    result = random_font()
    assert result in FONTS


def test_required_argument():
    """At least one argument needs to passed from the user."""
    args = ["sign_printer.py", "hello"]
    assert validate_args(args)

    args = ["sign_printer.py"]
    assert not validate_args(args)
