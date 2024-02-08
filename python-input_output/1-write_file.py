#!/usr/bin/python3
"""function that reads a text file (UTF8) and prints it to stdout"""


def write_file(filename="", text=""):
    """function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    return len(text)
