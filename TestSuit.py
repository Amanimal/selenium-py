# -*- coding: utf-8 -*-
import subprocess
import sys
from datetime import datetime

from utilities.settings import BASE_DIR


def date_format():
    return datetime.now().strftime("%Y-%m-%d_%H%M%S")


if __name__ == '__main__':
    # browsers = ["chrome", "edge", "firefox", "opera", 'safari']
    # browsers = ["chrome", "edge", "firefox", "opera"]
    browsers = ["opera"]

    # test script directory
    test_dir = BASE_DIR / 'test_cases'

    # python venv executable path
    py_venv = sys.executable

    # reports folder path
    reports = BASE_DIR / 'reports'

    for browser in browsers:
        subprocess.run(
            [py_venv, '-m', 'pytest', '-n=3', f'--html={reports}/{date_format()}_{browser}_report.html',
             f'{test_dir}', '--browser', f'{browser}'])
