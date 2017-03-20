import unittest

from libroman.exceptions import (
    InvalidRomanNumeralTypeError,
    InvalidRomanNumeralStringError,
    InvalidRomanNumeralSequenceError,
    OutOfBoundsNumberError,
)
from libroman.roman import Roman


class TestRoman(unittest.TestCase):

    def test_roman_init_type_valid(self):
        self.assertIsInstance(Roman('I'), Roman)
        self.assertIsInstance(Roman(1), Roman)

    def test_roman_init_type_invalid(self):
        types = [
            {'foo': 'bar'},
            (0, 0),
            {1, 2, 3},
            object(),
            1.0,
        ]
        for t in types:
            with self.assertRaises(InvalidRomanNumeralTypeError):
                Roman(t)

    def test_parse_roman_from_string_valid(self):
        tests = [
            ('I',   1),
            ('II',  2),
            ('III', 3),
            ('IV',  4),
            ('V',   5),
            ('VI',  6),
            ('VII', 7),
            ('VIII', 8),
            ('IX',  9),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000),
            ('XIX', 19),
            ('CXC', 190),
            ('MCM', 1900),
            ('MMMCMXCIX', 3999),
        ]
        for numeral, value in tests:
            self.assertEqual(Roman.parse_roman(numeral), value)

    def test_parse_roman_from_string_bad_chars(self):
        tests = [
            '!I',
            'X(C',
            'iii',
            'BCD',
            'I1I',
            '\\',
            '#',
        ]
        for numeral in tests:
            with self.assertRaises(InvalidRomanNumeralStringError):
                Roman.parse_roman(numeral)

    def test_parse_roman_from_string_bad_sequence(self):
        tests = [
            'IIII',
            'XXXX',
            'VVVV',
            'MMMM',
            'DDDD',
            'LLLL',
            'CDM',
            'MDMCLIV',
            'VIV',
            'LXL',
            'DCD',
            'IXIX',
        ]
        for numeral in tests:
            with self.assertRaises(InvalidRomanNumeralSequenceError):
                Roman.parse_roman(numeral)

    def test_roman_parse_from_int_valid(self):
        tests = [
            ('I',   1),
            ('II',  2),
            ('III', 3),
            ('IV',  4),
            ('V',   5),
            ('VI',  6),
            ('VII', 7),
            ('VIII', 8),
            ('IX',  9),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000),
            ('MMMCMXCIX', 3999),
        ]
        for numeral, value in tests:
            self.assertEqual(Roman.parse_int(value), numeral)

    def test_roman_parse_from_int_out_of_bounds(self):
        tests = [
            -5000,
            -1,
            0,
            4000,
            8888,
        ]
        for arabic in tests:
            with self.assertRaises(OutOfBoundsNumberError):
                Roman.parse_int(arabic)

    def test_roman_comp_eq(self):
        tests = [
            ('I',   1),
            ('II',  2),
            ('III', 3),
            ('IV',  4),
            ('V',   5),
            ('VI',  6),
            ('VII', 7),
            ('VIII', 8),
            ('IX',  9),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000),
            ('MMMCMXCIX', 3999),
        ]
        for numeral, value in tests:
            self.assertTrue(Roman(numeral) == Roman(value))

    def test_roman_comp_gt(self):
        tests = [
            ('II',  2),
            ('III', 3),
            ('IV',  4),
            ('V',   5),
            ('VI',  6),
            ('VII', 7),
            ('VIII', 8),
            ('IX',  9),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000),
            ('MMMCMXCIX', 3999),
        ]
        for numeral, value in tests:
            self.assertTrue(Roman(numeral) > Roman(value - 1))

    def test_roman_length(self):
        tests = [
            'VI',
            'VII',
            'VIII',
            'IX',
            'X',
            'L',
            'C',
            'D',
            'M',
            'MMMCMXCIX',
        ]
        for numeral in tests:
            self.assertEqual(len(Roman(numeral)), len(numeral))
