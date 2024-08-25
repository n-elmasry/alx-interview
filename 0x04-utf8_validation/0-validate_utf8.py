#!/usr/bin/python3
"""validUTF8"""


def validUTF8(data):
    """ determines if a given data set represents a valid UTF-8 encoding."""
    # Number of bytes left to process in the current UTF-8 character
    num_bytes = 0

    for byte in data:
        # Convert the integer to its binary string representation
        binary_rep = format(byte, '#010b')[-8:]

        if num_bytes == 0:
            # Determine the number of bytes in this UTF-8 character
            if binary_rep.startswith('0'):
                continue
            elif binary_rep.startswith('110'):
                num_bytes = 1
            elif binary_rep.startswith('1110'):
                num_bytes = 2
            elif binary_rep.startswith('11110'):
                num_bytes = 3
            else:
                return False
        else:
            # For continuation bytes, they must start with '10'
            if not binary_rep.startswith('10'):
                return False

        # Decrement the number of bytes left to process
        num_bytes -= 1

    # If all bytes have been processed correctly, num_bytes should be 0
    return num_bytes == 0
