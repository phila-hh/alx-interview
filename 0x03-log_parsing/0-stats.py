#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics
"""
import re


def run():
    """Executes the log parser"""
    file_size = 0
    line_number = 0
    status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            file_size = update_metrics(line, file_size, status_codes)
            line_number += 1
            if line_number % 10 == 0:
                print_stats(file_size, status_codes)
    except (KeyboardInterrupt, EOFError):
        print_stats(file_size, status_codes)


def update_metrics(line, f_size, s_codes):
    """Updates the metrics"""
    line_info = extract_input(line)
    status_code = line_info.get("status_code", '0')
    if status_code in s_codes.keys():
        s_codes[status_code] += 1
    return f_size + line_info['file_size']


def extract_input(line):
    """Extracts input from a given line"""
    info = {
        'status_code': 0,
        'file_size': 0,
    }

    log_format = "{}\\-{}{}{}{}\\s*'".format(fp[0], fp[1], fp[2], fp[3], fp[4])
    resp_match = re.fullmatch(log_format, line)
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        f_size = int(resp_match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = f_size
    return info


def print_stats(f_size, s_codes):
    """Prints the statistics"""
    print("File size: {:d}".format(f_size), flush=True)
    for status_code in sorted(s_codes.keys()):
        number = s_codes.get(status_code, 0)
        if number > 0:
            print("{:s}: {:d}".format(status_code, number), flush=True)


if __name__ == '__main__':
    run()
