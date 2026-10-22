#!/usr/bin/python3
"""Module for UTF-8 validation."""


def validUTF8(data):
    """Validate UTF-8 byte sequences."""
    remaining = 0

    for number in data:
        byte = number & 255

        if remaining == 0:
            if byte >> 7 == 0:
                continue
            elif byte >> 5 == 0b110:
                remaining = 1
            elif byte >> 4 == 0b1110:
                remaining = 2
            elif byte >> 3 == 0b11110:
                remaining = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            remaining -= 1

    return remaining == 0
