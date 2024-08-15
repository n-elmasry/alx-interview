#!/usr/bin/python3
""" A script that reads stdin line by line and computes metrics """

import sys
import re

input_format = r'^(\d{1,3}\.){3}\d{1,3} - \[\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2} [+-]\d{4}\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
status_count = {code: 0 for code in status_codes}

total_file_size = 0
line_count = 0

try:
    for line in sys.stdin:
        match = re.match(input_format, line)
        if match:
            line_count += 1
            status_code = int(match.group(2))  # Group 2 is the status code
            file_size = int(match.group(3))  # Group 3 is the file size

            total_file_size += file_size
            if status_code in status_count:
                status_count[status_code] += 1

            if line_count % 10 == 0:
                print(f'File size: {total_file_size}')
                for code in sorted(status_codes):
                    if status_count[code] > 0:
                        print(f'{code}: {status_count[code]}')

except KeyboardInterrupt:
    pass

finally:
    # Print the final metrics after the loop ends or on keyboard interrupt
    print(f'File size: {total_file_size}')
    for code in sorted(status_codes):
        if status_count[code] > 0:
            print(f'{code}: {status_count[code]}')
