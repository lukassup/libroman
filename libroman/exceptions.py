# -*- coding: utf-8 -*-

"""Exceptions for the `libroman` Python module."""


class RomanError(Exception):
    pass


class InvalidRomanNumeralTypeError(RomanError):
    pass


class InvalidRomanNumeralStringError(RomanError):
    pass


class InvalidRomanNumeralSequenceError(RomanError):
    pass


class OutOfBoundsNumberError(RomanError):
    pass
