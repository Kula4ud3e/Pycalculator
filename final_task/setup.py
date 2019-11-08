from setuptools import setup, Extension

setup(
    name='pycalc',
    version='1.0.0',
    description='Pure-python command-line calculator.',
    author='Vlad Kulakovskiy',
    author_email='kula4ud3e@gmail.com',
    packages=['pycalc'],
    entry_points={
        'console_scripts': [
            'pycalc=pycalc.calc:main',
        ],
    },
)
