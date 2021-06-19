#!/usr/bin/python

import os
import sys
import subprocess

# run all examples
def test_run():
    for example in os.listdir('./examples'):
        process = subprocess.run(f'python -m gclang ./examples/{example} run'.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        if process.stderr or process.returncode != 0:
            print(f'{example} failed')

# run all examples
def test_derive():
    for example in os.listdir('./examples'):
        process = subprocess.run(f'python -m gclang ./examples/{example} derive'.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        if process.stderr or process.returncode != 0:
            print(f'{example} failed')

print('Run:')
test_run()

print('\nDerive:')
test_derive()