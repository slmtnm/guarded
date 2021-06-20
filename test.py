#!/usr/bin/python

import os
import sys
import subprocess

# run all examples
def test_run():
    for root, dir, files in os.walk('./examples'):
        for example in files:
            path = root + '/' + example
            process = subprocess.run(f'python -m gclang {path} run'.split(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
            if process.stderr or process.returncode != 0:
                print(f'{path} failed')

# run all examples
def test_derive():
    for root, dir, files in os.walk('./examples'):
        for example in files:
            path = root + '/' + example
            process = subprocess.run(f'python -m gclang {path} derive'.split(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
            if process.stderr or process.returncode != 0:
                print(f'{path} failed')

print('Run:')
test_run()

print('\nDerive:')
test_derive()