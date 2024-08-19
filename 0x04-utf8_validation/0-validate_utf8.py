#!/usr/bin/python3
"""Task 0 Module"""


def validUTF8(data) -> bool:
    """method that determines if a given data set
    represents a valid UTF-8 encoding.
    """
    ex_bytes = 0

    UTF8_BIT_1 = 1 << 7
    UTF8_BIT_2 = 1 << 6

    for byte in data:
        lead_mask = 1 << 7

        if ex_bytes == 0:
            while lead_mask & byte:
                ex_bytes += 1
                lead_mask = lead_mask >> 1

            if ex_bytes == 0:
                continue
            if ex_bytes == 1 or\
                    ex_bytes > 4:
                return False
        else:
            if not (byte & UTF8_BIT_1 and not (byte & UTF8_BIT_2)):
                return False
        ex_bytes -= 1

    if ex_bytes == 0:
        return True
    else:
        return False
