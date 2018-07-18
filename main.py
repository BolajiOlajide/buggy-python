#!/usr/bin/python3

import unittest

from snippets import lambda_array

if __name__ == "__main__":
    try:
        assert (-1 >= 0), "Colder than absolute zero!"
    except AssertionError as error:
        print(error)
    except:
        print('Unknown error! 😢')
