#!/usr/bin/env python3
"""
A simple program that downloads a random cat image
and saves it as cat.jpg in the current directory.
"""

import urllib.request
import os

URL = 'https://cataas.com/cat'
OUTPUT_FILE = 'cat.jpg'


def main():
    print('Fetching a random cat image...')
    with urllib.request.urlopen(URL) as response:
        data = response.read()
    with open(OUTPUT_FILE, 'wb') as f:
        f.write(data)
    size_kb = len(data) / 1024
    print(f'Saved {OUTPUT_FILE} ({size_kb:.1f} KB). Enjoy!')
    if os.name == 'posix':
        try:
            import subprocess
            subprocess.Popen(['xdg-open', OUTPUT_FILE])
        except Exception:
            pass


if __name__ == '__main__':
    main()

