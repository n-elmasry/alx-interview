#!/usr/bin/python3
""" a script that reads stdin line by line and computes metrics"""

import sys


def print_message(status_codes, total_file_size):
    """ printing message """

    print("File size: {}".format(total_file_size))
    for key, val in sorted(status_codes.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_file_size = 0
code = 0
line_count = 0
status_codes = {"200": 0,
                "301": 0,
                "400": 0,
                "401": 0,
                "403": 0,
                "404": 0,
                "405": 0,
                "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            line_count += 1

            if line_count <= 10:
                total_file_size += int(parsed_line[0])  # file size
                code = parsed_line[1]  # status code

                if (code in status_codes.keys()):
                    status_codes[code] += 1

            if (line_count == 10):
                print_message(status_codes, total_file_size)
                line_count = 0

finally:
    print_message(status_codes, total_file_size)
