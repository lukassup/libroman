# -*- coding: utf-8 -*-

"""Python library to deal with Roman numerals.

All functionality is provided by the `Roman` class.
"""

from .exceptions import (
    InvalidRomanNumeralTypeError,
    InvalidRomanNumeralStringError,
    InvalidRomanNumeralSequenceError,
    OutOfBoundsNumberError,
)


class Roman(object):

    """Roman numeral."""

    VALID = set('IVXLCDM')
    DIGITS = [
        ('M',  1000, 3),
        ('CM',  900, 1),
        ('D',   500, 1),
        ('CD',  400, 1),
        ('C',   100, 3),
        ('XC',   90, 1),
        ('L',    50, 1),
        ('XL',   40, 1),
        ('X',    10, 3),
        ('IX',    9, 1),
        ('V',     5, 1),
        ('IV',    4, 1),
        ('I',     1, 3),
    ]

    def __init__(self, number):
        """Initialize with a Roman numeral or Arabic integer.

        :number: str or int
        """
        # check if number has the correct type: str or int
        if isinstance(number, str):
            self.roman = number
            self.arabic = self.parse_roman(self.roman)
        elif isinstance(number, int):
            self.roman = self.parse_int(number)
            self.arabic = number
        else:
            raise InvalidRomanNumeralTypeError()

    def __repr__(self):
        return '{0}({1!r})'.format(
                self.__class__.__name__,
                self.roman)

    def __str__(self):
        return self.roman

    def __eq__(self, other):
        return self.arabic == other.arabic

    def __gt__(self, other):
        return self.arabic > other.arabic

    def __len__(self):
        return len(self.roman)

    @classmethod
    def parse_roman(cls, roman):
        """Convert a Roman numeral to an Arabic number.

        :returns: int
        """
        if not roman:
            raise InvalidRomanNumeralStringError(
                    'Roman numeral cannot be blank.')
        # check if contains invalid numerals
        if not cls.VALID.issuperset(set(roman)):
            raise InvalidRomanNumeralStringError(
                    'Roman numeral contains invalid characters, '
                    'only MDCLXVI are allowed.')
        _roman = roman
        arabic = 0
        for digit, value, repeat in cls.DIGITS:
            # count repeating Roman numerals
            seq = 0
            while _roman.startswith(digit):
                seq += 1
                # ...as there can only be 1 consecutive two-digit numeral or 3
                # single-digit Roman numerals
                if seq > repeat:
                    raise InvalidRomanNumeralSequenceError(
                            'There cannot be more than three consecutive Roman numerals '
                            'or more than one subtractive numeral combination (e.g. IX).')
                arabic += value
                # cut the numeral from the left by one digit and
                # try another while loop
                _roman = _roman[len(digit):]
        # comparing the original with the reverse
        if len(_roman) > 0 or cls.parse_int(arabic) != roman:
            raise InvalidRomanNumeralSequenceError(
                    'Roman numeral contains an invalid trailing sequence. '
                    'Maybe the numers are out of order?')
        return arabic

    @classmethod
    def parse_int(cls, arabic):
        """Convert an Arabic number to Roman numeral.

        :returns: str
        """
        roman = ''
        arabic = arabic
        if not 0 < arabic < 4000:
            raise OutOfBoundsNumberError(
                    'Valid Roman numerals are in the range of [1, 3999].')
        for digit, value, _ in cls.DIGITS:
            while arabic >= value:
                roman += digit
                arabic -= value
        return roman

    @classmethod
    def from_str(cls, roman):
        """Initialize a Roman numeral from string (same as constructor)."""
        return cls(roman)

    @classmethod
    def from_int(cls, arabic):
        """Initialize a Roman numeral from an integer."""
        return cls(cls.parse_int(arabic))
