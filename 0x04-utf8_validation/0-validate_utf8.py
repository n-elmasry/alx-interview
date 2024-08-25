#!/usr/bin/python3
"""validUTF8"""


def validUTF8(data):
    """ determines if a given data set represents a valid UTF-8 encoding"""

    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the significant bits
    mask1 = 1 << 7    # 10000000
    mask2 = 1 << 6    # 01000000

    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            # 1-byte character
            if num_bytes == 0:
                continue

            # If the number of bytes is more than 4 or 1
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # For the subsequent bytes, they must start with '10xxxxxx'
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrease the number of bytes to process
        num_bytes -= 1

    # If there are still bytes remaining, the data is invalid
    return num_bytes == 0
