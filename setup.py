from setuptools import setup

_NAME = 'prodoku'
_AUTHOR = 'Anthony Frazier'
_VERSION = '0.0.1'
_DESCRIPTION = """ prodoku is an all-in-one Sudoku implementation native to Python-3. It offers puzzle-generation, puzzle-solving, and solution validation. """
_AUTHOR_EMAIL = 'anthonymfrazier1998@gmail.com'

setup (
    name = _NAME,
    version=_VERSION,
    description = _DESCRIPTION,
    author= _AUTHOR,
    author_email = _AUTHOR_EMAIL,
    packages = ['prodoku'],
    license = 'MIT',
    url='https://github.com/afraz98/prodoku'
)
