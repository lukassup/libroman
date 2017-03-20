#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""CLI entrypoints for libroman Python module."""

import argparse
import sys

from .roman import Roman


# TODO: translation
_ = (lambda text: text)


def parse_roman(number):
    print(Roman.parse_roman(number))


def parse_int(number):
    print(Roman.parse_int(number))


def main():
    """CLI entrypoint for libroman."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
            'number',
            metavar='NUMBER',
            help=_('Arabic or Roman numeral.'),
            type=str)
    mx_group = parser.add_mutually_exclusive_group()
    mx_group.add_argument(
            '-d',
            '--decimal',
            dest='roman',
            action='store_false',
            default=False,
            help=_('Convert from Arabic (default).'))
    mx_group.add_argument(
            '-r',
            '--roman',
            dest='roman',
            action='store_true',
            help=_('Convert from Roman.'))

    args = parser.parse_args()

    try:
        if args.roman:
            parse_roman(args.number)
        else:
            decimal = int(args.number)
            parse_int(decimal)
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
