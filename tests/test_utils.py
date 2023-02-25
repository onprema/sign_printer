"""
test_utils contains unit tests for the sign_printer utilities.
"""
import pytest
from sign_printer.utils import FONTS, random_font


def test_fonts_are_strings():
    assert all(isinstance(font, str) for font in FONTS)


def test_random_font_returns_a_random_font():
    result = random_font()
    assert result in FONTS
