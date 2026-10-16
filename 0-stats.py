#!/usr/bin/python3
import sys


def print_statistics(total_file_size, status_counts):
    """Prints the accumulated metrics."""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


if __name__ == "__main__":
    total_file_size = 0
    line_count = 0
    valid_status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    status_counts = {code: 0 for code in valid_status_codes}

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            
            if len(parts) >= 2:
                try:
                    file_size = int(parts[-1])
                    total_file_size += file_size
                except ValueError:
                    pass

                try:
                    status_code = parts[-2]
                    if status_code in status_counts:
                        status_counts[status_code] += 1
                except IndexError:
                    pass

            if line_count == 10:
                print_statistics(total_file_size, status_counts)
                line_count = 0

    except KeyboardInterrupt:
        print_statistics(total_file_size, status_counts)
        raise

    print_statistics(total_file_size, status_counts)
