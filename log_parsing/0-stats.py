#!/usr/bin/python3
"""Parse HTTP logs and print statistics."""

import re
import sys


def print_stats(total_size, status_counts):
    """Print total size and status code counts."""
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
        r'^\S+\s+-\s+'
        r'\[[^\]\r\n]+\]\s+'
        r'"GET /projects/260 HTTP/1\.1"\s+'
        r'(\S+)\s+(\d+)\s*$'
    )

    try:
        for line in sys.stdin:
            line_count += 1

            match = pattern.fullmatch(line.rstrip("\r\n"))

            if match:
                status_text = match.group(1)
                file_size = int(match.group(2))

                total_size += file_size

                try:
                    status = int(status_text)
                except ValueError:
                    status = None

                if status in status_counts:
                    status_counts[status] += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)

    else:
        if line_count == 0 or line_count % 10 != 0:
            print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
