"""
utils contains utilities for the sign_printer app.
"""
import random

USAGE = "Usage: python sign_printer <text>"


FONTS = [
   "1943____",
   "3-d",
   "3x5",
   "4x4_offr",
   "acrobatic",
   "advenger",
   "alligator",
   "alligator2",
   "alphabet",
   "aquaplan",
   "arrows",
   "atc_gran",
   "avatar",
   "banner",
   "banner3",
   "banner3-D",
   "banner4",
   "barbwire",
   "basic",
   "battle_s",
   "battlesh",
   "baz__bil",
   "beer_pub",
   "bell",
   "big",
   "bigchief",
   "binary",
   "block",
   "brite",
   "briteb",
   "britebi",
   "britei",
   "broadway",
   "bubble",
   "bubble_b",
   "bulbhead",
   "calgphy2",
   "caligraphy",
   "catwalk",
   "caus_in_",
   "chartr",
   "chartri",
   "italics_",
   "letters",
   "letterw3",
   "lexible_",
   "linux",
   "lockergnome",
   "mad_nurs",
   "madrid",
   "magic_ma",
   "marquee",
   "runyc",
   "sansb",
   "sansbi",
   "sansi",
   "sblood",
   "sbookbi",
   "z-pilot_",
   "zig_zag_",
]


def random_font():
   """Returns a random pyfiglet font."""
   return random.choice(FONTS)


def validate_args(args):
   """Validates the arguments passed from the command-line."""
   if len(args) > 1:
      return True
   return False