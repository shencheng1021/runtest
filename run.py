# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import os
import unittest

if __name__ == '__main__':
    print(os.path.dirname(__file__))
    suite=unittest.defaultTestLoader.discover("./test_case",pattern="test_*.py")
    unittest.main(defaultTest='suite',verbosity=0)