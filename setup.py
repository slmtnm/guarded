from setuptools import setup

setup(
    name="guarded",
    version='0.0.0',
    py_modules=['guarded'],
    install_requires=[
        'Click',
        'sympy==1.7.1',
        'click==7.1.2',
        'antlr4-python3-runtime==4.9.1'
    ],
    entry_points='''
        [console_scripts]
        guarded=guarded.__main__:cli
    ''',
)
