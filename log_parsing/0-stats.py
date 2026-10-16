#!/usr/bin/python3
"""Parse HTTP logs and print statistics."""

import sys
import re


def print_stats(total_size, status_counts):
    """Print total file size and status code counts."""
    print("File size: {}".format(total_size))

    for status in sorted(status_counts):
        if status_counts[status] > 0:
            print("{}: {}".format(status, status_counts[status]))


def main():
    """Read log lines and calculate statistics."""
    total_size = 0
    line_count = 0

    status_counts = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }

    pattern = re.compile(
        r'^\d{1,3}(?:\.\d{1,3}){3} - '
        r'\[[^\]\r\n]+\] '
        r'"GET /projects/260 HTTP/1\.1" '
        r'(\d+) (\d+)$'
    )

    try:
        for line in sys.stdin:
            line_count += 1

            match = pattern.fullmatch(line.rstrip("\r\n"))

            if match:
                status = int(match.group(1))
                file_size = int(match.group(2))

                total_size += file_size

                if status in status_counts:
                    status_counts[status] += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)

    else:
        if line_count == 0 or line_count % 10 != 0:
            print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
